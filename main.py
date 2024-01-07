import sys

from PyQt5 import QtWidgets

import handler.db_handler as h
import handler.db_handler_passw as hand_pass
from control_window import Ui_For
from check_db import *
from check_db_password import *
from log_in import Ui_Form
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QStyledItemDelegate
import translations

log_in = ['Успешная авторизация!', 'Successful authorization!']


class FirstRowDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super().initStyleOption(option, index)

        # Проверяем, является ли строка первой
        if index.row() == 0:
            option.palette.setColor(option.palette.Text, QtGui.QColor(255, 255, 255))  # Цвет текста первой строки
            option.palette.setColor(option.palette.Highlight, QtGui.QColor(255, 0, 0))  # Цвет выделения первой строки
            option.palette.setColor(option.palette.HighlightedText,
                                    QtGui.QColor(255, 255, 255))  # Цвет текста выделения первой строки


class CustomMessageBox(QDialog):
    def __init__(self, title, message):
        super().__init__()
        self.setWindowTitle(title)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        label = QLabel(message)
        label.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")

        ok_button = QPushButton("OK")
        ok_button.setStyleSheet(
            "QPushButton { background-color: #9f0830; color: white;"
            " border: none; border-radius: 5px; padding: 8px 16px; font-size: 16px; }"
            "QPushButton:hover { background-color: #6a0203; }"
            "QPushButton:pressed { background-color: #4f021e; }")
        ok_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(ok_button)
        layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(layout)


class InterfaceSystem(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        offset = None

        def mousePressEvent(event):
            global offset
            if event.button() == QtCore.Qt.LeftButton:
                offset = event.globalPos() - mywin.pos()

        def mouseMoveEvent(event):
            global offset
            if offset is not None:
                new_pos = event.globalPos() - offset
                if new_pos.x() < 0:
                    new_pos.setX(0)
                if new_pos.y() < 0:
                    new_pos.setY(0)
                if new_pos.x() + mywin.width() > QtWidgets.QDesktopWidget().availableGeometry().width():
                    new_pos.setX(QtWidgets.QDesktopWidget().availableGeometry().width() - mywin.width())
                if new_pos.y() + mywin.height() > QtWidgets.QDesktopWidget().availableGeometry().height():
                    new_pos.setY(QtWidgets.QDesktopWidget().availableGeometry().height() - mywin.height())
                mywin.move(new_pos)

        self.ui.frame.mousePressEvent = mousePressEvent
        self.ui.frame.mouseMoveEvent = mouseMoveEvent

        self.ui.pushButton.clicked.connect(self.reg)
        self.ui.pushButton_2.clicked.connect(self.auth)
        self.ui.pushButton_3.clicked.connect(self.del_)
        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]
        self.ui.pushButton_ru.clicked.connect(self.language_rus)
        self.ui.pushButton_en.clicked.connect(self.language_eng)

        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

    def language_rus(self):
        translations.language_ru()
        h.language_russ()
        hand_pass.language_russia()
        self.update_window()

    def language_eng(self):
        translations.language_en()
        h.language_engl()
        hand_pass.language_english()
        self.update_window()

    def update_window(self):
        self.ui.retranslateUi(self)

    # Проверка правильности ввода
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    # Обработчик сигналов
    def signal_handler(self, value):
        custom_message_box = CustomMessageBox(translations.translation['Оповещение'][translations.language],
                                              value)
        custom_message_box.exec_()
        if value in log_in:
            open_Append_Window()

    @check_input
    def auth(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_login(name, passw)

    @check_input
    def reg(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_register(name, passw)

    @check_input
    def del_(self):
        name = self.ui.lineEdit.text()
        passw = self.ui.lineEdit_2.text()
        self.check_db.thr_delet(name, passw)


class AppendPasswordWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui2 = Ui_For()
        self.ui2.setupUi(self)

        offset = None

        def mousePressEvent(event):
            global offset
            if event.button() == QtCore.Qt.LeftButton:
                offset = event.globalPos() - AppendWindow.pos()

        def mouseMoveEvent(event):
            global offset
            if offset is not None:
                new_pos = event.globalPos() - offset
                if new_pos.x() < 0:
                    new_pos.setX(0)
                if new_pos.y() < 0:
                    new_pos.setY(0)
                if new_pos.x() + AppendWindow.width() > QtWidgets.QDesktopWidget().availableGeometry().width():
                    new_pos.setX(QtWidgets.QDesktopWidget().availableGeometry().width() - AppendWindow.width())
                if new_pos.y() + AppendWindow.height() > QtWidgets.QDesktopWidget().availableGeometry().height():
                    new_pos.setY(QtWidgets.QDesktopWidget().availableGeometry().height() - AppendWindow.height())
                AppendWindow.move(new_pos)

        self.ui2.frame.mousePressEvent = mousePressEvent
        self.ui2.frame.mouseMoveEvent = mouseMoveEvent

        self.dataChanged = False

        self.ui2.pushButton_save.clicked.connect(self.saveChanges)
        self.ui2.pushButton_append_password.clicked.connect(self.auth1)

        self.check_db1 = CheckThread1()
        self.check_db1.mysignal1.connect(self.signal_handler1)

        # Базы для проверки правильности ввода
        self.base_line_edit1 = [self.ui2.lineEdit_2, self.ui2.lineEdit]
        self.base_line_edit2 = [self.ui2.lineEdit]

        # База для проверки правильности ввода добавления пароля
        self.base_line_append = [self.ui2.service, self.ui2.login, self.ui2.password]

        self.ui2.pushButton_back.clicked.connect(self.return_t)
        self.ui2.pushButton_password_output.clicked.connect(self.conclusion_password)
        self.ui2.pushButton_all_passw.clicked.connect(self.conclusion_all)
        self.ui2.pushButton_delete.clicked.connect(self.deleteSelectedRows)
        self.flag_login = False
        self.flag_service = False

    # Возврат к первому окну
    def return_t(self):
        AppendWindow.close()
        mywin.show()

    # Проверка правильности ввода
    def check_append(funct1):
        def wrapper1(self):
            for line_edit1 in self.base_line_append:
                if len(line_edit1.text()) == 0 or len(line_edit1.text().split()) == 0:
                    return
            funct1(self)

        return wrapper1

    # Проверка правильности ввода сервиса и логина
    def check_del(funct1):
        def wrapper1(self):
            for line_edit1 in self.base_line_edit1[:2]:
                if len(line_edit1.text()) == 0:
                    return
            funct1(self)

        return wrapper1

    # Проверка правильности ввода сервиса
    def check_del_all(funct1):
        def wrapper1(self):
            for line_edit1 in self.base_line_edit1[:1]:
                if len(line_edit1.text()) == 0:
                    return
            funct1(self)

        return wrapper1

    def signal_handler1(self, value1):
        custom_message_box = CustomMessageBox(translations.translation['Оповещение'][translations.language], value1)
        custom_message_box.exec_()

    @check_append
    def auth1(self):
        name_service = self.ui2.service.text()
        login1 = self.ui2.login.text()
        passw1 = self.ui2.password.text()
        self.check_db1.thr_login1(h.id_, name_service, login1, passw1)
        self.ui2.retranslateUi(self)

    # Проверка правильности ввода сервиса и логина
    def check_input_login_service(funct1):
        def wrapper1(self):
            for line_edit1 in self.base_line_edit1:
                if len(line_edit1.text()) == 0:
                    return
            funct1(self)

        return wrapper1

    # Проверка правильности ввода сервиса
    def check_input_service(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit2:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    def deleteSelectedRows(self):
        selected_rows = self.ui2.tableWidget.selectedItems()
        if len(selected_rows) > 0:
            unique_rows = set(item.row() for item in selected_rows)
            sorted_rows = sorted(unique_rows, reverse=True)  # Сортируем в обратном порядке, чтобы удалить с конца
            for row in sorted_rows:
                item = self.ui2.tableWidget.item(row, 0)
                service = item.text()  # Получаем значение из первой ячейки строки
                item = self.ui2.tableWidget.item(row, 1)
                login = item.text()  # Получаем значение из второй ячейки строки
                item = self.ui2.tableWidget.item(row, 2)
                password = item.text()  # Получаем значение из второй ячейки строки

                # Подключаемся к базе данных
                shifr.decrypt()

                con = sqlite3.connect('handler/users.sqlite')
                cur = con.cursor()

                if service != 'Service' and service != 'Сервис' and login != 'Логин' and login != 'Login':
                    # Выполняем SQL-запрос для удаления элемента
                    cur.execute("DELETE FROM passw WHERE service=? AND login=? AND password=?",
                                (service, login, password))
                    con.commit()
                    # Удаляем строку из таблицы
                    self.ui2.tableWidget.removeRow(row)

                # Закрываем соединение с базой данных
                cur.close()
                con.close()
                shifr.cipher()

        else:
            custom_message_box = CustomMessageBox(translations.translation['Оповещение'][translations.language],
                                                  translations.translation['Выберите пароль(и) для удаления!'][
                                                      translations.language])
            custom_message_box.exec_()

    def saveChanges(self):
        serv = ' '
        login = ' '
        # Получаем данные из таблицы
        num_rows = self.ui2.tableWidget.rowCount()
        num_cols = self.ui2.tableWidget.columnCount()
        data = []
        for row in range(num_rows):
            row_data = []
            for col in range(num_cols):
                item = self.ui2.tableWidget.item(row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("")
            data.append(row_data)
        for row in data:
            serv = row[0]
            login = row[1]

        # Получаем данные из оригинальной таблицы в базе данных
        original_data = self.getOriginalTableData(serv, login)

        # Сравниваем данные с оригинальной таблицей
        if (data[1:] != original_data) and original_data:
            # Подключаемся к базе данных
            shifr.decrypt()
            con = sqlite3.connect('handler/users.sqlite')
            cur = con.cursor()

            # Обновляем данные в базе данных
            for row in data:
                service = row[0]
                login = row[1]
                password = row[2]
                cur.execute("UPDATE passw SET password=? WHERE id_user=? AND service=? AND login=?",
                            (password, h.id_, service, login))
            con.commit()

            # Закрываем соединение с базой данных
            cur.close()
            con.close()
            shifr.cipher()
            custom_message_box = CustomMessageBox(translations.translation['Оповещение'][translations.language],
                                                  translations.translation['Изменения сохранены'][
                                                      translations.language])
            custom_message_box.exec_()
        else:
            custom_message_box = CustomMessageBox(translations.translation['Оповещение'][translations.language],
                                                  translations.translation['Нет изменений для сохранения'][
                                                      translations.language])
            custom_message_box.exec_()

    def getOriginalTableData(self, serv, login):

        # Подключаемся к базе данных
        shifr.decrypt()
        con = sqlite3.connect('handler/users.sqlite')
        cur = con.cursor()

        # Получаем данные из оригинальной таблицы в базе данных
        if self.flag_login:
            cur.execute("SELECT * FROM passw WHERE service=? and id_user=? and login=?", (serv, h.id_, login))
        elif self.flag_service:
            cur.execute("SELECT * FROM passw WHERE service=? and id_user=?", (serv, h.id_))
        original_data = cur.fetchall()
        if original_data:
            original_data = [list(i)[1:] for i in original_data]
        # Закрываем соединение с базой данных
        cur.close()
        con.close()
        shifr.cipher()

        return original_data

    # Вывод по одному паролю
    @check_input_login_service
    def conclusion_password(self):
        self.flag_login = True
        self.flag_service = False
        # Расшифровываем базу данных
        shifr.decrypt()

        # Подключаемся к базе данных
        con = sqlite3.connect('handler/users.sqlite')
        cur = con.cursor()
        service = self.ui2.lineEdit.text()
        login = self.ui2.lineEdit_2.text()

        # Получили результат запроса, который выводим в таблицу
        que = f"""SELECT service, login, password FROM passw WHERE id_user='{h.id_}' and service='{service}'
    		and login='{login}'"""
        result = [('Service', 'Login', 'Password')] + cur.execute(que).fetchall()

        if result[1:] == []:
            custom_message_box = CustomMessageBox(translations.translation['Оповещение'][translations.language],
                                                  translations.translation['Такого логина нет!'][translations.language])
            custom_message_box.exec_()
            self.ui2.lineEdit_2.clear()  # Очищаем текст в QLineEdit
        else:
            # Заполнили размеры таблицы
            self.ui2.tableWidget.setRowCount(len(result))
            self.ui2.tableWidget.setColumnCount(len(result[0]))

            # Установили политику изменения размера ячеек
            self.ui2.tableWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

            # Заполнили таблицу полученными элементами
            non_editable_columns = [0, 1]  # Индексы столбцов "Service" и "Login", которые делаем нередактируемыми

            # Заполнили таблицу полученными элементами
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    item = QtWidgets.QTableWidgetItem(str(val))
                    self.ui2.tableWidget.setItem(i, j, item)

                    # Настройка цвета текста и границ для первой строки
                    if i == 0:
                        item.setForeground(QtGui.QColor(105, 79, 108))  # Цвет текста первой строки
                        item.setBackground(QtGui.QColor(34, 28, 36))  # Цвет фона первой строки

                    # Установка флага редактирования для ячеек, кроме тех, что в non_editable_columns
                    if j not in non_editable_columns and item.text() != 'Password' and item.text() != 'Пароль':
                        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
                    else:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
            # Равномерное распределение ширины колонок
            header = self.ui2.tableWidget.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        cur.close()
        con.close()

        # Шифруем базу данных
        shifr.cipher()

    # Вывод всех поролей
    @check_input_service
    def conclusion_all(self):
        self.flag_service = True
        self.flag_login = False
        # Расшифровываем базу данных
        shifr.decrypt()

        # Подключаемся к базе данных
        con = sqlite3.connect('handler/users.sqlite')
        cur = con.cursor()
        service = self.ui2.lineEdit.text()

        # Получили результат запроса, который выводим в таблицу
        que = f"""SELECT service, login, password FROM passw WHERE id_user='{h.id_}' and service='{service}'"""
        serv = translations.translation['Service'][translations.language]
        log = translations.translation['Login'][translations.language]
        passw = translations.translation['Password'][translations.language]
        result = [(serv, log, passw)] + cur.execute(que).fetchall()

        if result[1:] == []:
            custom_message_box = CustomMessageBox(translations.translation['Оповещение'][translations.language],
                                                  translations.translation['Такого сервиса нет!'][
                                                      translations.language])
            custom_message_box.exec_()

        else:

            # Заполнили размеры таблицы
            self.ui2.tableWidget.setRowCount(len(result))
            self.ui2.tableWidget.setColumnCount(len(result[0]))

            # Установили политику изменения размера ячеек
            self.ui2.tableWidget.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

            # Заполнили таблицу полученными элементами
            non_editable_columns = [0, 1]  # Индексы столбцов "Service" и "Login", которые делаем нередактируемыми

            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    item = QtWidgets.QTableWidgetItem(str(val))
                    self.ui2.tableWidget.setItem(i, j, item)

                    # Настройка цвета текста и границ для первой строки
                    if i == 0:
                        item.setForeground(QtGui.QColor(105, 79, 108))  # Цвет текста первой строки
                        item.setBackground(QtGui.QColor(34, 28, 36))  # Цвет фона первой строки

                    # Установка флага редактирования для ячеек, кроме тех, что в non_editable_columns
                    if j not in non_editable_columns and item.text() != 'Password' and item.text() != 'Пароль':
                        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
                    else:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                        if item.text() != 'Service' \
                                and item.text() != 'Password' \
                                and item.text() != 'Пароль' \
                                and item.text() != 'Сервис' \
                                and item.text() != 'Login'\
                                and item.text() != 'Логин':
                            item.setForeground(QtGui.QBrush(QtGui.QColor(128, 128, 128)))

            # Равномерное распределение ширины колонок
            header = self.ui2.tableWidget.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        cur.close()
        con.close()

        # Шифруем базу данных
        shifr.cipher()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mywin = InterfaceSystem()
    mywin.show()
    AppendWindow = AppendPasswordWindow()


    def open_Append_Window():
        global AppendWindow
        AppendWindow = AppendPasswordWindow()
        AppendWindow.show()
        mywin.close()


    sys.exit(app.exec_())
