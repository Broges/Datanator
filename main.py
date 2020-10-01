import csv
from core.basket import Basket, read_basket
from core.transaction import Transaction, read_transaction
#from file_handling.functions import read_csv
import file_handling


transaction_list = []

clean_data = []
all_basket_objects = []

print("-----Transaction------ ")#
read_transaction(transaction_list)
for i in transaction_list:
    print(i)

print("\n-----Basket------ ")#
clean_data = read_basket(clean_data)
for i in range(0,len(clean_data)):
    basket_object = Basket(clean_data[i][0] ,clean_data[i][1] ,clean_data[i][2] , clean_data[i][3])
    all_basket_objects.append(basket_object)
for obj in all_basket_objects:
    print(obj)