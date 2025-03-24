import requests
import datetime
import time
import pandas as pd
import openpyxl
import os
import random

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJzaXRlX3dpZGdldCIsImp0aSI6IjY4OGRmNjZlNTRjM2ExMDdmNDg5NTdlYzBlY2M2N2MwYWE5MzczZjFjMDkzZTlhZGVhNDIxZmViNWFmMTg1MjZiZTkwNTk1MWFlNjAzZTQ2IiwiaWF0IjoxNzQyNDUyMzc1LjA0NDg3OCwibmJmIjoxNzQyNDUyMzc1LjA0NDg4LCJleHAiOjE3NDI0NTU5NzUuMDM4NzE2LCJzdWIiOiJTSVRFX1dJREdFVHwyNzcxIiwic2NvcGVzIjpbIlNJVEVfV0lER0VUIl0sInR5cGUiOiJzaXRlV2lkZ2V0IiwiZW50aXRsZW1lbnRzIjoiIiwiYWNjb3VudCI6eyJpZCI6NTI5MCwidGl0bGUiOiLQkNCcINCU0LXQstC10LvQvtC_0LzQtdC90YIiLCJzdWJkb21haW4iOiJwYjUyOTAiLCJiaWxsaW5nT3duZXJJZCI6NTI5OCwiY291bnRyeUNvZGUiOiJSVSJ9LCJyb2xlcyI6WyJST0xFX1NJVEVfV0lER0VUIl0sInNpdGVXaWRnZXQiOnsiaWQiOjI3NzEsImRvbWFpbiI6Imh0dHBzOi8veG4tLS0tY3RiZmZxcnV4ajdiM2MueG4tLXAxYWkifX0.XQZKXIxv5Vshm4OG3EUCuMcnLTiyOeuXrauJYk9ZJ0ddAGUlsUwQyZ2wwIZcYR4_m_XTWt2mwxLVWbRgQKcX0hFlcwLbJjAwcqPi1EosZqzsmXybVPe2qmgVBLGY5pEJil2OPg237qjV4c_BR-OEpxWQ3pDsj0Au9vi2VHZOGV89j4IDavvyHZ0uRN_yYwaN6jao6BkzbRN5Qa8P662ucUqY_pe-nt7AaaoUedJKjLCeoZXxllRnuP-RLDhelS1xVQmhSnEdUqricYnUWUt08gmIPU8ylPLwmjicmAXo0kziO-Pm1ljiUU0a4QtfOr-Xfto8qHSOiQC0XenDvmQVmw',
    'cache-control': 'no-cache',
    'origin': 'https://smart-catalog.profitbase.ru',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://smart-catalog.profitbase.ru/',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
}

params = {
    'isHouseFinished': '0',
    'status[0]': 'AVAILABLE',
    'houseId': '97607',
    'limit': '100',
    'full': 'true',
    'returnFilteredCount': 'true',
}

flats = []


def extract_digits_or_original(s):
    digits = ''.join([char for char in s if char.isdigit()])
    return int(digits) if digits else s




response = requests.get('https://pb5290.profitbase.ru/api/v4/json/property', params=params, headers=headers)

items = response.json()['data']['properties']

for i in items:

    url = ""

    date = datetime.date.today()
    project = i["projectName"]
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
    developer = "АМ Девелопмент"
    okrug = ''
    district = ''
    adress = i['address']
    eskrou = ''
    korpus = i["houseName"]
    konstruktiv = ''
    klass = ''
    srok_sdachi = ''
    srok_sdachi_old = ''
    stadia = ''
    dogovor = ''
    type = 'Квартира'
    finish_type = i['custom_fields'][18]['value']
    room_count = int(i["rooms_amount"])
    area = i['area']['area_total']
    price_per_metr = ''

    discount = ''
    price_per_metr_new = ''
    price = i['price']['value']
    old_price = ''

    section = int(i['sectionNumber'])
    floor = int(i["floor"])
    flat_number = ''

    print(
        f"{project}, {url}, дата: {date}, комнаты: {room_count}, площадь: {area}, цена: {price}, старая цена: {old_price}, корпус: {korpus}, этаж: {floor}")
    result = [date, project, english, promzona, mestopolozhenie, subway, distance_to_subway, time_to_subway, mck,
              distance_to_mck, time_to_mck, distance_to_bkl,
              time_to_bkl, bkl, status, start, comment, developer, okrug, district, adress, eskrou, korpus,
              konstruktiv, klass, srok_sdachi, srok_sdachi_old,
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
base_path = r"C:\PycharmProjects\SeleniumParcer"

folder_path = os.path.join(base_path, str(current_date))
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

filename = f"{developer}_{current_date}.xlsx"

# Полный путь к файлу
file_path = os.path.join(folder_path, filename)

# Сохранение файла в папку
df.to_excel(file_path, index=False)
