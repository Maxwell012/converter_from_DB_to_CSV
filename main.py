import sqlite3
import csv


def convert_db_to_csv(database_file):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    # Получаем список таблиц в базе данных
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Для каждой таблицы создаем CSV-файл
    for table in tables:
        table_name = table[0]
        csv_file = f"{table_name}.csv"

        # Получаем данные из таблицы
        cursor.execute(f"SELECT * FROM {table_name};")
        data = cursor.fetchall()

        # Получаем заголовки столбцов
        column_names = [description[0] for description in cursor.description]

        # Записываем данные в CSV-файл
        with open(f"result/{csv_file}", 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(column_names)
            writer.writerows(data)

        print(f"Таблица '{table_name}' конвертирована в файл '{csv_file}'.")

    conn.close()

# Пример использования
database_file = input("Enter DB location: ")
convert_db_to_csv(database_file)
