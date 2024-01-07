from PyQt5 import QtCore, QtGui, QtWidgets
import translations
from explanatory_window import ExplanationWindow

hover_color = "#6a0203"
pressed_color = "#391e54"


class Ui_For(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(983, 373)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 981, 411))
        self.frame.setStyleSheet("QFrame{"
                                 " border-radius: 10px;"
                                 " background-color: #2a232d;"
                                 "}"
                                 )
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_back = QtWidgets.QPushButton(self.frame)
        self.pushButton_back.setGeometry(QtCore.QRect(5, 5, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setIcon(QtGui.QIcon("images/icon_back.png"))
        self.pushButton_back.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_back.setText("")
        self.pushButton_back.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                border-top: 1px solid black;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 1px solid black;
            }
            QPushButton:hover {
                background-color: rgb(100, 0, 100);
            }

            QPushButton:pressed {
                background-color: rgb(75, 0, 75);
            }
        """)
        self.pushButton_back.setObjectName("pushButton_back")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(220, 80, 541, 241))
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.setStyleSheet("background-color:#22222e;"
                                       "border: 3px solid rgb(25, 0, 25);"
                                       "border-radius: 10;"
                                       "color: rgb(184, 184, 184)")
        self.tableWidget.verticalScrollBar().setStyleSheet(
            "QScrollBar:vertical {"
            "    background-color: #22222e;"
            "    width: 15px;"
            "    margin: 1px 0px 1px 0px;"
            "}"
            "QScrollBar::handle:vertical {"
            "    background-color: #542a7f;"
            "    min-height: 30px;"
            "}"
            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {"
            "    height: 0px;"
            "    background-color: #542a7f;"
            "}"
            "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {"
            "    background: none;"
            "}"
        )
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(340, 20, 311, 51))
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setStyleSheet("color:rgb(150, 100, 150)")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 120, 201, 31))
        self.lineEdit.setStyleSheet("background-color: #22222e;"
                                    "border: 2px solid #a20995;"
                                    "border-radius: 12;"
                                    "color: white")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 160, 201, 31))
        self.lineEdit_2.setStyleSheet("background-color: #22222e;"
                                      "border: 2px solid #a20995;"
                                      "border-radius: 12;"
                                      "color: white")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_all_passw = QtWidgets.QPushButton(self.frame)
        self.pushButton_all_passw.setGeometry(QtCore.QRect(20, 250, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_all_passw.setFont(font)
        self.pushButton_all_passw.setStyleSheet("QPushButton{"
                                                " border: 2px solid rgb(25, 0, 25);"
                                                " background-color: #252428;"
                                                " color: rgb(84, 42, 127);"
                                                " border-radius: 15;"
                                                " color: rgb(150, 100, 150);"
                                                "}"
                                                "QPushButton:hover{"
                                                " background-color: #3e2f40;"
                                                "}"
                                                "QPushButton:pressed{"
                                                " background-color: " + pressed_color + ";"
                                                                                        "}")
        self.pushButton_all_passw.setObjectName("pushButton")
        self.pushButton_password_output = QtWidgets.QPushButton(self.frame)
        self.pushButton_password_output.setGeometry(QtCore.QRect(20, 210, 181, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_password_output.setFont(font)
        self.pushButton_password_output.setStyleSheet("QPushButton{"
                                                      " border: 2px solid rgb(25, 0, 25);"
                                                      " background-color: #252428;"
                                                      " color: rgb(84, 42, 127);"
                                                      " border-radius: 15;"
                                                      " color: rgb(150, 100, 150);"
                                                      "}"
                                                      "QPushButton:hover{"
                                                      " background-color: #3e2f40;"
                                                      "}"
                                                      "QPushButton:pressed{"
                                                      " background-color: " + pressed_color + ";"
                                                                                              "}"
                                                      )
        self.pushButton_password_output.setObjectName("pushButton_password_output")
        self.pushButton_append_password = QtWidgets.QPushButton(self.frame)
        self.pushButton_append_password.setGeometry(QtCore.QRect(790, 250, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_append_password.setFont(font)
        self.pushButton_append_password.setMouseTracking(False)
        self.pushButton_append_password.setTabletTracking(False)
        self.pushButton_append_password.setStyleSheet("QPushButton{"
                                                      "background-color: #252428;"
                                                      "border: 2px solid rgb(25, 0, 25);"
                                                      "border-radius: 15;"
                                                      "color: rgb(150, 100, 150)"
                                                      "}"
                                                      "QPushButton:hover{"
                                                      " background-color: #3e2f40;"
                                                      "}"
                                                      "QPushButton:pressed{"
                                                      " background-color: " + pressed_color + ";"
                                                                                              "}")
        self.pushButton_append_password.setObjectName("pushButton_append_password")
        self.service = QtWidgets.QLineEdit(self.frame)
        self.service.setGeometry(QtCore.QRect(770, 120, 201, 31))
        self.service.setStyleSheet("background-color: #22222e;"
                                   "border: 2px solid #a20995;"
                                   "border-radius: 12;"
                                   "color: white")
        self.service.setObjectName("service")
        self.login = QtWidgets.QLineEdit(self.frame)
        self.login.setGeometry(QtCore.QRect(770, 160, 201, 31))
        self.login.setStyleSheet("background-color: #22222e;"
                                 "border: 2px solid #a20995;"
                                 "border-radius: 12;"
                                 "color: white")
        self.login.setObjectName("login")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(770, 200, 201, 31))
        self.password.setStyleSheet("background-color: #22222e;"
                                    "border: 2px solid #a20995;"
                                    "border-radius: 12;"
                                    "color: white")
        self.password.setText("")
        self.password.setObjectName("password")
        self.pushButton_delete = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setStyleSheet("QPushButton{"
                                             "background-color: #252428;"
                                             "border: 2px solid rgb(25, 0, 25);"
                                             "border-radius: 17;"
                                             "color: rgb(150, 100, 150)"
                                             "}"
                                             "QPushButton:hover{"
                                             " background-color: #3e2f40;"
                                             "}"
                                             "QPushButton:pressed{"
                                             "background-color: #5d0003;"
                                             "}")
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_delete.setText("Delete")
        # Добавляем кнопку для свертывания окна
        self.pushButton_minimize = QtWidgets.QPushButton(self.frame)
        self.pushButton_minimize.setGeometry(QtCore.QRect(915, 5, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_minimize.setFont(font)
        self.pushButton_minimize.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                border-top: 1px solid black;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 1px solid black;
            }
            QPushButton:hover {
                background-color: rgb(100, 0, 100);
            }

            QPushButton:pressed {
                background-color: rgb(75, 0, 75);
            }
        """)
        self.pushButton_minimize.setObjectName("pushButton_minimize")

        # Добавляем иконку для кнопки свертывания окна
        minimize_icon = QtGui.QIcon("images/minimize_icon.png")
        self.pushButton_minimize.setIcon(minimize_icon)
        self.pushButton_minimize.setIconSize(QtCore.QSize(20, 20))
        # Добавляем разделитель
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 45, 984, 1))
        self.line.setStyleSheet("background-color: black;")

        # Подключаем обработчик события для кнопки свертывания окна
        self.pushButton_minimize.clicked.connect(Form.showMinimized)

        # Добавляем кнопку для закрытия приложения
        self.pushButton_close = QtWidgets.QPushButton(self.frame)

        self.pushButton_close.setGeometry(QtCore.QRect(945, 5, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                border-top: 1px solid black;
                border-bottom: 1px solid black;
                border-left: 1px solid black;
                border-right: 1px solid black;
            }
            QPushButton:hover {
                background-color: #FF9999;
            }
            QPushButton:pressed {
                background-color: #FF0000;
            }
        """)
        self.pushButton_close.setObjectName("pushButton_close")

        # Добавляем иконку для кнопки закрытия приложения
        close_icon = QtGui.QIcon("images/close_icon.png")
        self.pushButton_close.setIcon(close_icon)
        self.pushButton_close.setIconSize(QtCore.QSize(20, 20))

        # Подключаем обработчик события для кнопки закрытия приложения
        self.pushButton_close.clicked.connect(QtWidgets.QApplication.instance().quit)

        # кнопка сохранение изменений в таблице
        self.pushButton_save = QtWidgets.QPushButton(self.frame)
        self.pushButton_save.setGeometry(QtCore.QRect(490, 330, 101, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setStyleSheet("QPushButton{"
                                           "background-color: #252428;"
                                           "border: 2px solid rgb(25, 0, 25);"
                                           "border-radius: 17;"
                                           "color: rgb(150, 100, 150)"
                                           "}"
                                           "QPushButton:hover{"
                                           " background-color: #3e2f40;"
                                           "}"
                                           "QPushButton:pressed{"
                                           " background-color: " + pressed_color + ";"
                                                                                   "}")
        self.pushButton_save.setObjectName("pushButton_save")

        # кнопка пояснения
        self.explanation_button = QtWidgets.QPushButton(self.frame)
        self.explanation_button.setGeometry(QtCore.QRect(885, 5, 31, 31))
        self.explanation_button.setObjectName("pushButton_hide_input")
        hide_input_icon = QtGui.QIcon("images/hide_icon.png")
        self.explanation_button.setIcon(hide_input_icon)
        self.explanation_button.setIconSize(QtCore.QSize(20, 20))
        self.explanation_button.setStyleSheet("""
        QPushButton {
        background-color: transparent;
        border: none;
        width: 40px;
        height: 20px;
        }
        QPushButton:hover {
        background-color: rgba(0, 0, 0, 0.1);
        border-top: 1px solid black;
        border-bottom: 1px solid black;
        border-radius: 10px;
        }
        QPushButton:pressed {
        background-color: rgba(0, 0, 0, 0.2);
        }
        """)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/explanation_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.explanation_button.setIcon(icon)
        self.explanation_button.setIconSize(QtCore.QSize(20, 20))

        self.explanation_button.setStyleSheet("""
        QPushButton {
        background-color: transparent;
        border: none;
        width: 40px;
        height: 20px;
        }
        QPushButton:hover {
        background-color: rgba(0, 0, 0, 0.1);
        border-top: 1px solid black;
        border-bottom: 1px solid black;
        border-radius: 10px;
        icon: url("images/explanation_icon.png");
        }
        QPushButton:pressed {
        background-color: rgba(0, 0, 0, 0.2);
        icon: url("images/explanation_icon.png");
        }
        """)
        self.explanation_button.clicked.connect(self.show_explanation_window)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_save.setGeometry(QtCore.QRect(490, 357, 101, 34))
        self.pushButton_delete.setGeometry(QtCore.QRect(380, 357, 101, 34))
        self.password.setGeometry(QtCore.QRect(770, 230, 201, 31))
        self.service.setGeometry(QtCore.QRect(770, 150, 201, 31))
        self.pushButton_append_password.setGeometry(QtCore.QRect(790, 280, 161, 31))
        self.login.setGeometry(QtCore.QRect(770, 190, 201, 31))
        self.pushButton_password_output.setGeometry(QtCore.QRect(20, 240, 181, 31))
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 190, 201, 31))
        self.pushButton_all_passw.setGeometry(QtCore.QRect(20, 280, 181, 31))
        self.tableWidget.setGeometry(QtCore.QRect(220, 110, 541, 241))
        self.label.setGeometry(QtCore.QRect(340, 53, 311, 51))
        self.lineEdit.setGeometry(QtCore.QRect(10, 150, 201, 31))
        Form.resize(983, 412)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Изменение элементов"))
        self.pushButton_back.setText(_translate("Form", ""))
        self.label.setText(_translate("Form", translations.translation["Your passwords:"][translations.language]))
        self.lineEdit.setPlaceholderText(
            _translate("Form", translations.translation["Service..."][translations.language]))
        self.lineEdit_2.setPlaceholderText(
            _translate("Form", translations.translation["Login..."][translations.language]))
        self.pushButton_all_passw.setText(
            _translate("Form", translations.translation["Passwords by service"][translations.language]))
        self.pushButton_password_output.setText(
            _translate("Form", translations.translation["Password output"][translations.language]))
        self.pushButton_append_password.setText(
            _translate("Form", translations.translation["Append password"][translations.language]))
        self.service.setPlaceholderText(
            _translate("Form", translations.translation["Service..."][translations.language]))
        self.login.setPlaceholderText(_translate("Form", translations.translation["Login..."][translations.language]))
        self.password.setPlaceholderText(
            _translate("Form", translations.translation["Password..."][translations.language]))
        self.pushButton_delete.setText(
            _translate("Form", translations.translation["Delete password(s)"][translations.language]))
        self.pushButton_save.setText(
            _translate("Form", translations.translation["Save password(s)"][translations.language]))

    def show_explanation_window(self):
        self.explanation_window = ExplanationWindow()
        self.explanation_window.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    ui = Ui_For()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
