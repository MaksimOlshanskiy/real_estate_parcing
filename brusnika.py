import requests
import datetime
import pandas as pd

cookies = {
    'mindboxDeviceUUID': 'd6b3597d-4b0b-4e45-8167-0b84971b36f7',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22d6b3597d-4b0b-4e45-8167-0b84971b36f7%22%7D',
    '_ym_uid': '1740772038458445073',
    '_ym_d': '1740772038',
    'carrotquest_device_guid': '602783f0-a1e1-4e8d-8bf4-51db4ae457ee',
    'carrotquest_uid': '1918172978202280724',
    'carrotquest_auth_token': 'user.1918172978202280724.51753-776395ac10b7ee9e1ccd2b8213.27fd7614f967e3a3e47ed64b56d86cafdad5baf1146258ec',
    '_gcl_au': '1.1.783360396.1740772039',
    'tmr_lvid': '872f20426e5033497a2ef8b7287d0f8f',
    'tmr_lvidTS': '1740772039049',
    'adrdel': '1740772039172',
    'adrdel': '1740772039172',
    'adrcid': 'A0r9KB4fc8duMUv2jPsp-tg',
    'adrcid': 'A0r9KB4fc8duMUv2jPsp-tg',
    'acs_3': '%7B%22hash%22%3A%222519d36ba1d6b3a4bd08e045fbf175fd06f869ed%22%2C%22nextSyncTime%22%3A1740858439184%2C%22syncLog%22%3A%7B%22224%22%3A1740772039184%2C%221228%22%3A1740772039184%7D%7D',
    'acs_3': '%7B%22hash%22%3A%222519d36ba1d6b3a4bd08e045fbf175fd06f869ed%22%2C%22nextSyncTime%22%3A1740858439184%2C%22syncLog%22%3A%7B%22224%22%3A1740772039184%2C%221228%22%3A1740772039184%7D%7D',
    '_cmg_csstGarz8': '1740772039',
    '_comagic_idGarz8': '10310214679.14411219924.1740772038',
    'domain_sid': 'XX3Zh8jAiJLM3fD2UxTUM%3A1740772040160',
    'csrftoken': 'AKb9zL4bJ8G57OCxKJ92gY6c90iJEdFB',
    '_sp_id.bc95': 'dc17f6a5-570a-4eeb-9143-098a76e41c8b.1740772039.1.1740772043..a3e0c881-6d8d-4c8c-a084-9e790ad23338..866d07bc-f22e-45ed-b29a-e87b40f7d3b8.1740772039082.2',
    'sessionid': '6wxcg0o0ijb0kmw10ra4yzj27tj3dj2e',
    '_ym_visorc': 'b',
    '_ym_isad': '2',
    'carrotquest_session': 'fw4zmb3bwttk7fq7tb16b1o7a0o1xk6u',
    'carrotquest_session_started': '1',
    'carrotquest_realtime_services_transport': 'wss',
    'carrotquest_jwt_access': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdHQiOiJhY2Nlc3MiLCJleHAiOjE3NDEwMTM3ODQsImlhdCI6MTc0MTAxMDE4NCwianRpIjoiYzAyZjA2Yzc4OThhNDRmZjljOTNhNjAwZTVlNmRkNGQiLCJhY3QiOiJ3ZWJfdXNlciIsImN0cyI6MTc0MTAxMDE4NCwicm9sZXMiOlsidXNlci4kYXBwX2lkOjUxNzUzLiR1c2VyX2lkOjE5MTgxNzI5NzgyMDIyODA3MjQiXSwiYXBwX2lkIjo1MTc1MywidXNlcl9pZCI6MTkxODE3Mjk3ODIwMjI4MDcyNH0.gclWwSmVpUyDAtS5YXmmfZt8ThihJ4_TwOpCd8SnY8M',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://moskva.brusnika.ru/flat/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'mindboxDeviceUUID=d6b3597d-4b0b-4e45-8167-0b84971b36f7; directCrm-session=%7B%22deviceGuid%22%3A%22d6b3597d-4b0b-4e45-8167-0b84971b36f7%22%7D; _ym_uid=1740772038458445073; _ym_d=1740772038; carrotquest_device_guid=602783f0-a1e1-4e8d-8bf4-51db4ae457ee; carrotquest_uid=1918172978202280724; carrotquest_auth_token=user.1918172978202280724.51753-776395ac10b7ee9e1ccd2b8213.27fd7614f967e3a3e47ed64b56d86cafdad5baf1146258ec; _gcl_au=1.1.783360396.1740772039; tmr_lvid=872f20426e5033497a2ef8b7287d0f8f; tmr_lvidTS=1740772039049; adrdel=1740772039172; adrdel=1740772039172; adrcid=A0r9KB4fc8duMUv2jPsp-tg; adrcid=A0r9KB4fc8duMUv2jPsp-tg; acs_3=%7B%22hash%22%3A%222519d36ba1d6b3a4bd08e045fbf175fd06f869ed%22%2C%22nextSyncTime%22%3A1740858439184%2C%22syncLog%22%3A%7B%22224%22%3A1740772039184%2C%221228%22%3A1740772039184%7D%7D; acs_3=%7B%22hash%22%3A%222519d36ba1d6b3a4bd08e045fbf175fd06f869ed%22%2C%22nextSyncTime%22%3A1740858439184%2C%22syncLog%22%3A%7B%22224%22%3A1740772039184%2C%221228%22%3A1740772039184%7D%7D; _cmg_csstGarz8=1740772039; _comagic_idGarz8=10310214679.14411219924.1740772038; domain_sid=XX3Zh8jAiJLM3fD2UxTUM%3A1740772040160; csrftoken=AKb9zL4bJ8G57OCxKJ92gY6c90iJEdFB; _sp_id.bc95=dc17f6a5-570a-4eeb-9143-098a76e41c8b.1740772039.1.1740772043..a3e0c881-6d8d-4c8c-a084-9e790ad23338..866d07bc-f22e-45ed-b29a-e87b40f7d3b8.1740772039082.2; sessionid=6wxcg0o0ijb0kmw10ra4yzj27tj3dj2e; _ym_visorc=b; _ym_isad=2; carrotquest_session=fw4zmb3bwttk7fq7tb16b1o7a0o1xk6u; carrotquest_session_started=1; carrotquest_realtime_services_transport=wss; carrotquest_jwt_access=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdHQiOiJhY2Nlc3MiLCJleHAiOjE3NDEwMTM3ODQsImlhdCI6MTc0MTAxMDE4NCwianRpIjoiYzAyZjA2Yzc4OThhNDRmZjljOTNhNjAwZTVlNmRkNGQiLCJhY3QiOiJ3ZWJfdXNlciIsImN0cyI6MTc0MTAxMDE4NCwicm9sZXMiOlsidXNlci4kYXBwX2lkOjUxNzUzLiR1c2VyX2lkOjE5MTgxNzI5NzgyMDIyODA3MjQiXSwiYXBwX2lkIjo1MTc1MywidXNlcl9pZCI6MTkxODE3Mjk3ODIwMjI4MDcyNH0.gclWwSmVpUyDAtS5YXmmfZt8ThihJ4_TwOpCd8SnY8M',
}

params = {
    'offset': '0',
    'ordering': 'price_order',
    'limit': '1722',  # можно установить лимит, чтобы выгрузить всё
    'active_banner': 'true',
    'active_big_card': 'true',
    'is_group': '0',
}

response = requests.get('https://moskva.brusnika.ru/api/filter/flats/', params=params, cookies=cookies, headers=headers)

items = response.json()["results"]
flats = []

for i in items:
    if 'id' in i:  # Убираем рекламную строку, т.к. в квартирах нет ключа id
        continue
    project = i["complex_name"]
    room_id = i["page_url"]
    ipoteka = "Семейная"
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
    area = i["square"]
    price = i["price"]
    old_price = i["price_package_without_promo"]
    korpus = i["building_name"]
    floor = i["building_floors_count"]
    print(
        f"{project}, {room_id}, ипотека: {ipoteka}, дата: {date}, тип: {room_type}, площадь: {area}, цена: {price}, старая цена: {old_price}, корпус: {korpus}, этаж: {floor}")
    result = [project, room_id, ipoteka, date, room_type, area, price, old_price, korpus, floor]
    flats.append(result)

df = pd.DataFrame(flats, columns=["Проект", "id", "Ипотека", "Дата", "Тип", "Площадь", "Актуальная цена", "Старая цена",
                                  "Корпус", "Этаж"])
df.insert(0, 'Row Number', range(1, len(df) + 1))

df.to_excel("brusnika.xlsx", index=False)
