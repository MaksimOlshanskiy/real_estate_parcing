import requests
import datetime
import time
import pandas as pd
import random


ids = [3746490,
       4815344
       ]  # id ЖК для парсинга

proxies = {
    'https': '47.95.203.57:8080'
}

cookies = {
    '_CIAN_GK': '787699e3-fc12-4a31-a77a-6cfd610b499c',
    '_gcl_au': '1.1.1422723987.1740731465',
    'tmr_lvid': 'b47c6c39b48ce8d68592cfa9ff9beaf0',
    'tmr_lvidTS': '1740731465513',
    'sopr_utm': '%7B%22utm_source%22%3A+%22direct%22%2C+%22utm_medium%22%3A+%22None%22%7D',
    '_ga': 'GA1.1.582149124.1740731467',
    '_ym_uid': '1740731467185025844',
    '_ym_d': '1740731467',
    'uxfb_usertype': 'searcher',
    'uxs_uid': '5b193cf0-f5ae-11ef-8867-1b8844357aae',
    'adrcid': 'A0r9KB4fc8duMUv2jPsp-tg',
    'afUserId': 'be3c106f-b0b6-4cef-af07-257ce88c47d3-p',
    'AF_SYNC': '1740731467748',
    'login_button_tooltip_key': '1',
    'cookie_agreement_accepted': '1',
    'session_region_id': '4555',
    'session_main_town_region_id': '4668',
    'login_mro_popup': '1',
    'acs_3': '%7B%22hash%22%3A%22be483547539f1e5fb43aa6ae1ea56ef0a5c5be24%22%2C%22nst%22%3A1741294177487%2C%22sl%22%3A%7B%22224%22%3A1741207777487%2C%221228%22%3A1741207777487%7D%7D',
    '_ym_isad': '2',
    '__zzatw-cian': 'MDA0dBA=Fz2+aQ==',
    'adrdel': '1741266453397',
    'countCallNowPopupShowed': '0%3A1741274868668',
    'sopr_session': '7c05da0fa5804d85',
    '_ym_visorc': 'b',
    'uxfb_card_satisfaction': '%5B279397945%2C308803465%5D',
    '__cf_bm': 'IWypRWEn4ZrUIxO40egJUDc9.umwT5f9sKdLvEiyLw4-1741277358-1.0.1.1-4vSOf.mOFjrlJkD7Xt6rS3pjTnJOGtcztMQ9iKvdlAW.NHUv6l.GogXrKFt_FBSlGMBPUM2xeH6Snig.Df1F4ggG_ZCU_BOzdVjxcdIkvF4',
    'cf_clearance': '5MMokz7l2u8AhjmptDz3rLGd.dCG2GVW0cMOXFdnkb8-1741277358-1.2.1.1-_YS1hFRBjSav1MVPNe3CXqDnhuU57JUqXoyzKWbaJ6RibjRu5g.4n.52NFwM.JqqV8y6NRj3RLLatW29Te8riHF_m.m.Pp6VCEwKm7EYN.G2imZVWPXIjd16FfSTE.ukqdMSjl4gtnNgLhbXaml6zWhVEieaLgn2hUusBen9vJmTrP1wK4XV_TqzXDTgCYRiKbyQ2sk4rPSaByAJplT.wqu280qiox7UPFqautzr.B2pVrpAE1I5rhNpwk1hBttAUZqAoy8IGAJmH3sduyxVYp.0gQwor8OZASfJ41xgiflF8EcQ3BK4GMxo1jICIaqyS.BpTAveqqm_nmMbhJZrNnn_Wh.DT88L3cbm8cCJupgTC80sshjr3MGF50IAenj1ZADrUXsvS1n1qr3dQ3Ig3CDvghubsQ3wMU.iqifaMv0',
    '_ga_3369S417EL': 'GS1.1.1741274870.8.1.1741278042.34.0.0',
    'cfidsw-cian': 'KgNBuiA0UkHyfeP7Pj2wdc5uZevfQn7KrnBRoEjzdBs9U+nwJc9m1MD2qtDybjiien89bQHgZf9z+1Dj414Wsk4U7rZkRh3DS2p0VyJ1FXRkfWJw3Q7QRzxXIgRj9MhvUarszPjqF7y1eHZN/idREKNpyIkh2TNjR18jRw==',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'origin': 'https://barnaul.cian.ru',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://barnaul.cian.ru/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    # 'cookie': '_CIAN_GK=787699e3-fc12-4a31-a77a-6cfd610b499c; _gcl_au=1.1.1422723987.1740731465; tmr_lvid=b47c6c39b48ce8d68592cfa9ff9beaf0; tmr_lvidTS=1740731465513; sopr_utm=%7B%22utm_source%22%3A+%22direct%22%2C+%22utm_medium%22%3A+%22None%22%7D; _ga=GA1.1.582149124.1740731467; _ym_uid=1740731467185025844; _ym_d=1740731467; uxfb_usertype=searcher; uxs_uid=5b193cf0-f5ae-11ef-8867-1b8844357aae; adrcid=A0r9KB4fc8duMUv2jPsp-tg; afUserId=be3c106f-b0b6-4cef-af07-257ce88c47d3-p; AF_SYNC=1740731467748; login_button_tooltip_key=1; cookie_agreement_accepted=1; session_region_id=4555; session_main_town_region_id=4668; login_mro_popup=1; acs_3=%7B%22hash%22%3A%22be483547539f1e5fb43aa6ae1ea56ef0a5c5be24%22%2C%22nst%22%3A1741294177487%2C%22sl%22%3A%7B%22224%22%3A1741207777487%2C%221228%22%3A1741207777487%7D%7D; _ym_isad=2; __zzatw-cian=MDA0dBA=Fz2+aQ==; adrdel=1741266453397; countCallNowPopupShowed=0%3A1741274868668; sopr_session=7c05da0fa5804d85; _ym_visorc=b; uxfb_card_satisfaction=%5B279397945%2C308803465%5D; __cf_bm=IWypRWEn4ZrUIxO40egJUDc9.umwT5f9sKdLvEiyLw4-1741277358-1.0.1.1-4vSOf.mOFjrlJkD7Xt6rS3pjTnJOGtcztMQ9iKvdlAW.NHUv6l.GogXrKFt_FBSlGMBPUM2xeH6Snig.Df1F4ggG_ZCU_BOzdVjxcdIkvF4; cf_clearance=5MMokz7l2u8AhjmptDz3rLGd.dCG2GVW0cMOXFdnkb8-1741277358-1.2.1.1-_YS1hFRBjSav1MVPNe3CXqDnhuU57JUqXoyzKWbaJ6RibjRu5g.4n.52NFwM.JqqV8y6NRj3RLLatW29Te8riHF_m.m.Pp6VCEwKm7EYN.G2imZVWPXIjd16FfSTE.ukqdMSjl4gtnNgLhbXaml6zWhVEieaLgn2hUusBen9vJmTrP1wK4XV_TqzXDTgCYRiKbyQ2sk4rPSaByAJplT.wqu280qiox7UPFqautzr.B2pVrpAE1I5rhNpwk1hBttAUZqAoy8IGAJmH3sduyxVYp.0gQwor8OZASfJ41xgiflF8EcQ3BK4GMxo1jICIaqyS.BpTAveqqm_nmMbhJZrNnn_Wh.DT88L3cbm8cCJupgTC80sshjr3MGF50IAenj1ZADrUXsvS1n1qr3dQ3Ig3CDvghubsQ3wMU.iqifaMv0; _ga_3369S417EL=GS1.1.1741274870.8.1.1741278042.34.0.0; cfidsw-cian=KgNBuiA0UkHyfeP7Pj2wdc5uZevfQn7KrnBRoEjzdBs9U+nwJc9m1MD2qtDybjiien89bQHgZf9z+1Dj414Wsk4U7rZkRh3DS2p0VyJ1FXRkfWJw3Q7QRzxXIgRj9MhvUarszPjqF7y1eHZN/idREKNpyIkh2TNjR18jRw==',
}

json_data = {
    'jsonQuery': {
        '_type': 'flatsale',
        'engine_version': {
            'type': 'term',
            'value': 2,
        },
        'geo': {
            'type': 'geo',
            'value': [
                {
                    'type': 'newobject',
                    'id': 5311424,  # id жилого комплекса
                },
            ],
        },
        'from_developer': {
            'type': 'term',
            'value': True,
        },
        'page': {
            'type': 'term',
            'value': 1,  # номер страницы, увеличиваем на 1
        },
    },
}

current_date = datetime.date.today()

for y in ids:

    flats = []
    counter = 1
    total_count = 1
    json_data["jsonQuery"]["page"]["value"] = 1

    print("Новый ЖК", y)

    json_data["jsonQuery"]["geo"]["value"][0]["id"] = y

    while len(flats) < total_count:

        if counter > 1:
            sleep_time = random.uniform(25, 35)
            time.sleep(sleep_time)

        response = requests.post(
            'https://api.cian.ru/search-offers/v2/search-offers-desktop/',
            cookies=cookies,
            headers=headers,
            json=json_data

        )

        print(response.status_code)

        items = response.json()["data"]["offersSerialized"]

        for i in items:
            project = i["geo"]["jk"]["name"]
            flat_url = i["fullUrl"]
            area = i["totalArea"]
            rooms_count = i["roomsCount"]
            price = i["formattedFullPrice"]

            print(
                f"ЖК {project}, ссылка: {flat_url}, площадь {area}, количество комнат: {rooms_count}, цена: {price}")
            result = [project, flat_url, area, rooms_count, price]
            flats.append(result)

        json_data["jsonQuery"]["page"]["value"] += 1
        print("-----------------------------------------------------------------------------")
        total_count = response.json()["data"]["offerCount"]
        downloaded = len(flats)
        print(f'ID ЖК: {y}. Загружено {downloaded} предложений из {total_count}')
        counter += 1
    time.sleep(30)

    df = pd.DataFrame(flats, columns=["Проект", "url", "Площадь", "Комнаты", "Цена"])
    df = df.drop_duplicates()
    df.insert(0, '№', range(1, len(df) + 1))
    print(df.head())

    filename = f"Cian_{project}_{current_date}.xlsx"
    df.to_excel(filename, index=False)
