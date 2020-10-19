import boto3
import json
import sys

def send_sqs_message(queue_name, msg_body):
    sqs_client = boto3.client('sqs')
    # print(json.dumps(msg_body))
    if sys.getsizeof(json.dumps(msg_body)) < 256000:
        msg = sqs_client.send_message(QueueUrl="https://sqs.eu-west-1.amazonaws.com/579154747729/Team2-transform-to-load", MessageBody=json.dumps(msg_body))
    else:
        print(f"{msg_body[0][0]} was to big")
    return

def recieve_sqs_message(event):
    for record in event['Records']:
        payload=record["body"]
        return str(payload)