# текущий код выгружает все квартиры из всех ЖК одним запросом

import requests
import datetime
import time
import pandas as pd
import openpyxl

import requests

cookies = {
    'csrftoken': 'F6736b2F0ee6418B21Bcc2a1Ac10994D737b0E8603ab1b14823CAd9419b1abcD',
    '_ym_uid': '1740747075782024645',
    '_ym_d': '1740747075',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    '_gid': 'GA1.2.609567509.1740747075',
    'OAuth': '1285184712',
    'wr_visit_id': '1285184712',
    'mars': 'c1ddb9cc9f334452b4d517a7e0f6cac0',
    'cted': 'modId%3Dfc97be79%3Bclient_id%3D1886368892.1740747075%3Bya_client_id%3D1740747075782024645',
    '_ct_ids': 'fc97be79%3A17380%3A4788226779',
    '_ct_session_id': '4788226779',
    '_ct_site_id': '17380',
    '_ct': '3100000002816466805',
    '_ct_client_global_id': 'fbe0ef66-3f93-5e30-a689-c3153a19a53a',
    'dbl': 'd197cb120dd94e8ca200aaf218c2cb2a',
    '_ga': 'GA1.1.1886368892.1740747075',
    'call_s': '___fc97be79.1740748969.4788226779.168735:1060766|2___',
    '_ga_FR9TMQETHP': 'GS1.1.1740747075.1.1.1740747285.0.0.0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'access-control-allow-origin': '*',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://granelle.ru/flats/?project=zhivopisnyj&is_released=0&view=grid',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'x-csrftoken': 'F6736b2F0ee6418B21Bcc2a1Ac10994D737b0E8603ab1b14823CAd9419b1abcD',
    # 'cookie': 'csrftoken=F6736b2F0ee6418B21Bcc2a1Ac10994D737b0E8603ab1b14823CAd9419b1abcD; _ym_uid=1740747075782024645; _ym_d=1740747075; _ym_isad=2; _ym_visorc=w; _gid=GA1.2.609567509.1740747075; OAuth=1285184712; wr_visit_id=1285184712; mars=c1ddb9cc9f334452b4d517a7e0f6cac0; cted=modId%3Dfc97be79%3Bclient_id%3D1886368892.1740747075%3Bya_client_id%3D1740747075782024645; _ct_ids=fc97be79%3A17380%3A4788226779; _ct_session_id=4788226779; _ct_site_id=17380; _ct=3100000002816466805; _ct_client_global_id=fbe0ef66-3f93-5e30-a689-c3153a19a53a; dbl=d197cb120dd94e8ca200aaf218c2cb2a; _ga=GA1.1.1886368892.1740747075; call_s=___fc97be79.1740748969.4788226779.168735:1060766|2___; _ga_FR9TMQETHP=GS1.1.1740747075.1.1.1740747285.0.0.0',
}

params = {
    'area_max': '',
    'area_min': '',
    'city': '',
    'floor_number_max': '',
    'floor_number_min': '',
    'is_apartments': '',
    'is_black_friday': '',
    'is_business': '',
    'is_coming': '',
    'is_cyber_monday': '',
    'is_profit': '',
    'is_property_of_the_day': '',
    'is_released': '0',
    'is_with_keys': '',
    'limit': '3000',  # максимальное количество на выдаче
    'offset': '0',  # размер сдвига
    'order': '',
    'price_max': '',
    'price_min': '',
    'search': '',
    'withLayouts': 'false',
}

flats = []
counter = 1
offset = 0


url = 'https://granelle.ru/api/flats/'
response = requests.get(url, params=params, cookies=cookies, headers=headers)

items = response.json()["results"]

for i in items:
    project = i["project"]
    room_id = i["id"]
    ipoteka = ""
    date = datetime.date.today()
    room_temp = int(i["rooms"])
    if room_temp == 0 or room_temp == -1:
        room_type = "Студия"
    if room_temp == 1:
        room_type = "1 комната"
    if room_temp in [2, 3, 4]:
        room_type = f"{room_temp} комнаты"
    if room_temp >= 5:
        room_type = f"{room_temp} комнат"
    area = i["area"]
    price = i["price_discounted"]
    old_price = i["price"]
    korpus = i["building"]
    floor = i["floor"]
    print(
        f"{project}, {room_id}, ипотека: {ipoteka}, дата: {date}, тип: {room_type}, площадь: {area}, цена: {price}, старая цена: {old_price}, корпус: {korpus}, этаж: {floor}")
    result = [project, room_id, ipoteka, date, room_type, area, price, old_price, korpus, floor]
    flats.append(result)


df = pd.DataFrame(flats, columns=["Проект", "id", "Ипотека", "Дата", "Тип", "Площадь", "Актуальная цена", "Старая цена",
                                  "Корпус", "Этаж"])
df.insert(0, '№', range(1, len(df) + 1))
print(df)

df.to_excel("granel.xlsx", index=False)
