import unittest
from bucket_functions.trigger import inbetween_days

class Test_functions(unittest.TestCase):
    def test_inbetween_days(self):
        date1 = "28/12/2020"
        date2 = "30/12/2020"
        date3 = "01/01/2021"
        answer1 = ["28-12-2020", "29-12-2020", "30-12-2020"]
        answer2 = ["30-12-2020", "31-12-2020", "01-01-2021"]
        answer3 = []
        self.assertEqual(inbetween_days(date1, date2), answer1)
        self.assertEqual(inbetween_days(date2, date3), answer2)
        self.assertEqual(inbetween_days(date3, date1), answer3)

if __name__ == '__main__':
    unittest.main()