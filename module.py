import json
import csv
import argparse
import os


def save_file(file_path, data, file_format):
    """
    Зберігає двомірний масив у відповідному форматі JSON або CSV.

    Args:
        file_path str: Шлях файлу для збереження.
        data str(list[list[int]]): Двомірний список в форматі str.
        file_format  str: Формат файлу для збереження. Може бути 'json' або 'csv'.
    
    Raises:
        ValueError: Якщо файл вже інсує або масив не двомірний або невідомий формат.

    """
    # Перевырка на двомірність
    if not all(isinstance(row, list) for row in data):
        raise TypeError(f"Масив {data} не є двомірним")

    # Перевірка на існування файлу
    if os.path.isfile(file_path):
        raise ValueError(f"Файл {file_path} вже існує")
    
    # Запис файлу та перевіка на відповідність формату
    if file_format == "json":
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
    elif file_format == "csv":
        with open(file_path, "w", newline="") as f:
            csv.writer(f).writerows(data)
    else:
        raise ValueError(f"Невідомий формат файлу: {file_format}")


def arg_parser():
    """ 
    Функція парсить аргументи командного рядка

        Функція повертає класс argparse.Namespace
        з двома аргументами командного рядка: file_path, data
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path",  help="Введений шлях з командного рядка")
    parser.add_argument("data", help="Введений список з командного рядка")
    print(parser.parse_args())
    return parser.parse_args()
    

if __name__ == "__main__":
    args = arg_parser()

    # Десериалізує JSON-рядок в об'єкт
    data = json.loads(args.data)
    
    # Отримуэмо формат файлу з конвертацією до нижнього реєстру 
    file_format = args.file_path.split('.')[1].lower()
    save_file(args.file_path, data, file_format)

