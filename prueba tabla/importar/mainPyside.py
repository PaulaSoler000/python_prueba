import os
import sys
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QTableWidget, QTableWidgetItem
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import pandas as pd

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        loader = QUiLoader()
        file = QFile("Main.ui")
        file.open(QFile.ReadOnly)
        self.ui = loader.load(file, self)
        file.close()

        self.ui.ButtonOpen.clicked.connect(self.OpenFile)
        self.ui.BtnDescribe.clicked.connect(self.dataHead)

    def OpenFile(self):
        try:
            path = QFileDialog.getOpenFileName(self, 'Open CSV', os.getenv('HOME'), 'CSV(*.csv)')[0]
            self.all_data = pd.read_csv(path)
        except:
            print(path)

    def dataHead(self):
        numColomn = self.ui.spinBox.value()
        if numColomn == 0:
            NumRows = len(self.all_data.index)
        else:
            NumRows = numColomn
        self.ui.tableWidget.setColumnCount(len(self.all_data.columns))
        self.ui.tableWidget.setRowCount(NumRows)
        self.ui.tableWidget.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(NumRows):
            for j in range(len(self.all_data.columns)):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()

app = QApplication(sys.argv)
sheet = MainWindow()
sheet.show()
sys.exit(app.exec_())