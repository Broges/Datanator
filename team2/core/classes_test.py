import unittest
from basket import Basket
from transaction import Transaction

class Test_data_classes(unittest.TestCase):
    
    def test_Basket(self):

        test_Basket = Basket(1, 1, "Regular Flavoured hot chocolate - Hazelnut", 2.6)

        expected_basket_id = 1
        expected_transaction_id = 1
        expected_basket_item = "Regular Flavoured hot chocolate - Hazelnut"
        expected_price = 2.6

        self.assertEqual(test_Basket.basket_id, expected_basket_id)
        self.assertEqual(test_Basket.transaction_id, expected_transaction_id)
        self.assertEqual(test_Basket.basket_item, expected_basket_item)
        self.assertEqual(test_Basket.price, expected_price)

    def test_Transaction(self):
        test_Transaction = Transaction(1, "Isle of Wight", "Paul Kifer", "29/09/2020 09:00", 5)

        transaction_id = 1
        location = "Isle of Wight"
        customer_name = "Paul Kifer"
        date = "29/09/2020 09:00"
        pay_amount = 5.00

        self.assertEqual(test_Transaction.transaction_id, transaction_id)
        self.assertEqual(test_Transaction.location, location)
        self.assertEqual(test_Transaction.customer_name, customer_name)
        self.assertEqual(test_Transaction.date, date)
        self.assertEqual(test_Transaction.pay_amount, pay_amount)

if __name__ == '__main__':
    unittest.main()