import sqlite3
from handler import shifr
import translations as translations

global id_
languages = 'en'


def language_russ():
    global languages
    languages = 'ru'


def language_engl():
    global languages
    languages = 'en'


def login(login, passw, signal):
    shifr.decrypt()

    # Подключаемся к базе данных
    con = sqlite3.connect('handler/users.sqlite')
    cur = con.cursor()

    # Проверяем есть ли такой пользователь
    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == passw:
        global id_
        id_ = str(list(cur.execute(f'SELECT id FROM users WHERE name="{login}";'))[0][0])
        signal.emit(translations.translation['Успешная авторизация!'][languages])
    else:
        signal.emit(translations.translation['Проверьте правильность ввода данных!'][languages])

    cur.close()
    con.close()


    shifr.cipher()


def register(login, passw, signal):
    shifr.decrypt()

    # Подключаемся к базе данных
    con = sqlite3.connect('handler/users.sqlite')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    if value != []:
        signal.emit(translations.translation['Такой ник уже используется!'][languages])

    elif value == []:
        cur.execute(f"INSERT INTO users (name, password) VALUES ('{login}', '{passw}')")
        signal.emit(translations.translation['Вы успешно зарегистрированы!'][languages])
        con.commit()

    cur.close()
    con.close()

    shifr.cipher()


def delete(login, passw, signal):
    shifr.decrypt()

    # Подключаемся к базе данных
    con = sqlite3.connect('handler/users.sqlite')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE name="{login}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == passw:
        id = str(list(cur.execute(f'SELECT id FROM users WHERE name="{login}";'))[0][0])
        cur.execute(f"Delete From users where name = '{login}' and password = '{passw}'")
        cur.execute(f"""Delete From passw where id_user='{id}'""")
        signal.emit(translations.translation['Вы успешно удалены!'][languages])
        con.commit()
    else:
        signal.emit(translations.translation['Проверьте правильность ввода данных!'][languages])

    cur.close()
    con.close()

    shifr.cipher()
