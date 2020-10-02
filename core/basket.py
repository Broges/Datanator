from file_handling.functions import read_csv
from core.basket_class import Basket

def make_basket_list():
    lst = []

    data = read_csv('tmp/temp.csv') # /tmp/temp.csv
    lst = clean_basket_data(data)

    return lst

def clean_basket_data(data):
    lst = []
    transaction_id = 1
    basket_id = 1
    for row in data:
        combined_data = (row[3]).split(", ")
        for i in range(len(combined_data)):
            string = combined_data[i]
            product_name = ''.join([i for i in string if not (i.isdigit() or i == ".")])
            price = combined_data[i].strip(product_name)
            product_name = product_name[:-3]
            lst.append(Basket(basket_id, transaction_id, product_name, float(price)))
            basket_id += 1
        transaction_id += 1
    return lst