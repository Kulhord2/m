# source of information https://www.youtube.com/watch?v=l8Imtec4ReQ&t=3615s
import datetime
import ipaddress
import platform

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, Clock
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.stacklayout import StackLayout
from kivy.uix.relativelayout import RelativeLayout

from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader
from plyer import battery
from plyer import tts
from plyer import gps
import requests
import random

from API import API

Builder.load_file("Authorization/authorization.kv")


def default_settings():
    from SQLite.SQLite_CRUD_Querry.SQLite_Update import sqlite_write_table
    from SQLite.SQLite_CRUD_Querry.SQLite_Read import sqlite_count
    if sqlite_count("settings") == 0:
        settings = dict()
        settings.update({'id': 1,
                         'login': '1',
                         'password': '2',
                         'text_size': 0.3,
                         'Check_internet': "http://www.google.com",
                         'Connect_login': "111",
                         'Connect_password': "222",
                         'Address1': "62.80.175.116",
                         'Address2': "80.91.189.6",
                         'Address3': "88.198.110.32",
                         'Address4': " "})
        print(settings)
        sqlite_write_table("settings", settings)


def random_gps(ln: int):
    return random.randint(1, 9999999) / (10 ** ln)


def update_gps_test(dt):
    print(gps)
    API.send_gps_driver("/api/DriverGeolocation", 28, 50 + random_gps(7), 30 + random_gps(7))


class SManager(ScreenManager):
    pass


class SLogin(Screen):
    pass


class STop(Screen):
    pass


class SSettings(Screen):
    pass


class SOrders(Screen):
    pass


class SEmployer(Screen):
    pass


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        # так выведем список заказов
        super().__init__(**kwargs)
        b = Button(text="txt2", size_hint=(0.2, 0.2))
        self.add_widget(b)


class LoginWidget1(RelativeLayout):
    write_login = ''
    write_password = ''

    def def_write_login(self, widget):
        self.write_login = widget.text
        print(self.write_login)

    def def_write_password(self, widget):
        self.write_password = widget.text
        print(self.write_password)

    def login_logistics(self):
        print('press')
        from SQLite.SQLite_CRUD_Querry.SQLite_Read import sqlite_read_col_in_table
        from SQLite.SQLite_CRUD_Querry.SQLite_Update import sqlite_update_only
        login = sqlite_read_col_in_table("settings", "login")
        password = sqlite_read_col_in_table("settings", "password")
        if login == '' and password == '':
            if self.write_login != '':
                login = self.write_login
            if self.write_password != '':
                password = self.write_password
        # print(login, password)
        response = API.send_request('/is_register', {"staffId": login, "password": password})
        # print(response)
        if response != "True":
            DelMiaApp.get_running_app().root.current = "Top"
            sqlite_update_only("settings", {"login": login, "password": password})
        else:
            error_text = "Не корректный логин или пароль"


class BoxLayoutExample(BoxLayout):
    from SQLite.SQLite_CRUD_Querry.SQLite_Read import sqlite_read_col_in_table
    from SQLite.SQLite_CRUD_Querry.SQLite_Create_Tables import create_table
    from SQLite.SQLite_CRUD_Querry.SQLite_Update import sqlite_write_table, sqlite_update_table
    from Module.Weather.GetWeather import weather
    first_open = False
    write_login = ''
    write_password = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.Scheduller()

    def Scheduller(self):
        # timer only second int or float
        # Clock.schedule_interval(self.update, 2)
        Clock.schedule_interval(update_gps_test, (60 * 0.5))
        if not self.first_open:
            Clock.schedule_interval(self.start_screen, 0.1)
        # 60 second * 9 minute
        Clock.schedule_interval(self.update_token, (60 * 1.5))

    def start_screen(self, dt):
        if not self.first_open:
            self.first_open = True
            from SQLite.SQLite_CRUD_Querry import SQLite_Read
            if SQLite_Read.sqlite_count("settings") != 0:
                login = SQLite_Read.sqlite_read_col_in_table("settings", "login")
                password = SQLite_Read.sqlite_read_col_in_table("settings", "password")
                # response = API.get_token('/is_register', login, password)
                # print(login, password)
                # print("resp", response)
                # if response == "True":
                #     DelMiaApp.get_running_app().root.current = "Top"

    def update_token(self, dt):
        from SQLite.SQLite_CRUD_Querry.SQLite_Update import sqlite_update_table
        from SQLite.SQLite_CRUD_Querry.SQLite_Read import sqlite_read_col_in_table
        dic_data = dict()
        token_logistics = API.get_token("/token",
                                        sqlite_read_col_in_table("settings", "Connect_login"),
                                        sqlite_read_col_in_table("settings", "Connect_password"))
        print("t",token_logistics)
        dic_data.update({'id': 0, 'token': token_logistics, 'datetime_write': datetime.datetime.now()})
        sqlite_update_table('token', dic_data)
        # print('All token: ', API.get_token_out_sqlite())
        # print('Begin 20 simbl token: ', API.get_token_out_sqlite()[:20])

    def employee_click(self):
        if self.employee_shift != 'Стать на смену':
            self.employee_shift = 'Стать на смену'
        else:
            self.employee_shift = 'Выйти со смены'

    def load_sound(self):
        SoundLoader.load("")

    def update_gps(self):
        self.connect_gps_status = f'GPS: ш({1}) д({2})'

    def update_server(self):
        self.connect_status_server = f'GPS: ш({1}) д({2})'

    def update_internet(self):
        self.connect_status_internet = f'GPS: ш({1}) д({2})'

    def check_iNet(l_url):
        if l_url != '':
            try:
                response = requests.get(l_url)
                return (f'{response.status_code}')
            except requests.ConnectionError:
                return ('')
        else:
            return ('')

    def check_if_ip_is_network(ip_address):
        if ip_address != '':
            try:
                ipaddress.ip_network(ip_address)
                print("true")
                return "on"
            except ValueError:
                print("false")
                return "off"
        else:
            print("false")
            return "off"

    def update(self, dt):
        print("upd")

    create_table()
    sqlite_write_table('weather', weather(50.4487081, 30.561708))
    update_token('', datetime.datetime.now())
    default_settings()
    # закинуть в конфиг
    net = "http://www.google.com"
    if check_iNet(sqlite_read_col_in_table("settings", "Check_internet")) != '':
        int_st = 'on'
    else:
        int_st = 'off'

    # закинуть в конфиг 2 ип
    if (check_if_ip_is_network(sqlite_read_col_in_table("settings", "Address1")) == 'on'):
        serv_st = 'on(1)'
    elif (check_if_ip_is_network(sqlite_read_col_in_table("settings", "Address2")) == 'on'):
        serv_st = 'on(2)'
    elif (check_if_ip_is_network(sqlite_read_col_in_table("settings", "Address3")) == 'on'):
        serv_st = 'on(3)'
    else:
        serv_st = 'off'
    if platform.platform() == 'android':
        btry = battery.status
    else:
        btry = '0%'

    glat = 50.4487081
    glon = 30.561708
    weather(glat, glon)
    print(sqlite_read_col_in_table('weather', 'temp'))
    weather_now = StringProperty(f"{sqlite_read_col_in_table('weather', 'temp')} \u00b0C")
    employee_shift = StringProperty(f'Стать на смену')
    connect_gps_status = StringProperty(f'GPS: ш({glat}) д({glon})')
    connect_status_server = StringProperty(f'Status: {gps}')
    connect_status_internet = StringProperty(f'Internet: {int_st}')
    battery_status = StringProperty(f'Battery: {btry}')

    print(sqlite_read_col_in_table('weather', 'temp'))
    # print()
    # print('(1)GPS driver: ', API.get_gps_driver('/api/DriverGeolocation', '2'))
    # print(API.send_gps_driver('/api/DriverGeolocation', '2', glat, glat))
    # print('(2)GPS driver: ', API.get_gps_driver('/api/DriverGeolocation', '2'))


class DelMiaApp(App):
    pass


if __name__ == "__main__":
    DelMiaApp().run()
