class Basket:
    def __init__(self, basket_id, transaction_id, basket_item, price):
        self.basket_id = basket_id
        self.transaction_id = transaction_id
        self.basket_item = basket_item
        self.price = price
    def __repr__(self):
        return (f"{self.basket_id}, {self.transaction_id}, {self.basket_item}, £{self.price}")