import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from Chapter5.Ex82.ui.Ex82MainWindowEx import Ex82MainWindowEX

app=QApplication(sys.argv)
myui=Ex82MainWindowEX()
myui.setupUi(QMainWindow())
myui.show_window()
app.exec()