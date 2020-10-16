from core.redshiftFunctions import Redshift, redshiftHandler
from core.sqs import recieve_sqs_message
from core.basket import Basket
from core.transaction import Transaction

def lambda_handler(event,context):
    #print("Hello World")
    redshiftHandler.redshiftConnector()
    
    the_message = recieve_sqs_message(event)
    bigData = the_message[2:-2]
    listOfBasketObjects = []
    listOfTransactionObjects=[]
    all_data = bigData.split('], [')
    
    for item in all_data:
        attributes = item.split(',')
        if len(attributes) == 4:
            basketObject = Basket(attributes[0],attributes[1].replace(' ', ''),attributes[2],attributes[3])
            listOfBasketObjects.append(basketObject)
            if item == all_data[-1]:
                redshiftHandler.importDataToBasketTable(listOfBasketObjects)
    
        elif len(attributes) == 5:
            transactionObject = Transaction(attributes[0],attributes[1],attributes[2],attributes[3],attributes[4])
            listOfTransactionObjects.append(transactionObject)
            if item == all_data[-1]:
                redshiftHandler.importDataToTransactionTable(listOfTransactionObjects)
    redshiftHandler.closeRedshiftConnection()