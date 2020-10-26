import json
from basket import clean_basket_data
from transaction import clean_transaction_data
from SQS import send_sqs_message, recieve_sqs_message

def lambda_handler(event, context):
    print("hello world")
    # sqs_input=recieve_sqs_message(event)
    
    # sqs_input = sqs_input.replace("'", '"')
    # data = json.loads(sqs_input)
    
    # basket_objects_list = clean_basket_data(data)
    # transaction_objects_list = clean_transaction_data(data)
    
    # print(transaction_objects_list)

    # print("About to send message")
    # send_sqs_message('Team2-transform-to-load', basket_objects_list)
    # send_sqs_message('Team2-transform-to-load', transaction_objects_list)
    # print("Message sent")
    
    return