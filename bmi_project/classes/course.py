from socketserver import ThreadingMixIn


class Course:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def calc_BMI(self):
        bmi = self.weight / (self.height * self.height)
        return bmi
    def status(self):
        bmi=self.calc_BMI()
        if bmi < 18.5:
            return "Thin"
        if 18.5<bmi<24.9:
            return "Normal"
        if 25<bmi<29.9:
            return "Fat"
        if bmi>30:
            return "Obesity"
