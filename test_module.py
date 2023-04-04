import unittest
import os
from tempfile import NamedTemporaryFile
import json
import csv
from module import save_file

    
class TestSaveToFile(unittest.TestCase):
    # Тестування винятку, який виникає, якщо файл вже існує
    # NamedTemporaryFile створює тимчасовий файл до визову
    # і очікує що функція поверене ValueError
    def test_existing_file(self):
        with NamedTemporaryFile() as tmp_file:
            with self.assertRaises(ValueError):
                save_file(tmp_file.name, [[1,2],[3,4]], "csv")
            

    # Тестування винятку, який виникає, якщо невідоме розширення файлу 
    def test_invalid_file_format(self):
        file = os.getcwd() + "/file1.pdf"
        self.assertRaises(ValueError, save_file, file, [[1,2],[3,4]], "pdf")
        self.assertRaises(ValueError, save_file, file, [[1,2],[3,4]], "123")
    

    # Тестування винятку, який виникає, якщо дані не двомірні
    def test_invalid_data(self):
        file = os.getcwd() + "/file1.csv"
        self.assertRaises(TypeError, save_file, file, [1, 2, 3], "csv")
    

    # Тестування збереження файла в форматі JSON
    def test_saving_file_JSON(self):
        file = os.getcwd() + "/file1.json"
        data = [[1,2],[3,4]]
        save_file(file, data, "json")
        with open(file, "r") as f:
            file_data = f.read()
        self.assertEqual(json.loads(file_data), data)


    # Тестування збереження файла в форматі CSV
    def test_saving_file_CSV(self):
        file = os.getcwd() + "/file1.csv"
        data = [[1,2],[3,4]]
        save_file(file, data, "csv")
        file_data = []
        with open('file1.csv', newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            for row in csv_reader:
                file_data.append([int(x) for x in row if x])
        self.assertEqual(file_data, data)
    
