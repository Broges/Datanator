import boto3
import csv

def get_csv_data_from_bucket(bucketname, file_key):    
    s3 = boto3.client('s3')
    s3_object = s3.get_object(Bucket = bucketname, Key = file_key)
    data = s3_object['Body'].read().decode('utf-8')
    csv_data = csv.reader(data.splitlines())
    data = []
    for row in csv_data:
        data.append(row)
    return data