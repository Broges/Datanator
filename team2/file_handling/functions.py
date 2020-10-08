import boto3
import csv
from datetime import date
from core.basket_class import Basket
from core.transaction_class import Transaction

def get_csv(file):
    bucketname = 'cafe-transactions' # replace with your bucket name
    s3 = boto3.resource('s3')
    newfile = f'/tmp/{file}'
    s3.Bucket(bucketname).download_file(file, newfile)

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
    file_name = name_csv.replace('/tmp/', '')
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file(name_csv, 'cafe-etl', file_name)

def make_new_filenames(file_name):
    temp_1 = file_name.strip('.csv')
    temp_2 = temp_1.split('')
    time = temp_2[-1]
    date = temp_2[-2]
    name = temp_1.replace(time,'').replace(date,'').strip('')

    temp_3 = name.split('')
    code = ""
    if len(temp_3) > 1:
        for foo in temp_3:
            code = code + foo[0]
    else:
        code = name[0:3]

    transactionfilename = f"/tmp/team2{code}_{date}_transaction.csv" # team2_transaction_iow_30-09-2020.csv
    basketfilename = f"/tmp/team2{code}_{date}_basket.csv" # team2_basket_iow_30-09-2020.csv

    return transactionfilename, basketfilename
