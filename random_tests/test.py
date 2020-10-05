# load csv file
# transformed

transformed_list = [1, 1, "Regular Flavoured hot chocolate - Hazelnut", 2.60,
    2, 1, "Regular Luxury hot chocolate", 2.40,
    3, 2, "Frappes - Strawberries & Cream", 2.75
    ]

basket = []
basket_list = []

class Basket:
    def __init__(self, basket_id, transaction_id, basket_item, price):
        self.basket_id = basket_id
        self.transaction_id = transaction_id
        self.basket_item = basket_item
        self.price = price
    
    def __repr__(self):
        return (f"{self.basket_id}, {self.transaction_id}, {self.basket_item}, £{self.price}")

for i in range(int((len(transformed_list) / 4))):
    basket = Basket(transformed_list[(i*4) + 0], transformed_list[(i*4) + 1], transformed_list[(i*4) + 2], float(transformed_list[(i*4) + 3]))
    basket_list.append(basket)

for obj in basket_list:
    print(obj)