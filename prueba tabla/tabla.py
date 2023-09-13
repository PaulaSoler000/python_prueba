import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QLineEdit, \
                            QPushButton, QItemDelegate, QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QDoubleValidator

# https://www.youtube.com/watch?v=zrXFhHE-Ysg
# https://pandera.readthedocs.io/en/stable/fastapi.html
# https://saturncloud.io/blog/how-to-display-a-pandas-dataframe-in-an-existing-flask-html-table/

class FloatDelegate(QItemDelegate):
    def __init__(self, parent=None):
        super().__init__()

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setValidator(QDoubleValidator())
        return editor


class TableWidget(QTableWidget):
    def __init__(self, df):
        super().__init__()
        self.df = df
        self.setStyleSheet('font-size: 20px;')

        # set table dimension
        nRows, nColumns = self.df.shape
        self.setColumnCount(nColumns)
        self.setRowCount(nRows)

        self.setHorizontalHeaderLabels(('Col X', 'Col Y'))
        self.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.setItemDelegateForColumn(1, FloatDelegate())

        # data insertion
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                self.setItem(i, j, QTableWidgetItem(str(self.df.iloc[i, j])))

        self.cellChanged[int, int].connect(self.updateDF)

    def updateDF(self, row, column):
        text = self.item(row, column).text()
        self.df.iloc[row, column] = text


class DFEditor(QWidget):
    data = {
        'Col X': list('ABCD'),
        'col Y': [10, 20, 30, 40]
    }

    df = pd.DataFrame(data)

    def __init__(self):
        super().__init__()
        self.resize(800, 500)

        mainLayout = QVBoxLayout()

        self.table = TableWidget(DFEditor.df)
        mainLayout.addWidget(self.table)

        button_print = QPushButton('hacer print')
        button_print.setStyleSheet('font-size: 20px')
        button_print.clicked.connect(self.print_DF_Values)
        mainLayout.addWidget(button_print)

        button_export = QPushButton('Exportar a CSV')
        button_export.setStyleSheet('font-size: 20px')
        button_export.clicked.connect(self.export_to_csv)
        mainLayout.addWidget(button_export)

        self.setLayout(mainLayout)

    def print_DF_Values(self):
        print(self.table.df)

    def export_to_csv(self):
        self.table.df.to_csv('Data export.csv', index=False)
        print('CSV file exported.')


if __name__ == '__main__':
    app = QApplication([])

    demo = DFEditor()
    demo.show()

    app.exec_()
