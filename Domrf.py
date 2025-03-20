# скрипт для загрузки по-недельных отчётов о выданных кредитах и составлении годовых отчётов. 

import pandas as pd
import requests
from io import BytesIO
from datetime import datetime, timedelta
import time
import os

def filter_regions(df, column_name):
    """
    Фильтрует строки DataFrame, оставляя только те, где в названии есть слово 'область' или 'край'.

    Parameters:
    df (pd.DataFrame): Исходный DataFrame
    column_name (str): Название столбца, по которому нужно фильтровать

    Returns:
    pd.DataFrame: Отфильтрованный DataFrame
    """
    return df[df[column_name].str.contains('область|край|республика|город|ненецкий|еврейская|Ханты-Мансийский|Чукотский', case=False, na=False)]

params = {
    'date': "28.12.2023"
}
counter = 1
target_date = datetime(2023, 1, 1)
new_date = datetime(2023, 1, 2)
while target_date <= new_date:
    response = requests.get(
        'https://xn--d1aqf.xn--p1ai/api/public/content/mortgage/reports/weeklyreport/?type=itm&reportType=region&format=xlsx', params=params)

    if counter == 1:
        excel_data = BytesIO(response.content)
        df_new = pd.read_excel(excel_data)
        df_new.columns = ['Регион', 'Принято заявок, шт.', 'Одобрено заявок, шт.', 'Количество отказов, шт.',
                       'Заключено кредитов, шт.', 'Заключено кредитов, млн руб.', 'Выдано кредитов, шт.',
                       'Выдано кредитов, млн руб.']
        df_new = filter_regions(df_new, 'Регион')
        print(df_new.info())
    else:

        excel_data = BytesIO(response.content)
        df_next = pd.read_excel(excel_data)
        df_next.columns = ['Регион', 'Принято заявок, шт.', 'Одобрено заявок, шт.', 'Количество отказов, шт.',
                          'Заключено кредитов, шт.', 'Заключено кредитов, млн руб.', 'Выдано кредитов, шт.',
                          'Выдано кредитов, млн руб.']
        df_next = filter_regions(df_next, 'Регион')
        df_new = pd.concat([df_new, df_next], ignore_index=True)
        print(df_new.info())

    # Строка с датой
    date_str = params["date"]

    # Преобразуем строку в объект даты
    date_obj = datetime.strptime(date_str, "%d.%m.%Y")

    # Вычитаем 7 дней
    new_date = date_obj - timedelta(days=7)

    # Результат
    print("Новая дата:", new_date.strftime("%d.%m.%Y"))

    params["date"] = str(new_date.strftime("%d.%m.%Y"))
    counter += 1

    time.sleep(6)

grouped_df = df_new.groupby('Регион').sum()


# Базовый путь для сохранения
base_path = r"C:\PycharmProjects\SeleniumParcer\Domrf"

folder_path = os.path.join(base_path, "2023")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

filename = f"part1.xlsx"

# Полный путь к файлу
file_path = os.path.join(folder_path, filename)

# Сохранение файла в папку
grouped_df.to_excel(file_path, index=True)



