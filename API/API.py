import json
import time

import requests


def get_server_ip():
    return 'http://192.168.100.25:8008'


def get_token_out_sqlite():
    from SQLite.SQLite_CRUD_Querry.SQLite_Read import sqlite_read_col_in_table
    result = sqlite_read_col_in_table('token', 'token').replace('"', '')
    return result


def get_token(address: str, login: str, password: str):
    # print(f"login: {login} password: {password}")
    session = requests.post(f'{get_server_ip()}{address}', params={'username': login, 'password': password})
    print(session.text)
    print(session)
    return session.text


def get_data(address: str):
    aut = ("Bearer " + get_token_out_sqlite())
    headers = {"accept": "*/*",
               "Authorization": aut,
               "Content-Type": "application/json"}
    response = requests.get(f"{get_server_ip()}{address}", headers=headers)
    print(response.status_code)
    print(response.text)
    return response.text


def get_headers():
    t = get_token_out_sqlite()
    headers = {
        "Authorization": f"Bearer {t}",
        "Accept": "*/*",
        "Accept-Encoding": "gzip",
        "Content-Type": "application/json"}
    return headers


def get_headers_4_token():
    t = get_token_out_sqlite()
    aut = ("Bearer " + t)
    headers = {"accept": "*/*",
               "Authorization": aut,
               "Content-Type": "application/json"}
    # print(headers)
    return headers


def send_gps_driver(address: str, driver: int, lat: float, lon: float):
    print(f"lat: {lat} lon: {lon}")
    data = {
        "driverGeolocationId": 0,
        "latitude": lat,
        "longitude": lon,
        "driverId": driver}
    print(f"response: {data}")
    return send_request(f"{address}", data)


def send_request(address: str, data: str):
    # print(address)
    print(f"request: {get_server_ip()}{address}{json.dumps(data)}{get_headers_4_token()}")
    response = requests.post(f'{get_server_ip()}{address}', data=json.dumps(data), headers=get_headers_4_token())
    # response = requests.put(f'{get_server_ip()}{address}', data=data, headers=get_headers_4_token())
    print(response.status_code)
    print(f"response: {response.text}")
    print(time.time())
    return response.text


def login_request(address: str, login: str, password: str):
    # print(address)
    response = requests.post(f'{get_server_ip()}{address}?staffId={login}&password={password}',
                             headers=get_headers_4_token())
    # response = requests.put(f'{get_server_ip()}{address}', data=data, headers=get_headers_4_token())
    print(response.status_code)
    print(f"response: {response.text}")
    print(time.time())
    return response.text


def get_gps_driver(address: str, driver: str):
    session = requests.get(f'{get_server_ip()}{address}/{driver}', headers=get_headers())
    print(session)
    return session.text
