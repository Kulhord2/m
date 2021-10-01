import sqlite3
import sys
import traceback

def db_name():
    return 'SQLite/Delivery_test.db'


def sqlite_create_table(table):
    try:
        sqlite_connection = sqlite3.connect(db_name())
        # print('ok 1')
        cursor = sqlite_connection.cursor()
        # print('ok 2')
        cursor.execute(table)
        # print('ok 3')
        sqlite_connection.commit()
        # print('ok 4')
        # print(f"Table create in SQLite")
        cursor.close()
        return 'ok'
    except sqlite3.Error as error:
        # print(f"Error in connect sqlite {error}(cr)")
        # print("Класс исключения: ", error.__class__)
        # print("Исключение", error.args)
        # print("Печать подробноcтей исключения SQLite: ")
        # print()
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
        return 'error'
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            # print("Close connection")


def create_table():
    # weather
    table = """
            CREATE TABLE IF NOT EXISTS weather(
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            weather TEXT NOT NULL,
            write_datetime datetime KEY,
            temp_max REAL,
            temp_min REAL,
            temp REAL,
            visibility REAL,
            name TEXT
            );
            """
    if sqlite_create_table(table) == 'ok':
        print('ok')
    else:
        print('Error create table')

    # driver_info
    table = """
            CREATE TABLE IF NOT EXISTS driver_info(
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            phone TEXT NOT NULL ,
            password REAL NOT NULL,
            token TEXT KEY
            );
            """
    if sqlite_create_table(table) == 'ok':
        print('ok')
    else:
        print('Error create table')

    # token
    table = """
            CREATE TABLE IF NOT EXISTS token(
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            token BLOB NOT NULL ,
            datetime_write datetime NOT NULL
            );
            """
    if sqlite_create_table(table) == 'ok':
        print('ok')
    else:
        print('Error create table')

    # settings
    table = """
            CREATE TABLE IF NOT EXISTS settings(
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            login TEXT ,
            password TEXT ,
            text_size REAL ,
            Check_internet TEXT ,
            Connect_login TEXT ,
            Connect_password TEXT ,
            Address1 TEXT ,
            Address2 TEXT ,
            Address3 TEXT ,
            Address4 TEXT ,
            DriverId NUMERIC
            );
            """
    if sqlite_create_table(table) == 'ok':
        print('ok')
    else:
        print('Error create table')