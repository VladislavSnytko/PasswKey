from PyQt5 import QtCore, QtGui, QtWidgets
import translations

hover_color = "#6a0203"
pressed_color = "#391e54"


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(455, 350)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("QFrame{\n"
                                 " border-radius: 10px;\n"
                                 " background-color: #2a232d;\n"
                                 "}")
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(20, 80, 391, 31))
        self.lineEdit.setStyleSheet("background-color: #22222e;\n"
                                    "border: 2px solid #a20995;\n"
                                    "border-radius: 10;\n"
                                    "color: white")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 120, 391, 31))
        self.lineEdit_2.setStyleSheet("background-color: #22222e;\n"
                                      "border: 2px solid #a20995;\n"
                                      "border-radius: 10;\n"
                                      "color: white")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 170, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "background-color: #252228;\n"
                                        "border: 2px solid rgb(25, 0, 25);\n"
                                        "    color: rgb(145, 145, 151);\n"
                                        "border-radius: 15;\n"
                                        "color: rgb(150, 100, 150)\n"
                                        "}\n"
                                        "QPushButton:hover{"
                                        "background-color: #3e2f40;"
                                        "}"
                                        "QPushButton:pressed{"
                                        " background-color: " + pressed_color + ";"
                                                                                "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 220, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "background-color: #252228;\n"
                                      "border: 2px solid rgb(25, 0, 25);\n"
                                      "    color: rgb(150, 100, 150);\n"
                                      "border-radius: 15;\n"
                                      "color: rgb(150, 100, 150)\n"
                                      "}\n"
                                      "QPushButton:hover{"
                                      "background-color: #3e2f40;"
                                      "}"
                                      "QPushButton:pressed{"
                                      " background-color: " + pressed_color + ";"
                                                                              "}"
                                      )
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 270, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "background-color: #252228;\n"
                                        "border: 2px solid rgb(25, 0, 25);\n"
                                        "border-radius: 15;\n"
                                        "color: rgb(150, 100, 150)\n"
                                        "}\n"
                                        "QPushButton:hover{"
                                        "background-color: #3e2f40;"
                                        "}"
                                        "QPushButton:pressed{"
                                        "background-color: #5d0003;"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(142, 20, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setStyleSheet("color: rgb(150, 100, 150)")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.frame)

        # Добавляем кнопку для свертывания окна
        self.pushButton_minimize = QtWidgets.QPushButton(self.frame)
        self.pushButton_minimize.setGeometry(QtCore.QRect(365, 5, 31, 31))
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

        # Подключаем обработчик события для кнопки свертывания окна
        self.pushButton_minimize.clicked.connect(Form.showMinimized)

        # Добавляем кнопку для закрытия приложения
        self.pushButton_close = QtWidgets.QPushButton(self.frame)
        self.pushButton_close.setGeometry(QtCore.QRect(395, 5, 31, 31))
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

        self.pushButton_ru = QtWidgets.QPushButton(self.frame)
        self.pushButton_ru.setGeometry(QtCore.QRect(10, 5, 31, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ru.setFont(font)
        self.pushButton_ru.setObjectName("pushButton_ru")

        # Добавляем иконку для кнопки свертывания окна
        ru_icon = QtGui.QIcon("images/icon_ru.png")
        self.pushButton_ru.setIcon(ru_icon)
        self.pushButton_ru.setIconSize(QtCore.QSize(41, 41))

        self.pushButton_ru.setStyleSheet("""
                    QPushButton {
                        background-color: transparent;
                        border: none;
                        border-left: 1px solid black;
                        border-right: 1px solid black;
                        border-top: none;
                        border-bottom: none;
                    }

            QPushButton:hover {
                background-color: #3A006E;
            }

            QPushButton:pressed {
                background-color: #2A0055;
            }
        """)

        self.pushButton_en = QtWidgets.QPushButton(self.frame)
        self.pushButton_en.setGeometry(QtCore.QRect(40, 5, 31, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        # Добавляем иконку для кнопки свертывания окна
        en_icon = QtGui.QIcon("images/icon_en.png")
        self.pushButton_en.setIcon(en_icon)
        self.pushButton_en.setIconSize(QtCore.QSize(41, 41))
        self.pushButton_en.setStyleSheet("""
                    QPushButton {
                        background-color: transparent;
                        border: none;
                        border-left: 1px solid black;
                        border-right: 1px solid black;
                        border-top: none;
                        border-bottom: none;
                    }

            QPushButton:hover {
                background-color: #3A006E;
            }

            QPushButton:pressed {
                background-color: #2A0055;
            }
        """)
        Form.resize(380, 370)
        self.label.setGeometry(QtCore.QRect(107, 35, 151, 41))
        self.pushButton_en.setGeometry(QtCore.QRect(35, 5, 31, 31))
        self.pushButton_ru.setGeometry(QtCore.QRect(5, 5, 31, 31))
        self.pushButton_minimize.setGeometry(QtCore.QRect(290, 5, 31, 31))
        self.pushButton_close.setGeometry(QtCore.QRect(320, 5, 31, 31))

        line_edit_width = 321  # Измените это значение в соответствии с шириной ваших строковых полей

        # Выравнивание первого строки ввода
        self.lineEdit.setGeometry(QtCore.QRect(20, 110, line_edit_width, 31))

        # Выравнивание второго строки ввода под первым
        self.lineEdit_2.setGeometry(
            QtCore.QRect(20, self.lineEdit.y() + self.lineEdit.height() + 10, line_edit_width, 31))

        # Выравнивание первой кнопки под вторым строковым полем
        self.pushButton_2.setGeometry(QtCore.QRect(30, self.lineEdit_2.y() + self.lineEdit_2.height() + 10, 301, 34))

        # Выравнивание второй кнопки под первой кнопкой
        self.pushButton.setGeometry(QtCore.QRect(30, self.pushButton_2.y() + self.pushButton_2.height() + 10, 301, 34))

        # Выравнивание третьей кнопки под второй кнопкой
        self.pushButton_3.setGeometry(QtCore.QRect(30, self.pushButton.y() + self.pushButton.height() + 10, 301, 34))

        # Добавляем разделитель
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(15, 91, 325, 2))
        self.line.setStyleSheet("background-color: black;")

        self.pushButton_hide_input = QtWidgets.QPushButton(self.frame)
        self.pushButton_hide_input.setGeometry(QtCore.QRect(313, 156, 21, 21))
        self.pushButton_hide_input.setObjectName("pushButton_hide_input")
        hide_input_icon = QtGui.QIcon("images/hide_icon.png")
        self.pushButton_hide_input.setIcon(hide_input_icon)
        self.pushButton_hide_input.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_hide_input.setStyleSheet("""
        QPushButton {
        background-color: transparent;
        border: none;
        width: 40px;
        height: 20px;
        }
        QPushButton:hover {
        background-color: rgba(0, 0, 0, 0.1);
        border-top: 1px solid white;
        border-bottom: 1px solid white;
        border-radius: 10px;
        }
        QPushButton:pressed {
        background-color: rgba(0, 0, 0, 0.2);
        }
        """)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/hide_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_hide_input.setIcon(icon)
        self.pushButton_hide_input.setIconSize(QtCore.QSize(20, 20))

        hover_icon = QtGui.QIcon()
        hover_icon.addPixmap(QtGui.QPixmap("images/hide_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_hide_input.setStyleSheet("""
        QPushButton {
        background-color: transparent;
        border: none;
        width: 40px;
        height: 20px;
        }
        QPushButton:hover {
        background-color: rgba(0, 0, 0, 0.1);
        border-top: 1px solid white;
        border-bottom: 1px solid white;
        border-radius: 10px;
        icon: url("images/hide_icon.png");
        }
        QPushButton:pressed {
        background-color: rgba(0, 0, 0, 0.2);
        icon: url("images/hide_icon.png");
        }
        """)
        self.pushButton_hide_input.clicked.connect(self.toggle_hide_input)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Authorization"))
        self.lineEdit.setPlaceholderText(
            _translate("Form", translations.translation["Login..."][translations.language]))
        self.lineEdit_2.setPlaceholderText(
            _translate("Form", translations.translation["Password..."][translations.language]))
        self.pushButton_2.setText(_translate("Form", translations.translation["Log in"][translations.language]))
        self.pushButton.setText(_translate("Form", translations.translation["Append user"][translations.language]))
        self.pushButton_3.setText(_translate("Form", translations.translation["Delete user"][translations.language]))
        self.label.setText(_translate("Form", translations.translation["LOG IN"][translations.language]))
        self.pushButton_en.setText(_translate("Form", ""))
        self.pushButton_ru.setText(_translate("Form", ""))

    def toggle_hide_input(self):
        if self.lineEdit_2.echoMode() == QtWidgets.QLineEdit.Normal:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        else:
            self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)

    offset = None

    def mousePressEvent(event):
        global offset
        if event.button() == QtCore.Qt.LeftButton:
            offset = event.pos()

    def mouseMoveEvent(event):
        global offset
        if offset is not None:
            new_pos = event.globalPos() - offset
            Form.move(new_pos)

    ui.frame.mousePressEvent = mousePressEvent
    ui.frame.mouseMoveEvent = mouseMoveEvent

    Form.show()
    sys.exit(app.exec_())