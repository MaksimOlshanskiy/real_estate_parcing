import requests
import datetime
import time
import pandas as pd
import openpyxl
import os
import random


cookies = {
    'spid': '1741784632987_62d30c366d1e5b195ad803dff541d343_rmtsfh281m20htua',
    '_ym_uid': '1741784635438762062',
    '_ym_d': '1741784635',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    'tmr_lvid': '1c335b6614b3f392afef8213cbdc301d',
    'tmr_lvidTS': '1741784635189',
    '_cmg_csstvfLiQ': '1741784636',
    '_comagic_idvfLiQ': '9972780428.14161949863.1741784636',
    'domain_sid': 'OIbdJw_MXh1IehKOV3pwu%3A1741784636224',
    'USE_COOKIE_CONSENT_STATE': '{%22session%22:true%2C%22persistent%22:true%2C%22necessary%22:true%2C%22preferences%22:true%2C%22statistics%22:true%2C%22marketing%22:true%2C%22firstParty%22:true%2C%22thirdParty%22:true}',
    'tmr_detect': '0%7C1741784637480',
    'PHPSESSID': 'mfaplogjpoo3c4l2rpo18rnhgd',
    'PHPSESSID': 'go27flrpeer096u36lnh1nr0cd',
    'spsc': '1741784634908_1f432569f1c66728e15ccaae8f849953_e6cfb3ea8f0a0fa28cc6ebefdcae8ea5',
    '_ga': 'GA1.1.835945232.1741784643',
    'sessionId': '17417846437533915324',
    'adrdel': '1741784645914',
    'adrdel': '1741784645914',
    'adrcid': 'Ad53EZahiTy4QvZYZHYhh0Q',
    'adrcid': 'Ad53EZahiTy4QvZYZHYhh0Q',
    'acs_3': '%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1741871045923%2C%22sl%22%3A%7B%22224%22%3A1741784645923%2C%221228%22%3A1741784645923%7D%7D',
    'acs_3': '%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1741871045923%2C%22sl%22%3A%7B%22224%22%3A1741784645923%2C%221228%22%3A1741784645923%7D%7D',
    'mindboxDeviceUUID': 'b8b42419-45ee-4a92-8e84-640b5c64455a',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22b8b42419-45ee-4a92-8e84-640b5c64455a%22%7D',
    'scbsid_old': '2746015342',
    'uxs_uid': '7adaf8b0-ff42-11ef-978b-e730cc09ad57',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    '_ga_H5S7YBLWM3': 'GS1.1.17417846437533915324.1.1.1741784726.0.0.0',
    '_ga_70ZZHDSCR6': 'GS1.1.1741784642.1.1.1741784726.59.0.0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'authorization': '',
    'baggage': 'sentry-environment=production,sentry-public_key=64d42d1ec99f4044ff0df570a905dbca,sentry-trace_id=81669d007ff7436a9edbdb9bdc6bbc7a,sentry-sample_rate=0.1,sentry-transaction=%2Fflats%2F*,sentry-sampled=false',
    'priority': 'u=1, i',
    'referer': 'https://www.mr-group.ru/flats/page-2/',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '81669d007ff7436a9edbdb9bdc6bbc7a-aa21efe4773b036a-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    # 'cookie': 'spid=1741784632987_62d30c366d1e5b195ad803dff541d343_rmtsfh281m20htua; _ym_uid=1741784635438762062; _ym_d=1741784635; _ym_isad=2; _ym_visorc=b; tmr_lvid=1c335b6614b3f392afef8213cbdc301d; tmr_lvidTS=1741784635189; _cmg_csstvfLiQ=1741784636; _comagic_idvfLiQ=9972780428.14161949863.1741784636; domain_sid=OIbdJw_MXh1IehKOV3pwu%3A1741784636224; USE_COOKIE_CONSENT_STATE={%22session%22:true%2C%22persistent%22:true%2C%22necessary%22:true%2C%22preferences%22:true%2C%22statistics%22:true%2C%22marketing%22:true%2C%22firstParty%22:true%2C%22thirdParty%22:true}; tmr_detect=0%7C1741784637480; PHPSESSID=mfaplogjpoo3c4l2rpo18rnhgd; PHPSESSID=go27flrpeer096u36lnh1nr0cd; spsc=1741784634908_1f432569f1c66728e15ccaae8f849953_e6cfb3ea8f0a0fa28cc6ebefdcae8ea5; _ga=GA1.1.835945232.1741784643; sessionId=17417846437533915324; adrdel=1741784645914; adrdel=1741784645914; adrcid=Ad53EZahiTy4QvZYZHYhh0Q; adrcid=Ad53EZahiTy4QvZYZHYhh0Q; acs_3=%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1741871045923%2C%22sl%22%3A%7B%22224%22%3A1741784645923%2C%221228%22%3A1741784645923%7D%7D; acs_3=%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1741871045923%2C%22sl%22%3A%7B%22224%22%3A1741784645923%2C%221228%22%3A1741784645923%7D%7D; mindboxDeviceUUID=b8b42419-45ee-4a92-8e84-640b5c64455a; directCrm-session=%7B%22deviceGuid%22%3A%22b8b42419-45ee-4a92-8e84-640b5c64455a%22%7D; scbsid_old=2746015342; uxs_uid=7adaf8b0-ff42-11ef-978b-e730cc09ad57; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _ga_H5S7YBLWM3=GS1.1.17417846437533915324.1.1.1741784726.0.0.0; _ga_70ZZHDSCR6=GS1.1.1741784642.1.1.1741784726.59.0.0',
}

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

        date = datetime.date.today()
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
        korpus = extract_digits_or_original(i["building"]["name"])
        konstruktiv = ''
        klass = ''
        srok_sdachi = ''
        srok_sdachi_old = ''
        stadia = ''
        dogovor = ''
        type = ''
        finish_type = i["decoration"]["name"]
        room_count = int(i["rooms_number"])
        area = i["area"]
        price_per_metr = ''
        old_price = ""
        discount = ''
        price_per_metr_new = ''
        price = i["price"]
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

current_date = datetime.date.today()

# Базовый путь для сохранения
base_path = r"C:\Users\m.olshanskiy\PycharmProjects\ndv_parsing\MR"

folder_path = os.path.join(base_path, str(current_date))
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

filename = f"{developer}_{current_date}.xlsx"

# Полный путь к файлу
file_path = os.path.join(folder_path, filename)

# Сохранение файла в папку
df.to_excel(file_path, index=False)

