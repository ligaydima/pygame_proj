import sqlite3

import constants


class Interactor:
    def __init__(self):
        self.connection = sqlite3.connect(constants.DB_NAME)
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS "{constants.TABLE_NAME}" (  
                        "score" INTEGER,
                        "date" DATE)
                        """)
        self.connection.commit()

    def write(self, score):
        self.cursor.execute(f"""INSERT INTO {constants.TABLE_NAME} VALUES ({score}, DATE("now"))""")
        self.connection.commit()

    def get_top_5(self):
        res = sorted(self.cursor.execute(f"""SELECT * FROM {constants.TABLE_NAME}""").fetchall(), reverse=True)
        return res[:min(5, len(res))]

    def close(self):
        self.connection.close()
