import requests
from datetime import datetime
import time
import pandas as pd
import openpyxl
import os
import random




cookies = {
    'spid': '1740773648901_03ce84baa4c82c6610c75f9fd906c1db_3v494ab2t8ffk1ax',
    '_ga': 'GA1.1.2064951896.1740773652',
    '_ym_uid': '174077365388109578',
    '_ym_d': '1740773653',
    'uxs_uid': '949d6f70-f610-11ef-b11c-2111ca80d1e4',
    'scbsid_old': '2725937795',
    'mindboxDeviceUUID': 'd6b3597d-4b0b-4e45-8167-0b84971b36f7',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22d6b3597d-4b0b-4e45-8167-0b84971b36f7%22%7D',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    'adrcid': 'A0r9KB4fc8duMUv2jPsp-tg',
    'adrcid': 'A0r9KB4fc8duMUv2jPsp-tg',
    'tmr_lvid': '745e302fb5afadd050cb5589922668f8',
    'tmr_lvidTS': '1742231271404',
    'USE_COOKIE_CONSENT_STATE': '{%22session%22:true%2C%22persistent%22:true%2C%22necessary%22:true%2C%22preferences%22:true%2C%22statistics%22:true%2C%22marketing%22:true%2C%22firstParty%22:true%2C%22thirdParty%22:true}',
    'SCBnotShow': '-1',
    'smFpId_old_values': '%5B%228ffe7a1c09dffb649545b8fc0287fbcd%22%2C%22d4b1bc3704ccd15e3c8b66eb1c6b08fb%22%5D',
    'spsc': '1742460686344_941a5bff0a8fb6b38fbd03cf3851d62f_e6cfb3ea8f0a0fa28cc6ebefdcae8ea5',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    'PHPSESSID': 'vcpd2bhdfan8otr3ct81e420nj',
    'domain_sid': 'iYISHPzp6DZDrnhbZ--l6%3A1742460687954',
    '_cmg_csstvfLiQ': '1742460688',
    '_comagic_idvfLiQ': '10012218048.14208108458.1742460688',
    'tmr_detect': '0%7C1742460689236',
    'sessionId': '17424606894535847684',
    'acs_3': '%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1742547091063%2C%22sl%22%3A%7B%22224%22%3A1742460691063%2C%221228%22%3A1742460691063%7D%7D',
    'acs_3': '%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1742547091063%2C%22sl%22%3A%7B%22224%22%3A1742460691063%2C%221228%22%3A1742460691063%7D%7D',
    'adrdel': '1742460691080',
    'adrdel': '1742460691080',
    'sma_session_id': '2230852518',
    'SCBfrom': '',
    'SCBporogAct': '5000',
    'SCBstart': '1742460691763',
    'sma_postview_ready': '1',
    '_ga_H5S7YBLWM3': 'GS1.1.17424606894535847684.3.1.1742461606.0.0.0',
    '_ga_70ZZHDSCR6': 'GS1.1.1742460689.3.1.1742461606.34.0.0',
    'SCBindexAct': '3308',
    'sma_index_activity': '16014',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'authorization': '',
    'baggage': 'sentry-environment=production,sentry-public_key=64d42d1ec99f4044ff0df570a905dbca,sentry-trace_id=07d7dc6bf0f34132b9e34ffd3abdeb16,sentry-sample_rate=0.1,sentry-transaction=%2Fflats%2F,sentry-sampled=false',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.mr-group.ru/flats/',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '07d7dc6bf0f34132b9e34ffd3abdeb16-855b033fff845948-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    # 'cookie': 'spid=1740773648901_03ce84baa4c82c6610c75f9fd906c1db_3v494ab2t8ffk1ax; _ga=GA1.1.2064951896.1740773652; _ym_uid=174077365388109578; _ym_d=1740773653; uxs_uid=949d6f70-f610-11ef-b11c-2111ca80d1e4; scbsid_old=2725937795; mindboxDeviceUUID=d6b3597d-4b0b-4e45-8167-0b84971b36f7; directCrm-session=%7B%22deviceGuid%22%3A%22d6b3597d-4b0b-4e45-8167-0b84971b36f7%22%7D; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; adrcid=A0r9KB4fc8duMUv2jPsp-tg; adrcid=A0r9KB4fc8duMUv2jPsp-tg; tmr_lvid=745e302fb5afadd050cb5589922668f8; tmr_lvidTS=1742231271404; USE_COOKIE_CONSENT_STATE={%22session%22:true%2C%22persistent%22:true%2C%22necessary%22:true%2C%22preferences%22:true%2C%22statistics%22:true%2C%22marketing%22:true%2C%22firstParty%22:true%2C%22thirdParty%22:true}; SCBnotShow=-1; smFpId_old_values=%5B%228ffe7a1c09dffb649545b8fc0287fbcd%22%2C%22d4b1bc3704ccd15e3c8b66eb1c6b08fb%22%5D; spsc=1742460686344_941a5bff0a8fb6b38fbd03cf3851d62f_e6cfb3ea8f0a0fa28cc6ebefdcae8ea5; _ym_isad=2; _ym_visorc=b; PHPSESSID=vcpd2bhdfan8otr3ct81e420nj; domain_sid=iYISHPzp6DZDrnhbZ--l6%3A1742460687954; _cmg_csstvfLiQ=1742460688; _comagic_idvfLiQ=10012218048.14208108458.1742460688; tmr_detect=0%7C1742460689236; sessionId=17424606894535847684; acs_3=%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1742547091063%2C%22sl%22%3A%7B%22224%22%3A1742460691063%2C%221228%22%3A1742460691063%7D%7D; acs_3=%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1742547091063%2C%22sl%22%3A%7B%22224%22%3A1742460691063%2C%221228%22%3A1742460691063%7D%7D; adrdel=1742460691080; adrdel=1742460691080; sma_session_id=2230852518; SCBfrom=; SCBporogAct=5000; SCBstart=1742460691763; sma_postview_ready=1; _ga_H5S7YBLWM3=GS1.1.17424606894535847684.3.1.1742461606.0.0.0; _ga_70ZZHDSCR6=GS1.1.1742460689.3.1.1742461606.34.0.0; SCBindexAct=3308; sma_index_activity=16014',
}

today = '2025-03-20'
params = {
    'category': 'flats',
    'page': '1',
    'limit': '500',
}

flats = []

def extract_digits_or_original(s):
    digits = ''.join([char for char in s if char.isdigit()])
    return int(digits) if digits else s

while True:

    response = requests.get('https://www.mr-group.ru/api/sale/products', params=params, cookies=cookies, headers=headers)

    items = response.json()["items"]

    for i in items:

        url = ""

        date = today
        project = i["project"]["name"]
        english = ''
        promzona = ''
        mestopolozhenie = ''
        subway = ''
        distance_to_subway = ''
        time_to_subway = ''
        mck = ''
        distance_to_mck = ''
        time_to_mck = ''
        bkl = ''
        distance_to_bkl = ''
        time_to_bkl = ''
        status = ''
        start = ''
        comment = ''
        developer = "MR"
        okrug = ''
        district = ''
        adress = ''
        eskrou = ''
        korpus = i["building"]["name"]
        konstruktiv = ''
        klass = ''
        # Преобразование строки в объект datetime
        date_obj = datetime.fromisoformat(i['building']['deadline'])

        # Определение квартала
        month = date_obj.month
        year = date_obj.year

        # Определяем квартал
        if 1 <= month <= 3:
            quarter = 1
        elif 4 <= month <= 6:
            quarter = 2
        elif 7 <= month <= 9:
            quarter = 3
        else:
            quarter = 4

        # Формируем итоговую строку
        srok_sdachi = f"{quarter} квартал {year} года"
        srok_sdachi_old = ''
        stadia = ''
        dogovor = ''
        type = ''
        if i["decoration"]["name"] == "MR Base":
            finish_type = "Предчистовая отделка"
        elif i["decoration"]["name"] == "MR Ready":
            finish_type = "С отделкой"
        else:
            finish_type = i["decoration"]["name"]
        room_count = int(i["rooms_number"])
        area = i["area"]
        price_per_metr = ''
        if i['discount']:
            old_price = i["price"]
            price = i['discount']['price']
        else:
            old_price = ""
            price = i["price"]

        discount = ''
        price_per_metr_new = ''

        section = ''
        floor = i["floor"]
        flat_number = ''

        print(
            f"{project}, {url}, дата: {date}, комнаты: {room_count}, площадь: {area}, цена: {price}, старая цена: {old_price}, корпус: {korpus}, этаж: {floor}")
        result = [date, project, english, promzona, mestopolozhenie, subway, distance_to_subway, time_to_subway, mck, distance_to_mck, time_to_mck, distance_to_bkl,
              time_to_bkl, bkl, status, start, comment, developer, okrug, district, adress, eskrou, korpus, konstruktiv, klass, srok_sdachi, srok_sdachi_old,
              stadia, dogovor, type, finish_type, room_count, area, price_per_metr, old_price, discount, price_per_metr_new, price, section, floor, flat_number]
        flats.append(result)
    params["page"] = str(int(params["page"]) + 1)
    sleep_time = random.uniform(10, 15)
    time.sleep(sleep_time)
    if not items:
        print("Всё скачано. Переходим к загрузке в файл")
        break

df = pd.DataFrame(flats, columns=['Дата обновления',
 'Название проекта',
 'на англ',
 'промзона',
 'Местоположение',
 'Метро',
 'Расстояние до метро, км',
 'Время до метро, мин',
 'МЦК/МЦД/БКЛ',
 'Расстояние до МЦК/МЦД, км',
 'Время до МЦК/МЦД, мин',
 'БКЛ',
 'Расстояние до БКЛ, км',
 'Время до БКЛ, мин',
 'статус',
 'старт',
 'Комментарий',
 'Девелопер',
 'Округ',
 'Район',
 'Адрес',
 'Эскроу',
 'Корпус',
 'Конструктив',
 'Класс',
 'Срок сдачи',
 'Старый срок сдачи',
 'Стадия строительной готовности',
 'Договор',
 'Тип помещения',
 'Отделка',
 'Кол-во комнат',
 'Площадь, кв.м',
 'Цена кв.м, руб.',
 'Цена лота, руб.',
 'Скидка,%',
 'Цена кв.м со ск, руб.',
 'Цена лота со ск, руб.',
 'секция',
 'этаж',
 'номер'])

current_date = today

# Базовый путь для сохранения
base_path = r"C:\PycharmProjects\SeleniumParcer\MR"

folder_path = os.path.join(base_path, str(current_date))
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

filename = f"{developer}_{current_date}.xlsx"

# Полный путь к файлу
file_path = os.path.join(folder_path, filename)

# Сохранение файла в папку
df.to_excel(file_path, index=False)

