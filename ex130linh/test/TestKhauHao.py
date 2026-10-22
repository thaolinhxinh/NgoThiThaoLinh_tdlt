from PyQt6.QtWidgets import QApplication, QMainWindow
from ex130linh.ui.KhauHaoMainWindowEx import KhauHaoMainWindowEx

app = QApplication([])
window = QMainWindow()
ui = KhauHaoMainWindowEx()
ui.setupUi(window)
ui.show_window()
app.exec()
