import csv
from core.transaction_class import Transaction

def read_csv(file_name):
    with open(file_name) as file:
        reader = csv.reader(file, delimiter=',')
        data = []
        for row in reader:
            data.append(row)
        return data

def make_transactions_list():
    data = read_csv('tmp/temp.csv') # /tmp/temp.csv
    lst = clean_transaction_data(data)

    return lst
    
def clean_transaction_data(data):
    lst = []
    transaction_id = 1
    for line in data:
        lst.append(Transaction(transaction_id, line[1], line[2], line[0], float(line[4])))
        transaction_id += 1
    return lst

def do():
    transactions_list = make_transactions_list()

    total = 0
    for obj in transactions_list:
        total += obj.pay_amount
    print(f"£{int(total)}")

do()