from core.transaction import make_transactions_list
from core.basket import make_basket_list
from redshift.redshiftHandler import Redshift, redshiftHandler
from file_handling.functions import get_csv, write_csv, save_to_bucket, make_new_filenames
import boto3
import os
import datetime



def start(event, context):
    
    redshiftHandler.redshiftConnector() #gets credentials, and connects to redshift, keeps connection open

    today = datetime.datetime.utcnow().date()
    date = today - datetime.timedelta(days=2)
    date = date.strftime("%d-%m-%Y")


    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket('cafe-transactions')

    filename_list = []
    for my_bucket_object in my_bucket.objects.all():
        filename_list.append(my_bucket_object.key)


    for file_ in filename_list:
        if date in file_:
            get_csv(file_)

            transaction_filename, basket_filename = make_new_filenames(file_)

            transactions_list = make_transactions_list(date)
            basket_list = make_basket_list(date)

            redshiftHandler.redshiftTruncate()#calls method to truncate both tables

            redshiftHandler.importDataToBasketTable(basket_list)#imports all basket objects to basket table
            
            redshiftHandler.importDataToTransactionTable(transactions_list)#imports all transaction objects to transaction table
            

            #write_csv(transaction_filename, transactions_list)
            #write_csv(basket_filename, basket_list)

            #save_to_bucket(transaction_filename)
            #save_to_bucket(basket_filename)

   
    redshiftHandler.closeRedshiftConnection()#closes connection to redshift

    return
