from PyQt6.QtWidgets import QApplication, QMainWindow
from Chapter5.bmi_project.ui.BMIMainWindowEx import BMIMainWindowEx


app = QApplication([])

MainWindow = QMainWindow()

bmi_ui = BMIMainWindowEx()
bmi_ui.setupUi(MainWindow)
bmi_ui.show_window()

app.exec()