import boto3
import os
import sys
import psycopg2
from dotenv import load_dotenv
load_dotenv()



class Redshift:
    def __init__(self):
        pass
       
    def redshiftConnector(self):
        global conn
        host = os.getenv("DB_HOST") 
        port = int(os.getenv("DB_PORT"))
        DbUser = os.getenv("DB_USER")
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

        

    def redshiftGetFinalBasketID(self):
        try:
            cursor=conn.cursor()
            cursor.execute("SELECT basket_ID FROM basket_data_team2 ORDER BY basket_ID DESC LIMIT 1;")
            rawData = cursor.fetchone()
            rawData=str(rawData)
            filteredData = rawData.strip(",()")
        except Exception as ERROR:
            print("Error with id exec %s" %ERROR)
        return filteredData

    def redshiftExecute(self):
        try:
            cursor = conn.cursor()
            cursor.execute("TRUNCATE TABLE transaction_data_team2;")
            cursor.execute("TRUNCATE TABLE basket_data_team2;")
            cursor.execute("COPY basket_data_team2 FROM 's3://cafe-etl/basket' CREDENTIALS 'aws_access_key_id=AKIAYNWCQEFI3TSFRR44;aws_secret_access_key=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' csv IGNOREHEADER 1;")
            cursor.execute("COPY transaction_data_team2 FROM 's3://cafe-etl/transaction' CREDENTIALS 'aws_access_key_id=AKIAYNWCQEFI3TSFRR44;aws_secret_access_key=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' csv IGNOREHEADER 1;")
            cursor.close()
            conn.commit()
        except Exception as ERROR:
            print("Execution error: <%s>" %ERROR)
            sys.exit(1)

    def closeRedshiftConnection(self):
        try:
            conn.close()
        except Exception as ERROR:
            print("Error closing DB connection: <%s>" %ERROR)

redshiftHandler=Redshift()
