import sqlite3
import logging

logging.basicConfig(level=logging.DEBUG)


def test_db():
    """Function for get test connection from sqlite"""
    try:
        sqlite_connection = sqlite3.connect("../db.sqlite3")
        cursor = sqlite_connection.cursor()
        logging.info("База данных создана и успешно подключена к SQLite")

        sqlite_select_query = "select sqlite_version();"
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        logging.info(f"Версия базы данных SQLite: {record}")

        cursor.close()
    except sqlite3.Error as error:
        logging.info(f"Ошибка при подключении к sqlite {error}")
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            logging.info("Соединение с SQLite закрыто")


def get_db_cursor() -> sqlite3.Cursor:
    """Function for create db connection"""
    sqlite_connection = sqlite3.connect("../db.sqlite3")
    cursor = sqlite_connection.cursor()
    return cursor
