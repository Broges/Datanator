from core.transaction import make_transactions_list
from core.basket import make_basket_list
from file_handling.functions import get_csv, write_csv, save_to_bucket

def start(event, context): # event, lambda_context):
    dates = ["29-09-2020", "30-09-2020"]

    for date in dates:
        print(date)
        transaction_csv = (f"tmp/transaction_{date}.csv") # /tmp/transaction_{date}.csv
        basket_csv = (f"tmp/basket_{date}.csv") # /tmp/basket_{date}.csv

        get_csv(date)

        transactions_list = make_transactions_list(date)
        basket_list = make_basket_list(date)

        write_csv(transaction_csv, transactions_list)
        write_csv(basket_csv, basket_list)

        # save_to_bucket(transaction_csv)
        # save_to_bucket(basket_csv)
    return

lambda_handler() # event, lambda_context)