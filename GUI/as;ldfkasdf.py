from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import random
import sys

def build_mock_data(num_keys, num_rows=4, num_columns=3):
    result = {}
    key = "key"
    build_row = lambda: [random.randint(0,10) for _ in range(num_columns)]
    for i in range(num_keys):
        result[key+str(i)] = [build_row() for _ in range(num_rows)]
    return result

mock_data = build_mock_data(10)

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        super(TableModel, self).__init__(parent)
        self._data = data
        # defualt key
        self.dict_key = 'key0'

    def set_key(self, key):
        self.beginResetModel()
        self.dict_key = key
        self.endResetModel()

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self._data[self.dict_key])

    def columnCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self._data[self.dict_key][0])

    def data(self, QModelIndex, int_role=None):
        row = QModelIndex.row()
        column = QModelIndex.column()
        if int_role == QtCore.Qt.DisplayRole:
            return str(self._data[self.dict_key][row][column])

class ListModel(QtCore.QAbstractListModel):
    def __init__(self, data, parent=None):
        super(ListModel, self).__init__(parent)
        self._data = sorted(data.keys())

    def list_clicked(self, index):
        row = index.row()
        key = self._data[row]
        table_model.set_key(key)

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return len(self._data)

    def data(self, QModelIndex, int_role=None):
        row = QModelIndex.row()
        if int_role == QtCore.Qt.DisplayRole:
            return str(self._data[row])

    def flags(self, QModelIndex):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable


#########################################
# temporary just to get above code to run
app = QtWidgets.QApplication(sys.argv)

list_view = QListView()
list_model = ListModel(mock_data)
list_view.setModel(list_model)
list_view.clicked.connect(list_model.list_clicked)
list_view.show()

table_view = QTableView()
table_model = TableModel(mock_data)
table_view.setModel(table_model)
table_view.show()

sys.exit(app.exec_())