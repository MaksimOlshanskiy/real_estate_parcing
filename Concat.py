import os
import glob
import pandas as pd

# Путь к папке, где находятся Excel файлы
folder_path = 'C:\\PycharmProjects\\SeleniumParcer\\Cian\\Тюмень'

# Создаём пустой DataFrame для накопления данных
all_data = pd.DataFrame()

# Используем glob для поиска всех Excel файлов в папке
excel_files = glob.glob(os.path.join(folder_path, "*.xlsx"))

# Проходим по каждому файлу и добавляем его данные в DataFrame
for file_path in excel_files:
    df = pd.read_excel(file_path)  # Читаем Excel файл в DataFrame
    all_data = pd.concat([all_data, df], ignore_index=True)  # Добавляем данные в общий DataFrame

# Проверяем результат
print(all_data)

# Сохраняем объединённые данные в новый Excel файл
output_file = 'C:\\PycharmProjects\\SeleniumParcer\\Cian\\Тюмень\\combined_data.xlsx'
all_data.to_excel(output_file, index=False)

print(f"Все данные сохранены в {output_file}")
