from PyQt5 import QtCore

from handler.db_handler_passw import append_password


class CheckThread1(QtCore.QThread):
	mysignal1 = QtCore.pyqtSignal(str)

	def thr_login1(self, id_, name_service, login1, passw1):
		append_password(id_, name_service, login1, passw1, self.mysignal1)


