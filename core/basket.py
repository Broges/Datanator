import csv
from file_handling.functions import read_csv


class Basket:
    def __init__(self, basket_id, transaction_id, basket_item, price):
        self.basket_id = basket_id
        self.transaction_id = transaction_id
        self.basket_item = basket_item
        self.price = price
    def __repr__(self):
        return (f"{self.basket_id}, {self.transaction_id}, {self.basket_item}, £{self.price}")

def read_basket(clean_data):
    transaction_id = 1
    basket_id = 1
    
    csv_rows = read_csv('oo.csv')
    transaction_id = 1
    basket_id = 1
    clean_data = []
    for row in csv_rows:
        combined_data = (row[3]).split(", ")
        for i in range(len(combined_data)):
            s = combined_data[i]
            product_name = ''.join([i for i in s if not (i.isdigit() or i == ".")])
            price = combined_data[i].strip(product_name)
            product_name = product_name[:-3]
            clean_data.append([basket_id, transaction_id, product_name, float(price)])
            basket_id += 1
            transaction_id += 1
    return clean_data
# data = func()
# for line in data:
#     print(line)