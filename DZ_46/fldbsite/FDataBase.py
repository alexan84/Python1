class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = """SELECT * FROM mainmenu"""
        try:
            self.__cur.execute(sql)
            response = self.__cur.fetchall()
            if response:
                return response
        except IOError:
            print('Ошибка чтения из БД.')
        return []