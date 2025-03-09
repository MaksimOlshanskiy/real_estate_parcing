import requests
import datetime
import time
import pandas as pd

headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain',
    'Origin': 'https://www.pik.ru',
    'Referer': 'https://www.pik.ru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}




flats = []
counter = 1

while True:
    url = 'https://flat.pik-service.ru/api/v1/filter/flat-by-block/518?type=1,2&location=2,3&flatPage='+str(counter)+'&flatLimit=8&onlyFlats=1'
    response = requests.get(
        url=url,
        headers=headers,
    )

    print('--------------------------------------------------------------')
    items = response.json()["data"]["items"]

    for i in items:
        project = i["blockName"]
        room_id = "https://www.pik.ru//flat/" + str(i["id"])
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
        area = i["area"]
        price = i["price"]
        old_price = i["oldPrice"]
        korpus = i["bulkName"]
        floor = i["floor"]
        print(f"{project}, {room_id}, ипотека: {ipoteka}, дата: {date}, тип: {room_type}, площадь: {area}, цена: {price}, старая цена: {old_price}, корпус: {korpus}, этаж: {floor}")
        result = [project, room_id, ipoteka, date, room_type, area, price, old_price, korpus, floor]
        flats.append(result)
    if not items:
        print("Всё скачано. Переходим к загрузке в файл")
        break
    counter += 1
    time.sleep(3)

df = pd.DataFrame(flats, columns=["Проект", "id", "Ипотека", "Дата", "Тип", "Площадь", "Актуальная цена", "Старая цена", "Корпус", "Этаж"])
df.insert(0, 'Row Number', range(1, len(df) + 1))
print(df)

current_date = datetime.date.today()
filename = f"Pik_{project}_{current_date}.xlsx"
df.to_excel(filename, index=False)