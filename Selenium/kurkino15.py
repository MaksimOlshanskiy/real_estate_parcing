from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup
import datetime

driver = webdriver.Chrome()


url = "https://kurkino15.ru/search"


def extract_digits_or_original(s):
    digits = ''.join([char for char in s if char.isdigit()])
    return int(digits) if digits else s















flats = []



while True:

    driver.get(url=url)
    page_content = driver.page_source  # Получаем HTML страницы после полной загрузки JavaScript
    soup = BeautifulSoup(page_content, 'html.parser')

    time.sleep(2)

    flats = soup.find_all('div', class_="ResultRow")
    print(len(flats))

    for i in flats:

        print()



        url = ''

        date = datetime.date.today()
        project = ''
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
        adress = ''
        eskrou = ''
        korpus = y[1]
        konstruktiv = ''
        klass = ''
        srok_sdachi = ''
        srok_sdachi_old = ''
        stadia = ''
        dogovor = ''
        finish_type = i.find("div", class_="finishing").text.strip()

        room_count = x[0]
        area = x[1]
        price_per_metr = ''

        discount = ''
        price_per_metr_new = ''
        price2 = extract_digits_or_original(i.find("div", class_=["price"]).text.replace(" ", '').strip())
        print(price2)
        price = extract_digits_or_original(i.find("div", class_="product-card__price").text.replace(" ", '').strip())
        old_price = ''

        section = ''
        floor = y[3]
        flat_number = y[5]

        print(
            f"{project}, {url}, дата: {date}, комнаты: {room_count}, площадь: {area}, цена: {price}, {price2}, {finish_type}, корпус: {korpus}, этаж: {floor}")
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



