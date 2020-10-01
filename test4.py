class Basket:
    def __init__(self, basket_id, transaction_id, basket_item, price):
        self.basket_id = basket_id
        self.transaction_id = transaction_id
        self.basket_item = basket_item
        self.price = price

    def __repr__(self):
        return (f"{self.basket_id}, {self.transaction_id}, {self.basket_item}, £{self.price}")

class Transaction:
    def __init__(self, transaction_id, location, customer_name, date, pay_amount):
        self.transaction_id = transaction_id
        self.location = location
        self.customer_name = customer_name
        self.date = date
        self.pay_amount = pay_amount
    
    def __repr__(self):
        return (f"{self.transaction_id}, {self.location}, {self.customer_name}, {self.date}, {self.pay_amount}")