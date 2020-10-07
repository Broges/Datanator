class Transaction:
    def __init__(self, transaction_id, location, customer_name, date, pay_amount):
        self.transaction_id = transaction_id
        self.location = location
        self.customer_name = customer_name
        self.date = date
        self.pay_amount = pay_amount
    
    def __repr__(self):
        return (f"{self.transaction_id}, {self.location}, {self.customer_name}, {self.date}, £{self.pay_amount}")