import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
data = {}


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('des.ui', self)
        self.result = []
        self.maxID = 0
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Фильмотека')
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'])
        self.tableWidget.setRowCount(0)
        con = sqlite3.connect("films_db.sqlite")
        cur = con.cursor()
        res = list(cur.execute("""SELECT * FROM films"""))
        a = {i[0]: i[1] for i in cur.execute("""select * FROM genres""")}

        for i in range(len(res)):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j in range(len(res[i])):
                if j == 3:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(a[res[i][j]]))
                else:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(res[i][j])))

        con.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
