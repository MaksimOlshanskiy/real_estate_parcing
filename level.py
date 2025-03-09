import requests
import datetime
import pandas as pd

cookies = {
    '_ga': 'GA1.1.81685078.1740772220',
    '_ym_uid': '174077221886345818',
    '_ym_d': '1740772218',
    'tmr_lvid': 'e874f0282635ffe8b7de137ac316a4e5',
    'tmr_lvidTS': '1740772223074',
    'scbsid_old': '2725937795',
    'mindboxDeviceUUID': 'd6b3597d-4b0b-4e45-8167-0b84971b36f7',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22d6b3597d-4b0b-4e45-8167-0b84971b36f7%22%7D',
    'SCBnotShow': '-1',
    'carrotquest_device_guid': '6d997f60-d4c2-46ce-9bba-006dad4bd9b9',
    'carrotquest_uid': '1918174530640020099',
    'carrotquest_auth_token': 'user.1918174530640020099.50549-b9906febe2aaab4d349cf1594e.47d47efe00cd8f58c8ea97db391e8a51693ff8a5be8b3761',
    'smFpId_old_values': '%5B%228ffe7a1c09dffb649545b8fc0287fbcd%22%5D',
    '_gcl_au': '1.1.1501037821.1740772225',
    'booking-blocking': 'false',
    'qrator_msid2': 'v2.0.1741015824.193.b28cc3716TKA4uco|ofYsAkrbPsZyZzp2|N+YLPypTH9/EqI1qdDZfr+WQleFfNxqviOsTjN4aIjP6M+iwSU+WQlpBR8d5oy27oV1nYaRNSt+7CM+HzvYjz0xQv4XM5UTwKnx0pdNvmUY=-K8yomI0H22JxGkk5a7cUn8Skz70=',
    'growthbook-attr-id': '4d60a9ac-867e-4032-b053-8e1ee8226f35',
    'ya_visit_init': '1741015826783',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    'carrotquest_realtime_services_transport': 'wss',
    'carrotquest_jwt_access': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdHQiOiJhY2Nlc3MiLCJleHAiOjE3NDEwMTk0MjksImlhdCI6MTc0MTAxNTgyOSwianRpIjoiZmFiM2M4M2RmYjk3NDVmOWI1YzY1M2U4YzVlZDNmNzciLCJhY3QiOiJ3ZWJfdXNlciIsImN0cyI6MTc0MTAxNTgyOSwicm9sZXMiOlsidXNlci4kYXBwX2lkOjUwNTQ5LiR1c2VyX2lkOjE5MTgxNzQ1MzA2NDAwMjAwOTkiXSwiYXBwX2lkIjo1MDU0OSwidXNlcl9pZCI6MTkxODE3NDUzMDY0MDAyMDA5OX0.jYt042unDNn5tV5gUh4ofE6_8Aj0FtQct4369UpJcfk',
    'domain_sid': 'qcIqS9U98g7tz8h1VzS3y%3A1741015829861',
    '_cmg_csstvg3wT': '1741015830',
    '_comagic_idvg3wT': '10327832739.14431146019.1741015830',
    'sma_session_id': '2210607035',
    'SCBfrom': '',
    'SCBporogAct': '5000',
    'SCBstart': '1741015831800',
    'menu': '%7B%22isFavorite%22%3Afalse%7D',
    'activity': '0|-1',
    'csrftoken': '2KNFKTsRWY0OACcnmMuvayjbGWEUGQpB',
    'ya_visit_total': '5',
    'ya_visit_total_session': '5',
    'ya_visit_page': '%2Ffilter%2Fkvartiry-v-level-lesnoy%2F',
    'pageCount': '4',
    'carrotquest_session': '1szjq1ndm9xionwecm9obhu969c75q8y',
    'carrotquest_session_started': '1',
    'tmr_detect': '0%7C1741015963528',
    'ya_visit_finished': 'done',
    '_ga_M5QHFCMEFC': 'GS1.1.1741015826.2.1.1741016230.49.0.0',
    'sma_index_activity': '5656',
    'SCBindexAct': '4202',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'baggage': 'sentry-environment=production,sentry-public_key=d431fc4e116909199fba6f7f1ecd0f0a,sentry-trace_id=7e41b1a53c764b4284999cc5fbeaf5d1',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'qrator-timestamp': '2025-03-03T15:37:13.541Z',
    'qrator-token': '3a9eef27c3d13731dd8e934c57dbb8dc',
    'qrator-version': '1.0',
    'referer': 'https://level.ru/filter/kvartiry-v-level-lesnoy/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '7e41b1a53c764b4284999cc5fbeaf5d1-abf3b4550f1ae622',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'x-csrftoken': '2KNFKTsRWY0OACcnmMuvayjbGWEUGQpB',
    'x-forwarded-host': '',
    # 'cookie': '_ga=GA1.1.81685078.1740772220; _ym_uid=174077221886345818; _ym_d=1740772218; tmr_lvid=e874f0282635ffe8b7de137ac316a4e5; tmr_lvidTS=1740772223074; scbsid_old=2725937795; mindboxDeviceUUID=d6b3597d-4b0b-4e45-8167-0b84971b36f7; directCrm-session=%7B%22deviceGuid%22%3A%22d6b3597d-4b0b-4e45-8167-0b84971b36f7%22%7D; SCBnotShow=-1; carrotquest_device_guid=6d997f60-d4c2-46ce-9bba-006dad4bd9b9; carrotquest_uid=1918174530640020099; carrotquest_auth_token=user.1918174530640020099.50549-b9906febe2aaab4d349cf1594e.47d47efe00cd8f58c8ea97db391e8a51693ff8a5be8b3761; smFpId_old_values=%5B%228ffe7a1c09dffb649545b8fc0287fbcd%22%5D; _gcl_au=1.1.1501037821.1740772225; booking-blocking=false; qrator_msid2=v2.0.1741015824.193.b28cc3716TKA4uco|ofYsAkrbPsZyZzp2|N+YLPypTH9/EqI1qdDZfr+WQleFfNxqviOsTjN4aIjP6M+iwSU+WQlpBR8d5oy27oV1nYaRNSt+7CM+HzvYjz0xQv4XM5UTwKnx0pdNvmUY=-K8yomI0H22JxGkk5a7cUn8Skz70=; growthbook-attr-id=4d60a9ac-867e-4032-b053-8e1ee8226f35; ya_visit_init=1741015826783; _ym_isad=2; _ym_visorc=w; carrotquest_realtime_services_transport=wss; carrotquest_jwt_access=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdHQiOiJhY2Nlc3MiLCJleHAiOjE3NDEwMTk0MjksImlhdCI6MTc0MTAxNTgyOSwianRpIjoiZmFiM2M4M2RmYjk3NDVmOWI1YzY1M2U4YzVlZDNmNzciLCJhY3QiOiJ3ZWJfdXNlciIsImN0cyI6MTc0MTAxNTgyOSwicm9sZXMiOlsidXNlci4kYXBwX2lkOjUwNTQ5LiR1c2VyX2lkOjE5MTgxNzQ1MzA2NDAwMjAwOTkiXSwiYXBwX2lkIjo1MDU0OSwidXNlcl9pZCI6MTkxODE3NDUzMDY0MDAyMDA5OX0.jYt042unDNn5tV5gUh4ofE6_8Aj0FtQct4369UpJcfk; domain_sid=qcIqS9U98g7tz8h1VzS3y%3A1741015829861; _cmg_csstvg3wT=1741015830; _comagic_idvg3wT=10327832739.14431146019.1741015830; sma_session_id=2210607035; SCBfrom=; SCBporogAct=5000; SCBstart=1741015831800; menu=%7B%22isFavorite%22%3Afalse%7D; activity=0|-1; csrftoken=2KNFKTsRWY0OACcnmMuvayjbGWEUGQpB; ya_visit_total=5; ya_visit_total_session=5; ya_visit_page=%2Ffilter%2Fkvartiry-v-level-lesnoy%2F; pageCount=4; carrotquest_session=1szjq1ndm9xionwecm9obhu969c75q8y; carrotquest_session_started=1; tmr_detect=0%7C1741015963528; ya_visit_finished=done; _ga_M5QHFCMEFC=GS1.1.1741015826.2.1.1741016230.49.0.0; sma_index_activity=5656; SCBindexAct=4202',
}

params = {
    'project': 'les',
    'limit': '100',
    'offset': '0',
}

response = requests.get('https://level.ru/api/filter/', params=params, cookies=cookies, headers=headers)

items = response.json()["results"]
flats = []

for i in items:

    project = i["project"]
    room_id = i["url"]
    ipoteka = "Семейная"
    date = datetime.date.today()
    room_temp = int(i["room"])
    if room_temp == 0 or room_temp == -1:
        room_type = "Студия"
    if room_temp == 1:
        room_type = "1 комната"
    if room_temp in [2, 3, 4]:
        room_type = f"{room_temp} комнаты"
    if room_temp >= 5:
        room_type = f"{room_temp} комнат"
    area = i["area"]
    price = i["price"]
    old_price = i["old_price"]
    korpus = i["building_name"]
    floor = i["floor"]
    print(
        f"{project}, {room_id}, ипотека: {ipoteka}, дата: {date}, тип: {room_type}, площадь: {area}, цена: {price}, старая цена: {old_price}, корпус: {korpus}, этаж: {floor}")
    result = [project, room_id, ipoteka, date, room_type, area, price, old_price, korpus, floor]
    flats.append(result)

# df = pd.DataFrame(flats, columns=["Проект", "id", "Ипотека", "Дата", "Тип", "Площадь", "Актуальная цена", "Старая цена",
#                                   "Корпус", "Этаж"])
# df.insert(0, 'Row Number', range(1, len(df) + 1))
#
# df.to_excel("level.xlsx", index=False)
