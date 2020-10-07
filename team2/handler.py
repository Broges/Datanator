from core.transaction import make_transactions_list
from core.basket import make_basket_list
from file_handling.functions import get_csv, write_csv, save_to_bucket
import boto3
import os
import sys
import psycopg2
from dotenv import load_dotenv
load_dotenv()

def lambda_handler(event, context): # event, lambda_context):
    load_dotenv()
    dates = ["29-09-2020", "30-09-2020"]

    for date in dates:
        print(date)
        transaction_csv = (f"/tmp/transaction_{date}.csv") # /tmp/transaction_{date}.csv
        basket_csv = (f"/tmp/basket_{date}.csv") # /tmp/basket_{date}.csv

        get_csv(date)

        transactions_list = make_transactions_list(date)
        basket_list = make_basket_list(date)

        write_csv(transaction_csv, transactions_list)
        write_csv(basket_csv, basket_list)

        save_to_bucket(transaction_csv)
        save_to_bucket(basket_csv)

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

#lambda_handler() # event, lambda_context)