import csv
from file_handling.functions import read_csv

class Transaction:
    def __init__(self, transaction_id, location, customer_name, date, pay_amount):
        self.transaction_id = transaction_id
        self.location = location
        self.customer_name = customer_name
        self.date = date
        self.pay_amount = pay_amount
    
    def __repr__(self):
        return (f"{self.transaction_id}, {self.location}, {self.customer_name}, {self.date}, {self.pay_amount}")

def read_transaction(transaction_list):
    x = 1
    data = read_csv('oo.csv')
    for line in data:
        transaction_list.append(Transaction(x, line[1], line[2], line[0], float(line[4]))) 
        x += 1
