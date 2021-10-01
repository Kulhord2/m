import sqlite3
import sys
import traceback
from SQLite.SQLite_CRUD_Querry.SQLite_Create_Tables import db_name


def sqlite_write_table(table: str, data_dic: dict):
    try:
        sqlite_connection = sqlite3.connect(db_name())
        cursor = sqlite_connection.cursor()
        # print('DB connect in SQLite')
        col = set()
        # val = set()
        val = []
        for key, values in data_dic.items():
            # print(key, values)
            col.add(key)
            # val.add(values)
            val.append(values)
        # print(val)
        if len(val) != 1:
            query = ('?,' * (len(val) - 1)) + '?'
        else:
            query = '?'
            # print(query)
        cursor.execute(f"INSERT INTO {table} values ({query})", val)
        sqlite_connection.commit()
        # print(f"Запись успешно вставлена в таблицу {table} ", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        # print(f"Error in connect sqlite {error} (wrt)")
        # print("Не удалось вставить данные в таблицу sqlite")
        # print("Класс исключения: ", error.__class__)
        # print("Исключение", error.args)
        # print("Печать подробноcтей исключения SQLite: ")
        # print()
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            # print("Close connection")


def sqlite_update_table(table: str, data_dic: dict):
    try:
        sqlite_connection = sqlite3.connect(db_name())
        cursor = sqlite_connection.cursor()
        # print('DB connect in SQLite')
        col = set()
        # val = set()
        val = []
        for key, values in data_dic.items():
            # print(key, values)
            col.add(key)
            # val.add(values)
            val.append(values)
        # print(val)
        if len(val) != 1:
            query = ('?,' * (len(val) - 1)) + '?'
        else:
            query = '?'
            # print(query)
        cursor.execute(f"INSERT OR REPLACE INTO {table} values ({query})", val)
        sqlite_connection.commit()
        # print(f"Запись успешно вставлена в таблицу {table} ", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        # print(f"Error in connect sqlite {error} (upd)")
        # print("Не удалось изменить данные в таблицу sqlite")
        # print("Класс исключения: ", error.__class__)
        # print("Исключение", error.args)
        # print("Печать подробноcтей исключения SQLite: ")
        # print()
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            # print("Close connection")


def sqlite_update_only(table: str, data_dic: dict):
    try:
        sqlite_connection = sqlite3.connect(db_name())
        cursor = sqlite_connection.cursor()
        # print('DB connect in SQLite')
        query = ''
        i = 0
        for key, values in data_dic.items():
            if i != len(data_dic):
                query = f"{query}{str(key)} = {str(values)},"
            else:
                query = f"{query}{str(key)} = {str(values)}"
            i += 1
        cursor.execute(f"UPDATE OR INSERT {table} SET {query} WHERE {id};")
        sqlite_connection.commit()
        # print(f"Запись успешно вставлена в таблицу {table} ", cursor.rowcount)
        cursor.close()
    except sqlite3.Error as error:
        # print(f"Error in connect sqlite {error} (upd)")
        # print("Не удалось изменить данные в таблицу sqlite")
        # print("Класс исключения: ", error.__class__)
        # print("Исключение", error.args)
        # print("Печать подробноcтей исключения SQLite: ")
        # print()
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            # print("Close connection")
