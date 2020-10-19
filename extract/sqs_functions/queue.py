import json
import boto3

def send_sqs_data(data, file_key):
    # sends the list of lists to the queue in the form of a string
    sqs_client = boto3.client('sqs')
    sqs_client.send_message(QueueUrl="https://sqs.eu-west-1.amazonaws.com/579154747729/Team2-extract-to-tranform", MessageBody=json.dumps(data))
    print(f"{file_key} has been extracted.")
    return