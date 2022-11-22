
from unittest import TestCase
class BMI(TestCase):
    @staticmethod
    def calc(w, h):
        if h == 0:
            raise ZeroDivisionError
        if h < 0 or w <= 0:
            return None
        return w/h**2
    @staticmethod
    def bmi(w, h):
        if BMI.calc(w, h) == None:
            return None
        if BMI.calc(w, h) < 18.5:
            return "Underweight"
        elif BMI.calc(w, h) > 25:
            return "Overweight"
        return "Good BMI"

    def test(self):
        w1, w2, w3 = 5, 0, -5
        h1, h2, h3 = 5, 10, 10
        excepted1, excepted2, excepted3 = 0.2, None, None
        actual1, actual2, actual3 = BMI.calc(w1, h1), BMI.calc(w2, h2), BMI.calc(w3, h3)
        self.assertEqual(actual1, excepted1)
        self.assertEqual(actual2, excepted2)
        self.assertEqual(actual3, excepted3)

        excepted1, excepted2, excepted3 = "Underweight", None, None
        actual1, actual2, actual3 = BMI.bmi(w1, h1), BMI.bmi(w2, h2), BMI.bmi(w3, h3)
        self.assertEqual(actual1, excepted1)
        self.assertEqual(actual2, excepted2)
        self.assertEqual(actual3, excepted3)


        w1, w2, w3 = 57, 80, 62
        h1, h2, h3 = 1.78, 1.5, 1.73
        excepted1, excepted2, excepted3 = "Underweight", "Overweight", "Good BMI"
        actual1, actual2, actual3 = BMI.bmi(w1, h1), BMI.bmi(w2, h2), BMI.bmi(w3, h3)
        self.assertEqual(excepted1, actual1)
        self.assertEqual(excepted2, actual2)
        self.assertEqual(excepted3, actual3)

if __name__ == '__main__':
    BMI.test()