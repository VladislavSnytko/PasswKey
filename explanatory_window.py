import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import translations


class ExplanationWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(translations.translation["Explanation"][translations.language])

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setStyleSheet("""
            QFrame {
                background-color: #2a232d;
                border-radius: 10px;
            }

            QPushButton:hover {
                background-color: rgb(100, 0, 100);
            }

            QPushButton:pressed {
                background-color: rgb(75, 0, 75);
            }
        """)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 200, 600, 150))

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setText(translations.translation["Explanation of button operation:"][translations.language] + ' ' +
                           translations.translation["Save password(s),"][translations.language] +
                           translations.translation[" Delete password(s)"][translations.language])
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #69456b;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setGeometry(QtCore.QRect(0, 5, 515, 35))

        self.label_text = QtWidgets.QLabel(self.frame)
        self.label_text.setText(translations.translation[
                                    'Сохранить пароль(и) - эта кнопка сохраняет измененный пароль(и) в таблице вывода паролей.'
                                    'Удалить пароль(и) - данная кнопка удаляет выбранный пароль(и) из таблицы вывода паролей.'][
                                    translations.language])
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_text.setFont(font)
        self.label_text.setStyleSheet("color: rgb(150, 100, 150);")
        self.label_text.setAlignment(QtCore.Qt.AlignCenter)
        self.label_text.setGeometry(QtCore.QRect(10, 55, 560, 100))

        self.pushButton_minimize = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_minimize.setFont(font)
        self.pushButton_minimize.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                border-top: 1px solid rgb(25, 0, 25);
                border-bottom: 1px solid rgb(25, 0, 25);
                border-left: 1px solid rgb(25, 0, 25);
                border-right: 1px solid rgb(25, 0, 25);
            }
            QPushButton:hover {
                background-color: rgb(100, 0, 100);
            }
            QPushButton:pressed {
                background-color: rgb(75, 0, 75);
            }
        """)

        self.pushButton_minimize.setObjectName("pushButton_minimize")

        minimize_icon = QtGui.QIcon("images/minimize_icon.png")
        self.pushButton_minimize.setIcon(minimize_icon)
        self.pushButton_minimize.setIconSize(QtCore.QSize(20, 20))

        self.pushButton_minimize.clicked.connect(self.showMinimized)

        self.pushButton_close = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                border-top: 1px solid rgb(25, 0, 25);
                border-bottom: 1px solid rgb(25, 0, 25);
                border-left: 1px solid rgb(25, 0, 25);
                border-right: 1px solid rgb(25, 0, 25);
            }
            QPushButton:hover {
                background-color: rgb(255, 153, 153);
            }
            QPushButton:pressed {
                background-color: rgb(255, 0, 0);
            }
        """)

        self.pushButton_close.setObjectName("pushButton_close")

        close_icon = QtGui.QIcon("images/close_icon.png")
        self.pushButton_close.setIcon(close_icon)
        self.pushButton_close.setIconSize(QtCore.QSize(20, 20))

        self.pushButton_close.clicked.connect(self.close)

        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(0, 45, 984, 1))
        self.line.setStyleSheet("background-color: rgb(25, 0, 25);")

        self.pushButton_close.setGeometry(QtCore.QRect(560, 5, 31, 31))
        self.pushButton_minimize.setGeometry(QtCore.QRect(530, 5, 31, 31))

        self.center_window()

        self.drag_start_position = None
        self.window_position = None

    def center_window(self):
        screen_geometry = QtWidgets.QApplication.desktop().screenGeometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drag_start_position = event.globalPos()
            self.window_position = self.frameGeometry().topLeft()

    def mouseMoveEvent(self, event):
        if self.drag_start_position:
            delta = event.globalPos() - self.drag_start_position
            self.move(self.window_position + delta)

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drag_start_position = None
            self.window_position = None


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ExplanationWindow()
    window.show()
    sys.exit(app.exec_())
