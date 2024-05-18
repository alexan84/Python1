# Dz 44 - создать таблицу с очками

import sqlite3
#
# # создадим список с кортежами
#
# glas_tpl = [
#     ('q', 54000),
#     ('w', 46000),
#     ('i', 38000),
#     ('p', 29000),
#     ('z', 33000),
# ]
# #
# with sqlite3.connect('glasses.db') as con:
#     cur = con.cursor()
#     cur.execute('''
#     CREATE TABLE IF NOT EXISTS glas(
#         glas_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     ''')

# cur.execute("INSERT INTO glas VALUES(1, 'g', 22000)")
# cur.execute("INSERT INTO glas VALUES(2, 'h', 29000)")
# cur.execute("INSERT INTO glas VALUES(3, 'j', 57000)")
# cur.execute("INSERT INTO glas VALUES(4, 'd', 35000)")
# cur.execute("INSERT INTO glas VALUES(5, 's', 52000)")
#

# for car in cars_tpl:
#     cur.execute("INSERT INTO glas VALUES(NULL, ?, ?)", car)
#

#     cur.executemany("INSERT INTO glas VALUES(NULL, ?, ?)", glas_tpl)
#
#     cur.execute("UPDATE glas SET price = :Price WHERE model LIKE 'B%'", {"Price": 0})
#
#     cur.executescript("""
#     DELETE FROM glas WHERE model LIKE 'B%';
#     DELETE FROM glas WHERE model LIKE 'C%';
#     DELETE FROM glas WHERE model LIKE 'D%';
#     DELETE FROM glas WHERE model LIKE 'H%';
#     UPDATE glas SET price = price + 100;
#     """)



# def read_ava(n):
#     try:
#         with open(f'avatars/{n}.png', 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, 'wb') as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#     return True
#
#
# with sqlite3.connect('glasses.db') as con:
#     con.row_factory = sqlite3.Row  # что бы обращаться в цикле по ключам
#     cur = con.cursor()
#     cur.executescript('''
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT, ava BLOB, score INTEGER
#     );
#     ''')
#     cur.execute('SELECT ava FROM users')
#     img = cur.fetchone()['ava']
#
#     write_ava('out.png', img)
#
#     # img = read_ava(1)
#     # if img:
#     #     binary = sqlite3.Binary(img)
#     #     cur.execute('INSERT INTO users VALUES ("Илья", ?, 1000)', (binary,))

# with sqlite3.connect('glasses.db') as con:
#     cur = con.cursor()
#
#     with open('sql_damp.sql', 'w') as f:
#         for sql in con.iterdump():
#             print(sql)
#             f.write(sql)

# with sqlite3.connect('glasses_new.db') as con:
#     cur = con.cursor()
#
#     with open('sql_damp.sql', 'r') as f:
#         sql = f.read()
#         cur.executescript(sql)


#*****************************************************************************************










# **********************************************************************************************
# import sqlite3
#
# with sqlite3.connect('students.db') as con:
#     cur = con.cursor()
#
#
# cur.execute("""CREATE  TABLE IF NOT EXISTS student(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     surname TEXT NOT NULL,
#     name TEXT NOT NULL,
#     patronymic TEXT NOT NULL,
#     age INTEGER CHECK (age > 16),
#     group TEXT NOT NULL
#     )""");
#
#
# cur.execute("""CREATE  TABLE IF NOT EXISTS groups(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     group_name TEXT NOT NULL,
#     FOREIGN KEY (id) REFERENCES association (group_id),
#     FOREIGN KEY (id) REFERENCES student (group),
#     )""");
#
# cur.execute("""CREATE  TABLE IF NOT EXISTS association(
#     lesson_id INTEGER NOT NULL,
#     group_id INTEGER NOT NULL,
#     FOREIGN KEY (group_id) REFERENCES groups (id),
#     FOREIGN KEY (lesson_id) REFERENCES lessons (id)
#     )""");
# cur.execute("""CREATE  TABLE IF NOT EXISTS lessons(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     lesson_title TEXT NOT NULL,
#     )""")

################################
# CREATE  TABLE student(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     surname TEXT NOT NULL,
#     name TEXT NOT NULL,
#     patronymic TEXT NOT NULL,
#     age INTEGER CHECK (age > 16),
#     group TEXT NOT NULL
# );
#
#
# CREATE  TABLE groups(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     group_name TEXT NOT NULL,
#     PRIMARY KEY (id) REFERENCES association (group_id)
#     PRIMARY KEY (id) REFERENCES student (group)
# );
#
# CREATE  TABLE association(
#     lesson_id INTEGER NOT NULL,
#     group_id INTEGER NOT NULL,
#     FOREIGN KEY (group_id) REFERENCES groups (id)
#     FOREIGN KEY (lesson_id) REFERENCES lessons (id)
# );
# CREATE  TABLE lessons(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     lesson_title TEXT NOT NULL,
# )

# Dz 37 - спарсить данные с нескольких страниц


# import requests
# from bs4 import BeautifulSoup
#
#
# class Parser:
#     html = ''
#     res = []
#
#     def __init__(self, url, path):
#         self.url = url
#         self.path = path
#
#     def get_html(self):
#         response = requests.get(self.url).text
#         self.html = BeautifulSoup(response, 'lxml')
#
#     def parsing(self):
#         news = self.html.find_all('div', class_='caption')
#         for item in news:
#             title = item.find('h3').text
#             href = item.find('h3').find('a').get('href')
#             author = item.find('a', class_='topic-info-author-link').text.strip()
#             self.res.append({
#                 'title': title,
#                 'href': href,
#                 'author': author
#             })
#
#     def save(self):
#         with open(self.path, 'w') as file:
#             i = 1
#             for item in self.res:
#                 file.write(
#                     f'Новость № {i}\n\nНазвание: {item["title"]}\nСсылка: {item["href"]}\nАвтор: {item["author"]}'
#                     f'\n\n{"*" * 30}\n'
#                 )
#                 i += 1
#
#     def run(self):
#         for i in range(1, 5):
#             self.url + f'page{i}/'
#             self.get_html()
#             self.parsing()
#             self.save()
#
#
# def main():
#     pars = Parser(
#         url='https://www.ixbt.com/live/index/news/',
#         path='news.txt'
#     )
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()

# def main():
#     pars = Parser(
#         url='https://www.ixbt.com/live/index/news/',
#         path='news.txt'
#     )
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()


# Dz 36 - с любого интернер ресурса получить данные в несколько переменных и вывести их


# import requests
# from bs4 import BeautifulSoup
#
#
# def practice_html_1(url_1):
#     r = requests.get(url_1)
#     return r.text
#
#
# def get_data_1(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     datas = soup.find('div', class_="flex--item py32 md:pt16 md:pb16").text
#     return datas
#
#
#
#
# def main():
#     # url_1 = 'https://ru.stackoverflow.com/questions/822357/%D0%BD%D0%B5-%D0%BC%D0%BE%D0%B3%D1%83-%D0%B8%D0%BC%D0%BF%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D1%82%D1%8C-%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C-%D0%B2-%D0%BF%D0%B8%D1%82%D0%BE%D0%BD%D0%B5'
#     url_1 = 'https://stackoverflow.com/'
#     print(get_data_1(practice_html_1(url_1)))
#
#
#
# if __name__ == '__main__':
#     main()

# Dz 35

# import csv
#
# with open('data2.csv', encoding='UTF-8') as f:
#     file_datas = csv.reader(f, delimiter=';')
#     count = 0
#     for file_data in file_datas:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(file_data)}")
#         else:
#             print(f" Имя доменна: {file_data[0]}, Поставщик: {file_data[1]}, "
#                   f"Номер: {file_data[2]}, Локация: {file_data[3]}")
#         count += 1


# Dz 34

# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ', '.join(map(str, self.marks))
#         return f"Студент: {self.name}: {a}"
#
#     def add_mark(self, mark):
#         """Добавляем оценку студенту"""
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         """Удаление оценки студента"""
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         """Заменяем оценку на другую, у студента"""
#         self.marks[index] = new_mark
#
#     def average_mark(self):
#         """Средний бал всех оценок студента"""
#         return round(sum(self.marks) / len(self.marks), 1)
#
#     def dump_to_json(self):
#         """Создаем файл по имени студента"""
#         data = {'name': self.name, 'marks': self.marks}
#         with open(self.get_file_name(), 'w', encoding='UTF-8') as f:
#             json.dump(data, f)
#
#     def load_from_file(self):
#         """Открываем файл по мени студента"""
#         with open(self.get_file_name(), 'r', encoding='UTF-8') as f:
#             print(json.load(f))
#
#     def get_file_name(self):
#         """Вспомогательный метод для создания и открытия файлов"""
#         return self.name + '.json'
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = '\n'.join(map(str, self.students))
#         return f"\nГруппа: {self.group} \n{a}"
#
#     def add_student(self, student):
#         """Добавляем студента в группу"""
#         self.students.append(student)
#
#     def remove_student(self, index):
#         """Удаляем студента из группы"""
#         return self.students.pop(index)
#
#     @staticmethod
#     def change_group(group_1, group_2, index):
#         """Перемещаем студента из одной группы в другую"""
#         group_2.add_student(group_1.remove_student(index))
#
#     def get_student(self):
#         """Распаковка - распаковываем данные о студенте"""
#         return [{'name': student.name, 'marks': student.marks} for student in self.students]
#
#     def dump_to_json(self):
#         """Записываем группы, и находящий в них студентов в файл json"""
#         a_data = {self.group: self.get_student()}
#
#         try:
#             data = json.load(open(self.get_file_name()))
#         except FileNotFoundError:
#             data = []
#
#         data.append(a_data)
#         with open(self.get_file_name(), 'w', encoding='UTF-8') as f:
#             json.dump(data, f, indent=2)
#
#     def get_file_name(self):
#         """Вспомогательный метод - содержит имя файла"""
#         return 'groups' + '.json'
#
#     def load_from_file(self):
#         """Загружает данные из json"""
#         with open(self.get_file_name(), 'r', encoding="UTF-8") as f:
#             print(json.load(f))
#
#     @staticmethod
#     def dump_groups(file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = {}
#
#         with open(file, 'w', encoding='UTF-8') as f:
#             stud_list = {}
#             for i in group.students:
#                 stud_list[i.name] = i.marks
#
#         data[group.group] = stud_list
#         json.dump(data, f, indent=2)
#
#     @staticmethod
#     def load_groups(file):
#         with open(file, 'r', encoding='UTF-8') as f:
#             print(json.load(f))
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
#
# gr1 = [st1]
# gr2 = [st2]
# gr3 = [st3]
#
# group1 = Group(gr1, 'Web')
# group2 = Group(gr2, 'Python')
# group3 = Group(gr3, 'JavaScript')
#
# group1.dump_to_json()
# group2.dump_to_json()
# group3.dump_to_json()
#
# group1.load_from_file()

# Group.dump_groups('groups.json', group1)
# Group.dump_groups('groups.json', group2)
# Group.load_groups('groups.json')
####
# Dz 33
# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#
#     latter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'e']
#     num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(latter)
#
#     while len(tel) != 10:
#         tel += choice(num)
#
#     person = {
#         'name': name,
#         'tel': tel,
#     }
#     return person
#
#
# def get_key():
#     keys = ''
#     data = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(keys) != 10:
#         keys += choice(data)
#
#     return keys
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('homework.json'))
#     except FileNotFoundError:
#         data = {}
#
#     data.update(person_dict)
#     with open('homework.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(2):
#     write_json({get_key(): gen_person()})

# Dz 32
# from ep.salary_employee import SalaryEmployee
# from ep.hourly_employee import HourlyEmployee
# from ep.sales_representative import SalesRepresentative
# from ep.payroll_system import PayrollSystem
#
# salary_employee = SalaryEmployee(1, "Валерий Задорожный", 1500)
# hourly_employee = HourlyEmployee(2, "Илья Кромин", 40, 15)
# sales_representative = SalesRepresentative(3, "Николай Хорольский", 1000,
#                                            250)
#
# payroll_system = PayrollSystem()
# payroll_system.calculate([
#     salary_employee,
#     hourly_employee,
#     sales_representative
# ])

# Dz 31

# class DescriptorOrder:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, int):
#             raise TypeError("Сумма и количество должно быть числом!")
#         if value < 0:
#             raise ValueError("Цена и количество товара не может быть отрицательным")
#         instance.__dict__[self.__name] = value
#
#
# class Order:
#     price = DescriptorOrder()
#     quantity = DescriptorOrder()
#
#     def __init__(self, product, price, quantity):
#         self.product = product
#         self.price = price
#         self.quantity = quantity
#
#
# order = Order('iPhone 14 Pro Max', 104_000, 10)
#
# order.price = 102_000
# order.quantity = 8
# print(f"Цена: {order.price} \nКоличество: {order.quantity}")
# print(order.__dict__)


# Dz 30

# сделаем 2 эеземпляра и сложим их
# class Point3D:
#     def __init__(self, x, y, z):  # инициализируем 3 точки
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __repr__(self):  # метод визуального контроля
#         return f"{self.x}, {self.y}, {self.z}"
#
#     @staticmethod
#     def check(other):  # статический метод проверяющий правый операнд
#         if not isinstance(other, Point3D):
#             raise ValueError("Правый операнд должен быть типом класса Point3D")
#
#     def __add__(self, other):  # метод складывающий два экземпляра класса
#         self.check(other)
#         x = self.x + other.x
#         y = self.y + other.y
#         z = self.z + other.z
#         return Point3D(x, y, z)
#
#     def __sub__(self, other):
#         self.check(other)
#         x = self.x - other.x
#         y = self.y - other.y
#         z = self.z - other.z
#         return Point3D(x, y, z)
#
#     def __mul__(self, other):
#         self.check(other)
#         x = self.x * other.x
#         y = self.y * other.y
#         z = self.z * other.z
#         return Point3D(x, y, z)
#
#     def __truediv__(self, other):
#         self.check(other)
#         x = self.x / other.x
#         y = self.y / other.y
#         z = self.z / other.z
#         return Point3D(x, y, z)
#
#     def __eq__(self, other):  # метод равенства
#         self.check(other)
#         return self.x == other.x and self.y == other.y and self.z == other.z
#
#     def __getitem__(self, item):  # вывод цифровых значений координат по ключу
#         key = {'x': self.x,
#                'y': self.y,
#                'z': self.z}
#         try:
#             return key[item]
#         except KeyError:
#             raise ValueError("Ключ должен быть строкой")
#
#     def __setitem__(self, key, value):  # установим новое значение координат по ключу
#         if not isinstance(key, str):
#             raise ValueError(f"Ключ должен быть строкой")
#
#         if not isinstance(value, int):
#             raise TypeError(f"Значение должно быть числом")
#
#         if key == 'x':
#             self.x = value
#         if key == 'y':
#             self.y = value
#         if key == 'z':
#             self.z = value
#
#
# # это сложить между собой
# p1 = Point3D(12, 15, 18)
# p2 = Point3D(6, 3, 9)
#
# print(f"Координаты 1-й точки:", p1)
# print(f"Координаты 2-й точки:", p2)
# print()
# # перегрузка вычислений происходит с помощью методов __add__,
# p3 = p1 + p2
# p4 = p1 - p2
# p5 = p3 * p4
# p6 = p3 / p4
#
# print(f"Сложение координат:", p3)
# print(f"Вычитание координат:", p4)
# print(f"Умножение координат:", p5)
# print(f"Деление координат:", p6)
# print()
#
# print(f"Равенство координат:", p1 == p2)
# print()
# # вывод цифровых значений координат по ключу
# print(f"x1 = {p1['x']}, x2 = {p2['x']}")
# print(f"y1 = {p1['y']}, y2 = {p2['y']}")
# print(f"z1 = {p1['z']}, z2 = {p2['z']}")
# # установим новое значение координат по ключу
# p2['x'] = 20
# print(f"Запись значение в координату x2: {p2['x']}")
# # вывод значения которое изменили p2['x']
# print(f"x1 = {p1['x']}, x2 = {p2['x']}")


# Dz 29 -
#
# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f'{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}'
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else '0' + str(x)
#
#     @staticmethod
#     def check(other):
#         """Исключение для Перегрузки операторов. \n
#            Служит для проверки правого операнда, что он является типом класса Clock."""
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом класса Clock")
#
#     def __add__(self, other):
#         self.check(other)
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         self.check(other)
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#         self.check(other)
#         return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):
#         self.check(other)
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):
#         self.check(other)
#         return Clock(self.sec % other.sec)
#
#
# c1 = Clock(100)
# c2 = Clock(200)
# print(c1.get_format_time())
# print(c2.get_format_time())
#
# c3 = c1 + c2
# c4 = c1 - c2
# c5 = c1 * c2
# c6 = c1 // c2
# c7 = c1 % c2
#
# print()
# print(f'{c3.get_format_time()} (x + y)')
# print(f'{c4.get_format_time()} (x - y)')
# print(f'{c5.get_format_time()} (x * y)')
# print(f'{c6.get_format_time()} (x // y)')
# print(f'{c7.get_format_time()} (x % y)')

# Dz 28 - класс студент

# class Studen:
#     def __init__(self,name):
#         self.name = name
#         self.comp = self.comp()  # доступ к классу комп
#
#     def infa(self):  # метод распечатывающий инфу
#         print(f'{self.name}', '=>',end=' ')
#         print(f'{self.comp.model}', end=' ')
#         print(f'{self.comp.cpu}',end=' ')
#         print(f'{self.comp.gpu}')
#
#
#
#     class comp():  # класс с инфой о компе
#         def __init__(self):
#             self.model = 'hp'
#             self.cpu = 'i7'
#             self.gpu = '16'
#
#
#
# roman = Studen('roman')
# roman.infa()
# vladimir =Studen('vladimir')
# vladimir.infa()


# Dz 28 - создать класс стол и дочерние классы
# import math
#
#
# class Table:
#
#     def __init__(self, width, length, radius):
#         self._width = width
#         self._length = length
#         self._radius = radius
#
#     def info_square_table(self):
#         raise NotImplementedError("В классе должен метод square_table()")
#
#
# class TableRectangular(Table):
#     def square_table(self):
#         return self._width * self._length
#
#     def set_square_table(self, width=None, length=None):
#         if width is None:
#             if length:
#                 self._length = length
#
#         elif length is None:
#             if width:
#                 self._width = width
#
#         else:
#             if width and length:
#                 self._width = width
#                 self._length = length
#
#     def info_square_table(self):
#         print(f"Площадь прямоугольного стола: {self.square_table()}")
#
#
# class TableRound(Table):
#     def square_table(self):
#         return round(math.pi * (self._radius ** 2), 2)
#
#     def info_square_table(self):
#         print(f"Площадь круглого стола: {self.square_table()}")
#
#
# rec = TableRectangular(20, 10, 0)
# rec.info_square_table()
# rec.set_square_table(length=20)
# rec.info_square_table()
# ro = TableRound(0, 0, 20)
# ro.info_square_table()


# Dz 27 - доработать  класс аккаунт

# import re
#
#
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     SUFFIX_RUB = 'RUB'
#     SUFFIX_USD = 'USD'
#     SUFFIX_EUR = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = self.set_surname(surname)
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f'Счёт №{self.num} принадлежащий {self.surname} был открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счёт №{self.num} принадлежащий {self.surname} был закрыт.')
#
#     @classmethod
#     def set_rate_usd(cls, new_rate):
#         cls.rate_usd = new_rate
#
#     @classmethod
#     def set_rate_eur(cls, new_rate):
#         cls.rate_eur = new_rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @property
#     def value(self):
#         return self.__value
#
#     @value.setter
#     def value(self, new_value):
#         if not isinstance(new_value, (int | float)):
#             raise TypeError('Убедитесь что введено цифровое значение для баланса')
#         if new_value < 0:
#             raise ValueError('Отрицательное значение баланса не допустимо.')
#         self.__value = round(float(new_value), 2)
#
#     def get_surname(self):
#         return self.surname
#
#     def set_surname(self, new_surname: str):
#         if not isinstance(new_surname, str):
#             raise TypeError('Фамилия должна быть строкой')
#         elif re.findall(r'[^а-яё-]', new_surname, re.IGNORECASE):
#             raise ValueError('Допустимы только буквы А-я и -')
#         self.surname = new_surname
#
#     def add_money(self, amount):
#         self.value += amount
#         print(f'{amount} {Account.SUFFIX_RUB} успешно добавлено!')
#         self.print_balance()
#
#     def convert_to_usd(self):
#         usd_value = self.convert(self.value, self.rate_usd)
#         print(f'Состояние счёта: {usd_value} {Account.SUFFIX_USD}')
#
#     def convert_to_eur(self):
#         eur_value = self.convert(self.value, self.rate_eur)
#         print(f'Состояние счёта: {eur_value} {Account.SUFFIX_EUR}')
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print(f'Проценты были успешно начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, amount):
#         if amount > self.value:
#             print(f'К сожалению у вас нет {amount} {Account.SUFFIX_RUB}')
#         else:
#             self.value -= amount
#             print(f'{amount} {Account.SUFFIX_RUB} было успешно снято!')
#         self.print_balance()
#
#     def print_balance(self):
#         print(f'Текущий баланс: {self.value} {Account.SUFFIX_RUB}.')
#
#     def print_info(self):
#         print('Информация о счете:')
#         print('-' * 20)
#         print(f'№{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#
# if __name__ == '__main__':
#     acc = Account('Долгих', '12345', 0.03, 5000)
#     acc.print_info()
#     acc.convert_to_usd()
#     acc.convert_to_eur()
#     Account.set_rate_usd(2)
#     Account.set_rate_eur(3)
#     print()
#     acc.convert_to_usd()
#     acc.convert_to_eur()
#     acc.set_surname('Дюма')
#     acc.print_info()
#     print()
#     acc.add_percent()
#     print()
#     acc.withdraw_money(100)
#     print()
#     acc.withdraw_money(3000)
#     print()
#     acc.add_money(5000)
#     print()
#     acc.withdraw_money(3000)
#     print()


# Dz 26 - Создать класс персон


# class Person:
#
#     def __init__(self, name: str, old: int):
#         __name = ''
#         __old = 0
#         self.name = name
#         self.old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         if not isinstance(new_name, str):
#             raise TypeError('Имя задается строкой')
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, new_old):
#         if not isinstance(new_old, int):
#             raise TypeError('Возраст задаётся цифрами')
#         self.__old = new_old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# person = Person(name='Irina', old=26)
# print(person.__dict__)
# person.name = 'Igor'
# print(person.name)
# person.old = 31
# print(person.old)
#
# del person.name
# print(person.__dict__)


#
# # Dz 25 Создать класс прямоугольник
#
# from math import sqrt
#
#
# class Rectangle:
#     def __init__(self, length, height):
#         self.length = length
#         self.height = height
#         self.area = self.length * self.height
#         self.perimeter = 2 * (self.length + self.height)
#         self.diagonal = round(sqrt(self.length ** 2 + self.height ** 2), 2)
#
#     def get_length(self):
#         return f'Длина прямоугольника: {self.length}'
#
#     def get_height(self):
#         return f'Ширина прямоугольника: {self.height}'
#
#     def get_area(self):
#         return f'Площадь прямоугольника: {self.area}'
#
#     def get_perimeter(self):
#         return f'Периметр прямоугольника: {self.perimeter}'
#
#     def get_diagonal(self):
#         return f'Гипотенуза прямоугольника: {self.diagonal}'
#
#     def __str__(self):
#         graphic = ''
#         for i in range(self.length):
#             if i == 0 or i == self.length - 1:
#                 graphic += '* ' * self.height + '\n'
#             else:
#                 graphic += '* ' + '  ' * (self.height - 10) + '*' + '\n'
#         return graphic
#
#
# rectangle = Rectangle(3, 9)
# print(rectangle.get_length())
# print(rectangle.get_height())
# print(rectangle.get_area())
# print(rectangle.get_perimeter())
# print(rectangle.get_diagonal())
# print(rectangle)


# Dz 24 Создать класс автомобиль

#
# class Car:
#
#     def __init__(
#             self, model, year_of_issue, manufacturer, engine_power, color, price, ):
#         self.model = model
#         self.year_of_issue = year_of_issue
#         self.manufacturer = manufacturer
#         self.engine_power = engine_power
#         self.color = color
#         self.price = price
#
#     def __str__(self):
#         a = 'данные атомобиля '
#         b = f'\nНазвание модели: {self.model}\n' \
#             f'Год выпуска: {self.year_of_issue}\n' \
#             f'Производитель: {self.manufacturer}\n' \
#             f'Мощность двигателя: {self.engine_power} л.с.\n' \
#             f'Цвет машины: {self.color}\n' \
#             f'Цена: {self.price}\n'
#
#         return a + b
#
#     def set_model(self, model):
#         self.model = model
#
#     def get_model(self):
#         return self.model
#
#     def set_year_of_issue(self, year_of_issue):
#         self.year_of_issue = year_of_issue
#
#     def get_year_of_issue(self):
#         return self.year_of_issue
#
#     def set_manufacturer(self, manufacturer):
#         self.manufacturer = manufacturer
#
#     def get_manufacturer(self):
#         return self.manufacturer
#
#     def set_engine_power(self, engine_power):
#         self.engine_power = engine_power
#
#     def get_engine_power(self):
#         return self.engine_power
#
#     def set_color(self, color):
#         self.color = color
#
#     def get_color(self):
#         return self.color
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
#
# if __name__ == '__main__':
#     car = Car(
#         model='X7 M50i',
#         year_of_issue='2021',
#         manufacturer='BMW',
#         engine_power=530,
#         color='white',
#         price=10790000
#     )
#
#     print(car)

# DZ 23 - просканировать директорию и вывести размер и название файлов и папок
# import os
# import time
#
# file_path = r'test\folder1\file.txt'
# if os.path.exists(file_path):
#     dirs, name = os.path.split(file_path)
#     print(f'{name} - {os.path.getsize(file_path)} bytes ')
#     print(f'{dirs} - dir ')
# else:
#     print(f'Файл {file_path} не существует')


# DZ 22 - Обмен местами двух строк в файле

# # Создадим файли закоментируем его
# f = open('text2.txt','w')
# f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n')
# f.close()

# Считываем данные файла и записываем в переменную
# f = open("text2.txt", "r")
# rl = f.readlines()
# f.close()
#
# # Заменили по индексу вторую строку
# print(rl)
# rl[1] = rl[0] # 'Hello World\n'
# print(rl)
#
# pos = int(input('Введите индекс для замены: '))
# if 0 <= pos < len(rl):
#     rl.pop(pos)
# else:
#     print('Индекс введен не верно')
#
#
# # Только тут перезапишем в самом файле нужный элемент
# f = open("text2.txt","w")
# f.writelines(rl)
# f.close()


# DZ 21 - Вычислить количество отрицательных чисел в массиве(списке)


# def count(lst):
#     if len(lst) == 1:
#         if lst[0] < 1:
#             return 1
#         else:
#             return 0
#     else:
#         if lst[0] < 1:
#             return 1 + count(lst[1:])
#         else:
#             return count(lst[1:])
#
#
# print("count ", count([-2, 3, 8, -11, -4, 6,]))


# DZ 20 - валидация номера телефона
# import re
# st = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78'
# print(re.findall( r"(?:(?:8|\+7)[\- ]?)?(?:\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}", st))


# DZ 19 - Найти адрес электронной почты
# import re
# st = '123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru'
# print(re.findall( r"[\w._-]+@[\w._-]+\.[\w.]+", st))


# DZ 18 - дана строка в которой h встречается минимум два раза.
# Разверните последовательность символов,заключенную между первым и последним
# появлением буквы h в противоположном порядке

# s = 'I am lerning Python. hello, WORLD'
# # a = (s[s.find('h')+1:s.rfind('h')])
# # print(a[::-1])
#
#
# s1=s[:s.find('h')]
# s2=s[s.rfind('h'):s.find('h'):-1]
# s3=s[s.rfind('h'):]
# print(s1+s2+s3)


# DZ 17 - даны два числа a = 122, b = 97, где a и b - коды символов.Нужно вывести все символы,
# ASCII- коды которых лежат между
# a и b включительно, в порядке возрастания их кодов

# a = 122
# b = 97
# print(*(chr(x) for x in range(a, b + 1)) if a < b else (chr(x) for x in range(b, a + 1)))

# DZ 16 - Создать функцию,которая находит сумму чисел и декоратор,
# который находит среднее арифметическое этих чисел

# def an(num):
#     def wrap(*args):
#         c = num(*args) / len(args)
#         print('Среднее арифметическое', c)
#
#     return wrap
#
#
# @an
# def ms(*args):
#     a = sum(args)
#     print('Сумма чисел:', a)
#     return a
#
#
# ms(2, 3, 3, 4)

# DZ 15 - Создать лямбда-выражения для нахождения площадей фигур
#
# a = [
#     lambda x, y: x * y,
#     lambda x, y, c: (x + y) * c / 2,
#     lambda x,: 3.14 * x ** 2
#
# ]
#
# print('Прямоугольник', a[0](2, 5))
# print('Трапеция', a[1](7, 5, 3))
# print('Круг', a[2](2))

# DZ 14 - Пользователь вводит данные студентов нужно определить средний балл и вывести данные студентов


# <<<<<<< HEAD
# stu = {}
# n = int(input("Количество студентов: "))
# s = 0
# for i in range(n):
#     sname = input(str(i+1) + "-й студент: ")
#     poin = int(input("Балл: "))
#     stu[sname] = poin
#     s += poin
#
# avrg = s / n
# print("\nСредний балл: %.0f. Студенты с баллом выше среднего:" % avrg)
# for i in stu:
#     if stu[i] > avrg:
#         print(i)
#
#
#
#
# =======
# studs = {}
# n = int(input("Количество студентов: "))
# s = 0
# for i in range(n):
#     sname = input(str(i+1) + "-й студент: ")
#     point = int(input("Балл: "))
#     studs[sname] = point
#     s += point
#
# avrg = s / n
# print("\nСредний балл: %.0f. Студенты с баллом выше среднего:" % avrg)
# for i in studs:
#     if studs[i] > avrg:
#         print(i)
# >>>>>>> 14285a936aef2e2d90ffe640d0ef4f65bc662efe
#
#
# # DZ 13 Найти общую прибыль
# a = ['January', 'February', 'March']
# b = [52000.00, 51000.00, 48000.00]
# c = [46800.00, 45900.00, 43200.00]
# for s, k, m in zip(b, c, a):
#     p = s - k
#     print('прибыль в', m, '=', p)


# DZ 12 Создать новый словарь с именем и зарплатой
# и удалить их из исходного словаря


# a = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# a.clear()
# print(a)

# a = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d = list(a.items())[1]
# print(d)
# b = a.pop('name')
# c = a.pop('salary')
# print(a)
# a = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# del a['age']
# del a['city']
#
# print(a)


# DZ 11 Посчитать количество гласных букв

# s = input("Введите строку:")
# count = 0
# a = set("а, я, у, ю, о, е, ё, э, и, ы")
# for i in s:
#     if i in a:
#         count += 1
# print('Количество гласных равно:', count)

# DZ 10 выведите статистику частности символов в кортеже - 253523651
# b = input('= ')
# a = tuple(b)
# for x in set(a):
#     print(f'{x} - {a.count(x)}')


# DZ 9 - Заполните один кортеж десятью случайными числами от 0 до 5 включительно.
# Так же заполните второй кортеж числами от -5 до 0.
# Для заполнения кортежей числами напишите одну функцию.
# Объедените два кортежа с помощью +,создав третий кортеж.
# С помощью метода кортежа count() определите в нем кол-во. нулей.
# Выведите на экран третий кортеж и количество нулей в нем

# from random import randint
#
# def slicer():
#     s = tuple(randint(0, 5) for i in range(10))
#     c = tuple(randint(-5, 0) for i in range(10))
#     a = s + c
#     # return a
#     print(a.count(0))
#     return a
#
# print(slicer())


# # DZ 8 функция площади фигур
# from math import sqrt, pi
#
# print("1-прямоугольник, 2-треугольник, 3-круг")
# figure = input("Выберите фигуру: ")
#
# if figure == '1':
#     print("Длины сторон прямоугольника:")
#     a = float(input("a = "))
#     b = float(input("b = "))
#     print("Площадь: %.2f" % (a * b))
# elif figure == '2':
#     print("Длины сторон треугольника:")
#     a = float(input("a = "))
#     b = float(input("b = "))
#     c = float(input("c = "))
#     p = (a + b + c) / 2
#     s = sqrt(p * (p - a) * (p - b) * (p - c))
#     print("Площадь: %.2f" % s)
# elif figure == '3':
#     r = float(input("Радиус круга R = "))
#     print("Площадь: %.2f" % (pi * r ** 2))
# else:
#     print("Ошибка ввода")


# # DZ 7 Заполнить список случайными числами
# import random
#
#
# nums = list(range(10))
#
# random.shuffle(nums)
# print(nums[0:10])


# DZ 6 дан список .
# выведите те его элементы которые встречаются в списке только один
# раз.элементы нужно выводить в том порядке в котором они
# встречаются в списке

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i != j and a[i] == a[j]:
#             break
#     else:
#         print(a[i], end=' ')


# # DZ 5 Найти среднее арифметическое всех ненулевых элементов введенного списка
# a = [int(input("->")) for i in range(int(input("Введите количество элементов списка: n = ")))]
# print(a)
# sa = 0
# c = 0
# for i in range(len(a)):
#     if a[i] > 0:
#         c += 1
#         sa += a[i]
#
#
# print(sa / c)


# DZ 4
# a = 5
#
# count = 0
#
# while 0 < a <= 100:
#     user = int(input("Введите число: "))
#     print(user)
#     count += 1
#     if user == a or user == 0:
#         print("Угадали\nколичество попыток", count)
#         if user == 0:
#             print("Конец")
#         break
#
#     elif user > a:
#         print("Число меньше")
#     elif user < a:
#         print("Число больше")


# DZ 3 (18.11.23)
# a = int(input("Число символов: "))
# b = input("Тип символов: ")
# c = int(input("Ориентация строки 0 или 1: "))
# i = 0
# while i < a:
#     if c == 0:
#         print(b, end=" ")
#         i += 1
#     else:
#         print(b, end="\n")
#         i += 1


# DZ 2
# a = 5
# b = 7
# c = 3
# d = a+b+c
# e = a*b*c
# x = (a+b+c)/3
# print("Среднее арифметическое", x)
# print("Произвеление чисел", e)
# print("Сумма чисел", d)
