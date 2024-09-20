from django.test import SimpleTestCase, TestCase
import app.calc as calc

class CalcTest(SimpleTestCase):

    def test_add(self):
        """testig additiong"""

        a, b = 2,2
        res = calc.add(a, b)
        self.assertEqual(res,3)

