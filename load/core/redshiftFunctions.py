import boto3
import os
import sys
import psycopg2
import psycopg2.extras
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

    def redshiftTruncate(self):
        try:
            cursor = conn.cursor()
            cursor.execute("TRUNCATE TABLE transaction_data_team2;")
            cursor.execute("TRUNCATE TABLE basket_data_team2;")
            cursor.close()
            conn.commit()
        except Exception as ERROR:
            print("Truncate error: <%s>" %ERROR)
            

    def closeRedshiftConnection(self):
        try:
            conn.close()
        except Exception as ERROR:
            print("Error closing DB connection: <%s>" %ERROR)

    def importDataToBasketTable(self,list):

        try:
            cursor = conn.cursor()
            query="INSERT INTO basket_data_team2 VALUES %s"#creates the query without values
            data=[(obj.basket_id,obj.transaction_id,obj.basket_item,obj.price) for obj in list]#iterates through every obj in list, puts their attributes as values
            psycopg2.extras.execute_values(cursor,query,data)#combines all vars together to create entire sql query
            cursor.close()
            conn.commit()#pushes changes to DB

        except Exception as ERROR:
            print("Execution error with basket table: <%s>" %ERROR)

    def importDataToTransactionTable(self,list):

        try:
            cursor = conn.cursor()
            query="INSERT INTO transaction_data_team2 VALUES %s" #creates the query
            data=[(obj.transaction_id,obj.location,obj.customer_name,obj.date, obj.pay_amount) for obj in list] #iterates through every object in list, grabs their attributes and puts them as values
            psycopg2.extras.execute_values(cursor,query,data)#combines all vars together to create entire sql query
            cursor.close()
            conn.commit() #pushes the code to the DB

        except Exception as ERROR:
            print("Execution error with transaction table: <%s>" %ERROR)

redshiftHandler=Redshift()