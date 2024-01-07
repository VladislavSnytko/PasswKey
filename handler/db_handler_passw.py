import sqlite3
from handler import shifr
import translations as translations

languages = 'en'


def language_russia():
    global languages
    languages = 'ru'


def language_english():
    global languages
    languages = 'en'


def append_password(id_, name_service, login1, passw1, signal1):
    shifr.decrypt()

    # Подключаемся к базе данных
    con = sqlite3.connect('handler/users.sqlite')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM passw WHERE id_user="{id_}" and service="{name_service}" and login="{login1}";')
    value1 = cur.fetchall()

    if value1 != []:
        signal1.emit(translations.translation['Такой логин уже есть!'][languages])

    elif value1 == []:
        cur.execute(f"""INSERT INTO passw (id_user, service, login, password)
        VALUES ('{id_}', '{name_service}', '{login1}', '{passw1}')""")

        phrase = translations.translation['Вы успешно добавили пароль от сервиса'][languages]
        signal1.emit(f'{phrase} {name_service}!')
        con.commit()

    cur.close()
    con.close()

    shifr.cipher()
