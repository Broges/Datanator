from core.transaction import make_transactions_list
from core.basket import make_basket_list
from file_handling.functions import get_csv, write_csv, save_to_bucket, make_new_filenames
import boto3
import os
import datetime
import sys
import psycopg2
from dotenv import load_dotenv
load_dotenv()


def start(event, context):
    today = datetime.datetime.utcnow().date()
    date = today - datetime.timedelta(days=2)
    date = date.strftime("%d-%m-%Y")
    print(date)
    load_dotenv()


    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket('cafe-transactions')

    filename_list = []
    for my_bucket_object in my_bucket.objects.all():
        filename_list.append(my_bucket_object.key)

    print(filename_list)

    for file_ in filename_list:
        if date in file_:
            get_csv(file_)

            transaction_filename, basket_filename = make_new_filenames(file_)

            transactions_list = make_transactions_list(date)
            basket_list = make_basket_list(date)

            write_csv(transaction_filename, transactions_list)
            write_csv(basket_filename, basket_list)

            save_to_bucket(transaction_filename)
            save_to_bucket(basket_filename)


    host = os.getenv("DB_HOST")
    port = int(os.getenv("DB_PORT"))
    DbUser = os.getenv("DB_USER")
    passwd = os.getenv("DB_PASS")
    db = os.getenv("DB_NAME")
    cluster = os.getenv("DB_CLUSTER")

    try:
        client = boto3.client('redshift')
        creds = client.get_cluster_credentials(
            DbUser=DbUser,
            DbName=db,
            ClusterIdentifier=cluster,
            DurationSeconds=3600)
    except Exception as ERROR:
        print("Credentials issue: <%s>" %ERROR)
        sys.exit(1)

    print("got creds")

    try:
        conn=psycopg2.connect(
            dbname=db,
            user=creds["DbUser"],
            password=creds["DbPassword"],
            port=port,
            host=host)
    except Exception as ERROR:
        print("Connection issue: <%s>" %ERROR)
        sys.exit(1)

    print("connected")

    try:
        cursor = conn.cursor()
        cursor.execute("TRUNCATE TABLE transaction_data_team2;")
        cursor.execute("TRUNCATE TABLE basket_data_team2;")
        cursor.execute("COPY basket_data_team2 FROM 's3://cafe-etl/basket' CREDENTIALS 'aws_access_key_id=AKIAYNWCQEFI3TSFRR44;aws_secret_access_key=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' csv IGNOREHEADER 1;")
        cursor.execute("COPY transaction_data_team2 FROM 's3://cafe-etl/transaction' CREDENTIALS 'aws_access_key_id=AKIAYNWCQEFI3TSFRR44;aws_secret_access_key=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' csv IGNOREHEADER 1;")
        cursor.close()
        conn.commit()
        conn.close()
    except Exception as ERROR:
        print("Execution error: <%s>" %ERROR)
        sys.exit(1)

    print("executed statements")
    return
