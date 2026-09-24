from Chapter5.Ex73.libs.my_module import solving_program
from Chapter5.Ex73.ui.MyMainWindow import Ui_MainWindow



class MyMainWindowEx(Ui_MainWindow):
        def setupUi(self, MainWindow):
            super().setupUi(MainWindow)
            self.MainWindow = MainWindow  # de chung minh mainwindow dang cos ng dung de ko bi xoa
            self.setupSignalAndSlot()
            MainWindow.setFixedSize(800, 600)
        def show_window(self):
            self.MainWindow.show()

        def setupSignalAndSlot(self):
            self.pushButton.clicked.connect(self.solve_quanratic)
        def solve_quanratic(self):
            a=int(self.enterALineEdit.text())
            b=int(self.enterBLineEdit.text())
            c=int(self.enterCLineEdit.text())
            result=(solving_program(a,b,c))
            self.resultLineEdit.setText(str(result))


