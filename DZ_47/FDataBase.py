import sqlite3
import time
import math
import re
from flask import url_for


# получаем данные из таблиц БЗ
class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print('Ошибка чтения из БД.')
        return []

# метод добавления статьи
    def add_post(self, title, text, url):
# проверка что статья с одинаковым url не создавалась ранее
        try:
            self.__cur.execute('SELECT COUNT() as `count` FROM posts WHERE url LIKE ?', (url,))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print('Статья с таким url уже существует')
                return False
            base = url_for('static', filename='images')
            text = re.sub(r"(?P<tag><img\s+[^>]*src=)(?P<quote>[\"'])(?P<url>.+?)(?P=quote)>", r"\g<tag>" + base + r"/\g<url>>", text)
            tm = math.floor(time.time())  # время из секунд , округленное и будет меняться как только добавляются новые статьи
            self.__cur.execute('INSERT INTO posts VALUES(NULL, ?, ?, ?, ?)',
                               (title, text, url, tm))
            self.__db.commit()  # сохраняем БД
        except sqlite3.Error as e:
            print('Ошибка добавления статьи в БД ' + str(e))
            return False
        return True

# метод показывающий статью при вводе в адресную строку
    def get_post(self, alias):
        try:
            self.__cur.execute(f'SELECT title, text FROM posts WHERE url = "{alias}"')
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка получения статьи из БД ' + str(e))
            return False
        return False, False

# превью статей
    def get_posts_annonce(self):
        try:
            # выводим данные о статье и сортируем время в обратном порядке,что бы новая статья выводилась выше
            self.__cur.execute(f'SELECT id, title, text, url  FROM posts ORDER BY time DESC')
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print('Ошибка получения статьи в БД ' + str(e))
            return False
        return []