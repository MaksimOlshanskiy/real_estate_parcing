# требуется менять cookie, а именно 'qrator_jsid'. Запросы через сессию

# id всех проектов: [69011,69057,41,56,68189,44,69104,57,5,69054,20,7,68195,68192,68188,68191,69106,69108,68199,69206,2,45,40,69103,21,68196,31,69101,68194,3,69051,55,1,49,68185,69102,4,42,69100,69110]

import requests
import datetime
import time
import pandas as pd
import openpyxl

cookies = {
    '_smt': '5f304b3c-fcfa-4230-89da-07b20401d1a9',
    'mindboxDeviceUUID': 'd6b3597d-4b0b-4e45-8167-0b84971b36f7',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22d6b3597d-4b0b-4e45-8167-0b84971b36f7%22%7D',
    '_ymab_param': 'BYeHflO6XUN0s7S7mxCGcH0Zaw6E-ogsUI6oL6LCn20uw6mVuLxheUCUjqi6P1ZNzUoWCCLgIm88uVglZkilWjwhBCQ',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    '_ym_uid': '1740722171243961658',
    '_ym_d': '1740722171',
    '_ct': '1300000000511218043',
    '_ct_client_global_id': 'fbe0ef66-3f93-5e30-a689-c3153a19a53a',
    'suggested_city': '1',
    'sessionid': 'mt73xxzzmdnmhsgeqgy4zcn0cgn0b60h',
    'cookies_accepted': '1',
    '_ga': 'GA1.1.745973656.1740722186',
    'FPID': 'FPID2.2.R9K7jfSqpWPdJvRjcUB9I6d8uo%2F68Nn%2FouyBDgsE13w%3D.1740722186',
    'tmr_lvid': '67dc556b7be44bbeeb2284f35f17fd7b',
    'tmr_lvidTS': '1740722185746',
    'nxt-city': '%7B%22dep%22%3A%7B%22version%22%3A1%2C%22sc%22%3A0%7D%2C%22__v_isRef%22%3Atrue%2C%22__v_isShallow%22%3Afalse%2C%22_rawValue%22%3A%7B%22key%22%3A%22moscow%22%2C%22name%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%2C%22url_prefix%22%3A%22%22%2C%22contact_number%22%3A%22%2B7%20495%20292-31-31%22%7D%2C%22_value%22%3A%7B%22key%22%3A%22moscow%22%2C%22name%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%2C%22url_prefix%22%3A%22%22%2C%22contact_number%22%3A%22%2B7%20495%20292-31-31%22%7D%7D',
    'cted': 'modId%3Dhtlowve6%3Bclient_id%3D745973656.1740722186%3Bya_client_id%3D1740722171243961658',
    '_ct_site_id': '36409',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    '_ct_ids': 'htlowve6%3A36409%3A827790664',
    '_ct_session_id': '827790664',
    'FPLC': 'Ubq%2BLhjbs9AXv5nrvE6FgtCwfc2BwsSsuwoq%2BFgx2eHPTXVEupfQ5L2MOxATO4EcIP%2BYVe0wUvP4tguzue50BIvEy8lEDlILFu0cEdaDxF0NrkxFoNS7F4vw%2FaQXrw%3D%3D',
    'domain_sid': 'wKdbbuq6KB-jddLKpqmNw%3A1740939726800',
    'pageviewTimerAllFired1min': 'true',
    'pageviewTimerAllFired2min': 'true',
    'pageviewTimerAllFired5min': 'true',
    'pageviewTimerAllFired10min': 'true',
    'pageviewTimerAllFired15min': 'true',
    'pageviewTimerMSKFired1min': 'true',
    'pageviewTimerMSKFired2min': 'true',
    'pageviewTimerMSKFired5min': 'true',
    'pageviewTimerMSKFired10min': 'true',
    'pageviewTimerMSKFired15min': 'true',
    'qrator_jsid': '1741352368.131.9st4vI1hCtoUYDep-f275ua9h0q96hbgog1kq77it05nvl1l3',
    'pageviewCount': '4',
    'pageviewCountMSK': '4',
    'tmr_detect': '0%7C1740941037191',
    'undefined': '2040.755',
    'pageviewTimerAll': '2040.755',
    'pageviewTimerMSK': '2040.755',
    'pageviewTimerAllFired15sec': 'true',
    'pageviewTimerAllFired30min': 'true',
    '_ga_2WZB3B8QT0': 'GS1.1.1740939725.10.1.1740941793.0.0.1128847705',
    'call_s': '___htlowve6.1740943598.827790664.185717:571622|2___',
    'csrftoken': 'bMNsn3Z853UN6dWS0kgC1bcSApxPR2zV9p0JuXzqejNBchiJJEFTQ3TJmJaivzNy',
}


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'baggage': 'sentry-environment=PROD,sentry-release=master,sentry-public_key=6f0fe185684eda71da9741fe58c43591,sentry-trace_id=3939e59cbbfe4f42b73120ffafd24f27,sentry-sample_rate=0.1,sentry-transaction=flats,sentry-sampled=false',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://samolet.ru/flats/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '3939e59cbbfe4f42b73120ffafd24f27-8967d98dfbcba32b-0',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    # 'cookie': '_smt=5f304b3c-fcfa-4230-89da-07b20401d1a9; mindboxDeviceUUID=d6b3597d-4b0b-4e45-8167-0b84971b36f7; directCrm-session=%7B%22deviceGuid%22%3A%22d6b3597d-4b0b-4e45-8167-0b84971b36f7%22%7D; _ymab_param=BYeHflO6XUN0s7S7mxCGcH0Zaw6E-ogsUI6oL6LCn20uw6mVuLxheUCUjqi6P1ZNzUoWCCLgIm88uVglZkilWjwhBCQ; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _ym_uid=1740722171243961658; _ym_d=1740722171; _ct=1300000000511218043; _ct_client_global_id=fbe0ef66-3f93-5e30-a689-c3153a19a53a; suggested_city=1; sessionid=mt73xxzzmdnmhsgeqgy4zcn0cgn0b60h; cookies_accepted=1; _ga=GA1.1.745973656.1740722186; FPID=FPID2.2.R9K7jfSqpWPdJvRjcUB9I6d8uo%2F68Nn%2FouyBDgsE13w%3D.1740722186; tmr_lvid=67dc556b7be44bbeeb2284f35f17fd7b; tmr_lvidTS=1740722185746; qrator_jsr=1740829664.757.SUcxAGlJJEACGe3D-89t22p0hsp8dan2qjirgjr3fkatju0ff-00; qrator_jsid=1740829664.757.SUcxAGlJJEACGe3D-4gfmukc5cno2g0lhmmfcisd0tnisdb95; nxt-city=%7B%22dep%22%3A%7B%22version%22%3A1%2C%22sc%22%3A0%7D%2C%22__v_isRef%22%3Atrue%2C%22__v_isShallow%22%3Afalse%2C%22_rawValue%22%3A%7B%22key%22%3A%22moscow%22%2C%22name%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%2C%22url_prefix%22%3A%22%22%2C%22contact_number%22%3A%22%2B7%20495%20292-31-31%22%7D%2C%22_value%22%3A%7B%22key%22%3A%22moscow%22%2C%22name%22%3A%22%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%22%2C%22url_prefix%22%3A%22%22%2C%22contact_number%22%3A%22%2B7%20495%20292-31-31%22%7D%7D; cted=modId%3Dhtlowve6%3Bclient_id%3D745973656.1740722186%3Bya_client_id%3D1740722171243961658; _ym_visorc=b; _ct_ids=htlowve6%3A36409%3A827067534; _ct_session_id=827067534; _ct_site_id=36409; _ym_isad=2; call_s=___htlowve6.1740831475.827067534.143945:445562|2___; csrftoken=HL5XENxGnFFa4FqABV0fXlNDlmSPnRKx9BuYpR9v9w1065gn6112SWYnUzffAEGd; pageviewCount=1; pageviewCountMSK=1; _ga_2WZB3B8QT0=GS1.1.1740829682.6.0.1740829682.0.0.1852189188; domain_sid=wKdbbuq6KB-jddLKpqmNw%3A1740829683659; tmr_detect=0%7C1740829684974; FPLC=NCfPA2YBBNZgqvo5EmTx5wC5y6pFlArzeUA0cS55mqD1LjVkPIyNPRd9Y%2BRaoEVDkkwGmgtP8%2FukJJ6juquPAcOcT5rWDROGXeaguxHI1cR34954y5AiiNZ60g2ySg%3D%3D',
}

projects = [68195, 68192, 68188, 68191, 69106, 69108,
            68199, 69206, 2, 45, 40, 69103, 21, 68196, 31, 69101, 68194, 3, 69051, 55, 1, 49, 68185, 69102, 4, 42,
            69100, 69110]

session = requests.Session()

for project in projects:

    flats = []
    counter = 1
    offset = 0

    while True:

        url = 'https://samolet.ru/backend/api_redesign/flats/?nameType=sale&free=1&type=100000000&ordering=-order_manual,filter_price_package,pk&project=' + str(
            project) + '&offset=' + str(offset) + '&limit=12&page=' + str(counter)
        response = session.get(
            url=url,
            headers=headers,
            cookies=cookies,
        )

        items = response.json()["results"]

        for i in items:
            project_name = i["project"]
            room_id = i["url"]
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
            price = i["price"]
            old_price = i["old_price_with_kitchen_markup"]
            korpus = i["building"]
            floor = i["floor_number"]
            print(
                f"{project_name}, {room_id}, ипотека: {ipoteka}, дата: {date}, тип: {room_type}, площадь: {area}, цена: {price}, старая цена: {old_price}, корпус: {korpus}, этаж: {floor}")
            result = [project_name, room_id, ipoteka, date, room_type, area, price, old_price, korpus, floor]
            flats.append(result)
        if not items:
            print("Всё скачано. Переходим к загрузке в файл")
            break
        counter += 1
        offset += 12

    df = pd.DataFrame(flats,
                      columns=["Проект", "id", "Ипотека", "Дата", "Тип", "Площадь", "Актуальная цена", "Старая цена",
                               "Корпус", "Этаж"])
    df.insert(0, '№', range(1, len(df) + 1))
    print(df)

    date = datetime.date.today()
    df.to_excel(f"2samolet_{project_name}_{date}.xlsx", index=False)

