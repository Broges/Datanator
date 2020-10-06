# import boto3
import csv
from datetime import date
from core.basket_class import Basket
from core.transaction_class import Transaction

def get_csv(date):
    pass
    # bucketname = 'cafe-transactions' # replace with your bucket name
    # #date = date.today()
    # filename = f'isle_of_wight_{date}_16-30-00.csv' # replace with your object key
    # s3 = boto3.resource('s3')
    # s3.Bucket(bucketname).download_file(filename, '/tmp/temp.csv')

def read_csv(file_name):
    with open(file_name) as file:
        reader = csv.reader(file, delimiter=',')
        data = []
        for row in reader:
            data.append(row)
    return data

def write_csv(csv_name, obj_list):
    with open(csv_name, mode='w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow("") #print empty line
        for obj in obj_list:
            if "basket" in csv_name:
                writer.writerow([obj.basket_id, obj.transaction_id, obj.basket_item, obj.price])
            else:
                writer.writerow([obj.transaction_id, obj.location, obj.customer_name, obj.date, obj.pay_amount])
        file.close()

def save_to_bucket(name_csv):
    pass
    # file_name = name_csv.replace('/tmp/', '')
    # s3 = boto3.resource('s3')
    # s3.meta.client.upload_file(name_csv, 'cafe-etl', file_name)

