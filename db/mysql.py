from config.db import DB
import mysql.connector
from factory.singleton import SingletonMeta
from config import *

'''
mysql = MySQL()
    cursor = mysql.db.cursor()
    cursor.execute("SHOW DATABASES")
    result = cursor.fetchall()
'''
class MySQL(metaclass=SingletonMeta):

    db = None

    def __init__(self):
        db = mysql.connector.connect(
            host=DB["host"],
            user=DB["user"],
            password=DB["password"]
        )

        self.db = db