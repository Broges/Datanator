import unittest
from test4 import Basket

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

if __name__ == '__main__':
    unittest.main()