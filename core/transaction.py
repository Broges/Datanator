from file_handling.functions import read_csv
from core.transaction_class import Transaction

def make_transactions_list():
    lst = []

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