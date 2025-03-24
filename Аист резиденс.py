import requests
import datetime
import time
import pandas as pd
import openpyxl
import os
import random

cookies = {
    'tmr_lvid': '373e3908e8e10a1a74802300f524551a',
    'tmr_lvidTS': '1742540992510',
    '_ym_uid': '1742540993355666364',
    '_ym_d': '1742540993',
    '_ct_ids': '8as82fa1%3A55785%3A423061774',
    '_ct_session_id': '423061774',
    '_ct_site_id': '55785',
    '_ct': '2300000000275016344',
    '_ym_visorc': 'w',
    '_ym_isad': '2',
    '_ct_client_global_id': 'fbe0ef66-3f93-5e30-a689-c3153a19a53a',
    '_ga': 'GA1.1.993239101.1742540994',
    'cted': 'modId%3D8as82fa1%3Bya_client_id%3D1742540993355666364%3Bclient_id%3D993239101.1742540994',
    'domain_sid': 'li-fmz5tGR_XX9OQJdwEc%3A1742540998177',
    'call_s': '___8as82fa1.1742542835.423061774.284095:854342|2___',
    '_ga_1ZPY9G3X05': 'GS1.1.1742540994.1.1.1742541038.0.0.0',
    'tmr_detect': '0%7C1742541039614',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://aist-residence.ru/apartamenty',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'tmr_lvid=373e3908e8e10a1a74802300f524551a; tmr_lvidTS=1742540992510; _ym_uid=1742540993355666364; _ym_d=1742540993; _ct_ids=8as82fa1%3A55785%3A423061774; _ct_session_id=423061774; _ct_site_id=55785; _ct=2300000000275016344; _ym_visorc=w; _ym_isad=2; _ct_client_global_id=fbe0ef66-3f93-5e30-a689-c3153a19a53a; _ga=GA1.1.993239101.1742540994; cted=modId%3D8as82fa1%3Bya_client_id%3D1742540993355666364%3Bclient_id%3D993239101.1742540994; domain_sid=li-fmz5tGR_XX9OQJdwEc%3A1742540998177; call_s=___8as82fa1.1742542835.423061774.284095:854342|2___; _ga_1ZPY9G3X05=GS1.1.1742540994.1.1.1742541038.0.0.0; tmr_detect=0%7C1742541039614',
}

flats = []


def extract_digits_or_original(s):
    digits = ''.join([char for char in s if char.isdigit()])
    return int(digits) if digits else s


response = requests.get(
    'https://aist-residence.ru/_next/data/bFwnArcDD0P9Vw5-FhcaF/apartamenty.json',
    cookies=cookies,
    headers=headers,
)
items = response.json()['pageProps']['data']['data']

for i in items:

    url = ""

    date = datetime.date.today()
    project = "Аист резиденс"
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
    developer = "Монарх"
    okrug = ''
    district = ''
    adress = ''
    eskrou = ''
    korpus = ''
    konstruktiv = ''
    klass = ''
    srok_sdachi = ''
    srok_sdachi_old = ''
    stadia = ''
    dogovor = ''
    type = 'Апартаменты'
    finish_type = ''
    if i['euro'] == True:
        room_count = f'E-{i["rooms"]}'
    else:
        room_count = int(i["rooms"])
    area = i["area"]
    price_per_metr = ''
    old_price = ''
    discount = ''
    price_per_metr_new = ''
    price = int(i["price"][:-3])
    section = i["section"]
    floor = i["floor"]
    flat_number = i['number']

    print(
        f"{project}, {url}, отделка: {finish_type}, тип: {room_count}, площадь: {area}, цена: {price}, старая цена: {old_price}, корпус: {korpus}, этаж: {floor}")
    result = [date, project, english, promzona, mestopolozhenie, subway, distance_to_subway, time_to_subway, mck,
              distance_to_mck, time_to_mck, distance_to_bkl,
              time_to_bkl, bkl, status, start, comment, developer, okrug, district, adress, eskrou, korpus, konstruktiv,
              klass, srok_sdachi, srok_sdachi_old,
              stadia, dogovor, type, finish_type, room_count, area, price_per_metr, old_price, discount,
              price_per_metr_new, price, section, floor, flat_number]
    flats.append(result)


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
base_path = r"C:\PycharmProjects\SeleniumParcer\Монарх"

folder_path = os.path.join(base_path, str(current_date))
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

filename = f"{developer}_{current_date}.xlsx"

# Полный путь к файлу
file_path = os.path.join(folder_path, filename)

# Сохранение файла в папку
df.to_excel(file_path, index=False)
