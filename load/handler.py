from core.redshiftFunctions import Redshift, redshiftHandler
from core.sqs import recieve_sqs_message
from core.basket import Basket
from core.transaction import Transaction

def lambda_handler(event,context):

    the_message = recieve_sqs_message(event)
    bigData = the_message[2:-2]
    
    all_data = bigData.split('], [')
    for item in all_data: #has the 4 thigns 
        attributes = item.split(',')
        if len(attributes) == 4:
            listOfBasketObjects = []
            basketObject = Basket(attributes[0],attributes[1],attributes[2],attributes[3])
            listOfBasketObjects.append(basketObject)            
        elif len(attributes) == 5:
            listOfTransactionObjects=[]
            transactionObject = Transaction(attributes[0],attributes[1],attributes[2],attributes[3],attributes[4])
            listOfTransactionObjects.append(transactionObject)
    
    redshiftHandler.redshiftConnector()
    
    redshiftHandler.importDataToTransactionTable(listOfTransactionObjects)
    redshiftHandler.importDataToBasketTable(listOfBasketObjects)
    redshiftHandler.closeRedshiftConnection()