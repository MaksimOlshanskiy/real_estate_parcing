import requests
import datetime
import time
import pandas as pd
import openpyxl
import os
import random


cookies = {
    '_ct': '2300000000269276706',
    '_ym_uid': '1741084848243041491',
    '_ym_d': '1741084848',
    '_ct_client_global_id': 'fbe0ef66-3f93-5e30-a689-c3153a19a53a',
    'BX_USER_ID': '0637000992907e90803d486cd4459565',
    '_ga': 'GA1.1.2050671085.1741084871',
    '_ym_isad': '2',
    'PHPSESSID': 'XXOHkpiXTUmS1mlGL6MHyRr7CmdV7zg6',
    'cted': 'modId%3Drwlsx7v3%3Bclient_id%3D2050671085.1741084871%3Bya_client_id%3D1741084848243041491',
    '_ym_visorc': 'w',
    '_ct_ids': 'rwlsx7v3%3A57297%3A421445259',
    '_ct_session_id': '421445259',
    '_ct_site_id': '57297',
    'call_s': '___rwlsx7v3.1742281464.421445259.302835:873280.302836:873422|2___',
    '_ga_C9SQLMNF29': 'GS1.1.1742279670.3.0.1742279682.0.0.0',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Pragma': 'no-cache',
    'Referer': 'https://rusich.group/catalog/?view=grid',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': '_ct=2300000000269276706; _ym_uid=1741084848243041491; _ym_d=1741084848; _ct_client_global_id=fbe0ef66-3f93-5e30-a689-c3153a19a53a; BX_USER_ID=0637000992907e90803d486cd4459565; _ga=GA1.1.2050671085.1741084871; _ym_isad=2; PHPSESSID=XXOHkpiXTUmS1mlGL6MHyRr7CmdV7zg6; cted=modId%3Drwlsx7v3%3Bclient_id%3D2050671085.1741084871%3Bya_client_id%3D1741084848243041491; _ym_visorc=w; _ct_ids=rwlsx7v3%3A57297%3A421445259; _ct_session_id=421445259; _ct_site_id=57297; call_s=___rwlsx7v3.1742281464.421445259.302835:873280.302836:873422|2___; _ga_C9SQLMNF29=GS1.1.1742279670.3.0.1742279682.0.0.0',
}

params = {
    'action': 'getApartments',
    'max_price': '',
    'min_price': '',
    'min_square': '',
    'max_square': '',
    'min_floor': '',
    'max_floor': '',
    'discount': '',
    'master_bedroom': '',
    'balcony': '',
    'rooms': '',
    'finish': '',
    'deadline': '',
    'corpus': '',
    'project': '',
    'min_monthly_payment': '',
    'max_monthly_payment': '',
    'sort': '',
    'order': '',
    'view': 'grid',
    'page': '1',
    'limit': '500',
}



flats = []

def extract_digits_or_original(s):
    digits = ''.join([char for char in s if char.isdigit()])
    return int(digits) if digits else s

while True:

    response = requests.get('https://rusich.group/ajax/catalog-filter.php', params=params, cookies=cookies, headers=headers)

    items = response.json()["result"]["apartments"]

    for i in items:

        url = ""

        date = datetime.date.today()
        project = i["PROJECT"]
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
        developer = "Русич"
        okrug = ''
        district = ''
        adress = ''
        eskrou = ''
        korpus = extract_digits_or_original(i["CORPUS"])
        konstruktiv = ''
        klass = ''
        srok_sdachi = ''
        srok_sdachi_old = ''
        stadia = ''
        dogovor = ''
        type = ''

        finish_type = i['FINISH']['value']

        room_count = int(extract_digits_or_original(i["NUMBER_OF_ROOMS"]))
        area = i["SQUARE"]
        price_per_metr = ''

        discount = ''
        price_per_metr_new = ''
        price = i["PRICE"]
        old_price = ''

        section = i['SECTION']
        floor = i["FLOOR"]
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
base_path = r"C:\PycharmProjects\SeleniumParcer\MR"

folder_path = os.path.join(base_path, str(current_date))
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

filename = f"{developer}_{current_date}.xlsx"

# Полный путь к файлу
file_path = os.path.join(folder_path, filename)

# Сохранение файла в папку
df.to_excel(file_path, index=False)
