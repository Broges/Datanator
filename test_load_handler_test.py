# import unittest
# from file_handling import *

# class TestPerson(unittest.TestCase):
#     def test_person(self):
#         expected_drink_brand = "J2O"
#         expected_drink_flavour = "Orange"
#         expected_drink_volume = "275ml"
#         container = Drink("J2O", "Orange", "275ml")
#         self.assertEqual(container.brand, expected_drink_brand)
#         self.assertEqual(container.flavour, expected_drink_flavour)
#         self.assertEqual(container.volume, expected_drink_volume)


a = "[[1, \"Croydon_11/10/2020_trans_1\", \"Regular Flavoured hot chocolate - Caramel\", 2.6], [2, \"Croydon_11/10/2020_trans_1\", \" Frappes - Strawberries & Cream\", 2.75]]"
b = "[['Croydon_11/10/2020_trans_231', 'Croydon', 'David Cottrell', '11/10/2020 09:43', 3.55], ['Croydon_11/10/2020_trans_232', 'Croydon', 'David Mcmullen', '11/10/2020 09:44', 5.45]]"

# bigData = b[2:-2]
# items = bigData.split('], [')
# x = 0
# for i in items:
#     p = i.split(',')
# if len(p) == 4:
#     print('basket') #here we'll do basket steps
# elif len(p) == 5:
#     print('transaction')#here we'll do transaction steps
    

bigData = a[2:-2]

items = bigData.split('], [')
for i in items:
    attributes = i.split(',')
    if len(attributes) == 4:
        listOfBasketObjects = []
        print(attributes[3])
#     if len(attributes) == 5:
#         print('poo')

# print(listOfBasketObjects)

# if __name__ == '__main__':
#     unittest.main()