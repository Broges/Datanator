from core.redshiftFunctions import Redshift, redshiftHandler
from core.sqs import recieve_sqs_message
from core.basket import Basket
from core.transaction import Transaction

def lambda_handler(event,context):


    allData = recieve_sqs_message(event)
    bigData = allData[2:-3]
    #bothLists[0] = basket
    #bothLists[1] = transactions
    
    bothLists = bigData.split(']],')
    bothLists[0] += "]"
    bothLists[0] = bothLists[0][1:-1]
    basketItems = bothLists[0].split('], [')
    
    bothLists[1] += "]"
    bothLists[1] = bothLists[1][3:-1]
    transactionItems = bothLists[1].split('], [')
    
    listOfBasketObjects = []
    for obj in basketItems:
        attributes = obj.split(',')
        basketObject = Basket(attributes[0],attributes[1],attributes[2],attributes[3])
        listOfBasketObjects.append(basketObject)
    
    listOfTransactionObjects=[]
    for obj in transactionItems:
        attributes = obj.split(',')
        transactionObject = Transaction(attributes[0],attributes[1],attributes[2],attributes[3],attributes[4])
        listOfTransactionObjects.append(transactionObject)

    
    redshiftHandler.redshiftConnector()
    redshiftHandler.redshiftTruncate()
    
    redshiftHandler.importDataToTransactionTable(listOfTransactionObjects)
    redshiftHandler.importDataToBasketTable(listOfBasketObjects)