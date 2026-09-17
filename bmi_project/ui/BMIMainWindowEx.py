
from Chapter5.bmi_project.classes.course import Course
from Chapter5.bmi_project.ui.BMIMainWindow import Ui_MainWindow


class BMIMainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalandSlot()
    def show_window(self):
        self.MainWindow.show()
    def setupSignalandSlot(self):
        self.pushButton.clicked.connect(self.invoke_bmi)
    def invoke_bmi(self):
        weight = float(self.lineEditWeight.text())
        height = float(self.lineEditHeight.text())
        b=Course(height,weight)

        bmi = b.calc_BMI()
        status=b.status()
        self.labelBMIresult.setText(str(round(bmi,2)))
        self.labelBMIresult_2.setText(str(status))