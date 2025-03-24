import requests
import datetime
import time
import pandas as pd
import openpyxl
import os
import random


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://dogma-evo.ru',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://dogma-evo.ru/',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
}

json_data = {
    'areas': [
        27.82,
        100.82,
    ],
    'costs': [
        7740455,
        22506984,
    ],
    'deadlines': [],
    'floors': [
        2,
        25,
    ],
    'layout_id': [],
    'letter_ids': [],
    'limit': 100,
    'offset': 0,
    'ids': [],
    'project_ids': [
        5,
    ],
    'rooms': [],
    'statuses': [
        2,
    ],
    'tags': [],
    'types': [
        1,
    ],
    'group_by': '',
    'order': {
        'field': 'cost',
        'type': 'asc',
    },
}


flats = []


def extract_digits_or_original(s):
    digits = ''.join([char for char in s if char.isdigit()])
    return int(digits) if digits else s


while True:

    response = requests.post('https://service.1dogma.ru/api/layouts-filter/v2/objects/filter', headers=headers, json=json_data)

    print(response.status_code)

    items = response.json()["objects"]

    if not items:
        print("Всё скачано. Переходим к загрузке в файл")
        break

    for i in items:

        url = ""

        date = datetime.date.today()
        project = i["project_name"]
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
        developer = "Догма"
        okrug = ''
        district = ''
        adress = i['address']
        eskrou = ''
        korpus = i["letter_name"]
        konstruktiv = ''
        klass = ''
        srok_sdachi = ''
        srok_sdachi_old = ''
        stadia = ''
        dogovor = ''
        if i['type'] == 'flat':
            type = 'Квартира'
        else:
            type = i['type']
        try:
            finish_type = i['tags'][0]['text']
        except:
            finish_type = "Без отделки"

        room_count = int(i["room"])
        area = i["area"]
        price_per_metr = ''

        discount = ''
        price_per_metr_new = ''


        if i["cost_sale"] == 0:
            price = i['cost']
            old_price = ''
        else:
            old_price = i['cost']
            price = i['cost_sale']


        section = ''
        floor = int(i["floor"])
        flat_number = i["flat_number"]

        print(
            f"{project}, {url}, дата: {date}, комнаты: {room_count}, площадь: {area}, цена: {price}, старая цена: {old_price}, корпус: {korpus}, этаж: {floor}")
        result = [date, project, english, promzona, mestopolozhenie, subway, distance_to_subway, time_to_subway, mck,
                  distance_to_mck, time_to_mck, distance_to_bkl,
                  time_to_bkl, bkl, status, start, comment, developer, okrug, district, adress, eskrou, korpus,
                  konstruktiv, klass, srok_sdachi, srok_sdachi_old,
                  stadia, dogovor, type, finish_type, room_count, area, price_per_metr, old_price, discount,
                  price_per_metr_new, price, section, floor, flat_number]
        flats.append(result)
    json_data["offset"] = int(json_data["offset"]) + 100
    sleep_time = random.uniform(10, 15)
    time.sleep(sleep_time)


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
base_path = r"C:\PycharmProjects\SeleniumParcer"

folder_path = os.path.join(base_path, str(current_date))
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

filename = f"{developer}_{current_date}.xlsx"

# Полный путь к файлу
file_path = os.path.join(folder_path, filename)

# Сохранение файла в папку
df.to_excel(file_path, index=False)
