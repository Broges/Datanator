from core.redshiftFunctions import Redshift, redshiftHandler


def lambda_handler(event,context):
    tempListTransactions = []
    tempListBasket = []
    for record in event['Records']:
       print ("test")
       payload=record["body"]
       print(str(payload))
    
   #  redshiftHandler.redshiftConnector()
   #  redshiftHandler.redshiftTruncate()
    
   #  redshiftHandler.importDataToTransactionTable(tempListTransactions)
   #  redshiftHandler.importDataToBasketTable(tempListBasket)