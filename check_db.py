from PyQt5 import QtCore

from handler.db_handler import *


class CheckThread(QtCore.QThread):
	mysignal = QtCore.pyqtSignal(str)

	def thr_login(self, name, passw):
		login(name, passw, self.mysignal)

	def thr_register(self, name, passw):
		register(name, passw, self.mysignal)

	def thr_delet(self, name, passw):
		delete(name, passw, self.mysignal)
