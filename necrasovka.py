import requests
import datetime
import time
import pandas as pd
import openpyxl
import os
import random

cookies = {
    'session': 'fed267c2539a6a06559ab8b3318bc3f37de6faba3f4021738b2727b9b880f280',
    'tmr_lvid': 'f3e5129d6835a04d13c30f1f9d49ba59',
    'tmr_lvidTS': '1742370906458',
    'scbsid_old': '2725937795',
    '_ym_uid': '1742370907816346159',
    '_ym_d': '1742370907',
    'roistat_visit': '127140',
    'roistat_first_visit': '127140',
    'roistat_visit_cookie_expire': '1209600',
    'roistat_is_need_listen_requests': '0',
    'roistat_is_save_data_in_cookie': '1',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    'domain_sid': '9WaR0EAbgifJmDKmvZatg%3A1742370907091',
    'roistat_marker': 'seo_google_',
    'roistat_marker_old': 'seo_google_',
    '___dc': 'e548c449-aa40-40ff-a6fa-451575933d13',
    '_cmg_csstIbdzG': '1742370908',
    '_comagic_idIbdzG': '10071065246.14251856856.1742370905',
    'tmr_detect': '0%7C1742370913556',
    'roistat_call_tracking': '1',
    'roistat_emailtracking_email': 'null',
    'roistat_emailtracking_tracking_email': 'null',
    'roistat_emailtracking_emails': '%5B%5D',
    'roistat_cookies_to_resave': 'roistat_ab%2Croistat_ab_submit%2Croistat_visit%2Croistat_marker%2Croistat_marker_old%2Croistat_call_tracking%2Croistat_emailtracking_email%2Croistat_emailtracking_tracking_email%2Croistat_emailtracking_emails',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://legendamarusino.ru/flats',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    'x-host': 'legendamarusino.ru',
    # 'cookie': 'session=fed267c2539a6a06559ab8b3318bc3f37de6faba3f4021738b2727b9b880f280; tmr_lvid=f3e5129d6835a04d13c30f1f9d49ba59; tmr_lvidTS=1742370906458; scbsid_old=2725937795; _ym_uid=1742370907816346159; _ym_d=1742370907; roistat_visit=127140; roistat_first_visit=127140; roistat_visit_cookie_expire=1209600; roistat_is_need_listen_requests=0; roistat_is_save_data_in_cookie=1; _ym_isad=2; _ym_visorc=w; domain_sid=9WaR0EAbgifJmDKmvZatg%3A1742370907091; roistat_marker=seo_google_; roistat_marker_old=seo_google_; ___dc=e548c449-aa40-40ff-a6fa-451575933d13; _cmg_csstIbdzG=1742370908; _comagic_idIbdzG=10071065246.14251856856.1742370905; tmr_detect=0%7C1742370913556; roistat_call_tracking=1; roistat_emailtracking_email=null; roistat_emailtracking_tracking_email=null; roistat_emailtracking_emails=%5B%5D; roistat_cookies_to_resave=roistat_ab%2Croistat_ab_submit%2Croistat_visit%2Croistat_marker%2Croistat_marker_old%2Croistat_call_tracking%2Croistat_emailtracking_email%2Croistat_emailtracking_tracking_email%2Croistat_emailtracking_emails',
}

params = {
    'project_id': 'a5f9b6b9-037d-4cd8-981c-cbd55e93a5c0',
    'status': 'free',
    'offset': '0',
    'limit': '16',
}

flats = []


def extract_digits_or_original(s):
    digits = ''.join([char for char in s if char.isdigit()])
    return int(digits) if digits else s


while True:

    response = requests.get(
        'https://legendamarusino.ru/api/realty-filter/residential/real-estates',
        params=params,
        cookies=cookies,
        headers=headers,
    )

    items = response.json()

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
        developer = "Некрасовка Девелопмент"
        okrug = ''
        district = ''
        adress = i['address']
        eskrou = ''
        korpus = extract_digits_or_original(i["building_number"])
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
            if i['finishing_type'] == 'no':
                finish_type = "Без отделки"
            elif i['finishing_type'] == 'yes':
                finish_type = "С отделкой"
        except:
            finish_type = ""

        room_count = int(i["rooms"])
        area = i["total_area"]
        price_per_metr = ''

        discount = ''
        price_per_metr_new = ''
        price = i["price"]
        try:
            old_price = i['old_price']
        except:
            old_price = ''

        section = int(i['section_number'])
        floor = int(i["floor_number"])
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
    params["offset"] = str(int(params["offset"]) + 16)
    sleep_time = random.uniform(2, 5)
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
base_path = r"C:\PycharmProjects\SeleniumParcer"

folder_path = os.path.join(base_path, str(current_date))
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

filename = f"{developer}_{current_date}.xlsx"

# Полный путь к файлу
file_path = os.path.join(folder_path, filename)

# Сохранение файла в папку
df.to_excel(file_path, index=False)
