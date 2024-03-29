import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
import pandas as pd
from PySide6.QtWidgets import QTableWidgetItem

class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])


# class MainWindow(QtWidgets.QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#
#         self.table = QtWidgets.QTableView()
#
#         data = pd.DataFrame([
#           [1, 9, 2],
#           [1, 0, -1],
#           [3, 5, 2],
#           [3, 3, 2],
#           [5, 8, 9],
#         ], columns = ['A', 'B', 'C'], index=['Row 1', 'Row 2', 'Row 3', 'Row 4', 'Row 5'])
#
#         self.model = TableModel(data)
#         self.table.setModel(self.model)
#
#         self.setCentralWidget(self.table)



class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.table = QtWidgets.QTableWidget()

        data = pd.DataFrame([
          [1, 9, 2],
          [1, 0, -1],
          [3, 5, 2],
          [3, 3, 2],
          [5, 8, 9],
        ], columns=['A', 'B', 'C'], index=['Row 1', 'Row 2', 'Row 3', 'Row 4', 'Row 5'])

        self. fill_table(data)
        self.setCentralWidget(self.table)

    def fill_table(self, data):
        self.table.setRowCount(data.shape[0])
        self.table.setColumnCount(data.shape[1])

        for i, column in enumerate(data.columns):
            for j, value in enumerate(data[column]):
                item = QTableWidgetItem(str(value))
                item.setFlags(item.flags() | Qt.ItemIsEditable)
                self.table.setItem(j, i, item)

            header_item = QTableWidgetItem(column)
            self.table.setHorizontalHeaderItem(i, header_item)

        for i, index in enumerate(data.index):
            header_item = QTableWidgetItem(index)
            self.table.setVerticalHeaderItem(i, header_item)


app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec()
