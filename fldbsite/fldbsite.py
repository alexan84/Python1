import sqlite3
import os
from flask import Flask, flash, g, redirect, render_template, request, session, url_for

from FDataBase import FDataBase

# придумаем где будет лежать база данных
DATABASE = '/tmp/flsk.db'
# далее дэбаг что бы видеть ошибки
DEBUG = True
# генерируем пароль в 16 ричной системе

SECRET_KEY = '57299cef992cfdcded5bbab88828eae543faa6df'  # os.urandom(20).hex()
# берем данные из этого документа
app = Flask(__name__)
app.config.from_object(__name__)
# обновим создание БД и ее нахождение
app.config.update(DATABASE=os.path.join(app.root_path, 'flsk.db'))


# открываем соединение с БД методом connect и если ее не существует файл создастся автоматически что бы можно было обращаться по ключам
def connect_db():
    connection = sqlite3.connect(app.config['DATABASE'])
    connection.row_factory = sqlite3.Row
    return connection


# создание БД,sq_db.sql содержит запросы к БД и также создает саму таблицу и так же будет режим считывания данных r
def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


#
# устанавливает соединение с БД если оно еще не установлено
def get_db():
    if not hasattr(g, 'link_db'):  # если соединение не установлено
        g.link_db = connect_db()  # вызываем его соединение
    return g.link_db


@app.route('/')
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.get_menu())


#
# закрывет соединение с БД как только пройдет какая то операция
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)
