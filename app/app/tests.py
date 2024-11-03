from django.test import SimpleTestCase, TestCase
import app.calc as calc

class CalcTest(SimpleTestCase):

    def test_add(self):
        """testig additiong"""

        a, b = 2,2
        res = calc.add(a, b)
        self.assertEqual(res,4)
 
    def test_substract(self):
        """substracting numbers"""
        a, b = 5, 2
        res = calc.substract(a, b)
        self.assertEqual(res, 3)