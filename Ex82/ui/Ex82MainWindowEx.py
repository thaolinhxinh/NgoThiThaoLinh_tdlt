from PyQt6.QtWidgets import QMessageBox

from Chapter5.Ex82.libs.MyModule import calculate_bill
from Chapter5.Ex82.ui.Ex82MainWindow import Ui_MainWindow


class Ex82MainWindowEX(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def show_window(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonCalc.clicked.connect(self.calculate_bill)
        self.pushButtonClose.clicked.connect(self.call_close_app)

    def calculate_bill(self):

        customer_name = self.lineEdiCustomerName.text()

        x = float(self.lineEditPrevious.text())
        y = float(self.lineEditCurrent.text())

        if self.radioButtonGroup1.isChecked():
            payment_type = 1
        elif self.radioButtonGroup2.isChecked():
            payment_type = 2

        result = calculate_bill(payment_type, x, y)

        self.textEditResult.setText(
            f"Customer name: {customer_name}\n"
            f"Payment type: {payment_type}\n"
            f"Previous month: {x} kWh\n"
            f"Current month: {y} kWh\n"
            f"Electricity used: {y - x} kWh\n"
            f"Total payment: {result:.2f}"
        )

    def call_close_app(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Exit confirmation?")
        msgBox.setText("Do you really want to exit?")
        msgBox.setIcon(QMessageBox.Icon.Question)

        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msgBox.setStandardButtons(buttons)

        ret = msgBox.exec()

        if ret == QMessageBox.StandardButton.Yes:
            exit(0)