import json
import boto3

def send_sqs_data(data, file_key):
    sqs_client = boto3.client('sqs')
    # sqs_queue_url = sqs_client.get_queue_url(QueueName = queue_name)['QueueUrl']
    sqs_client.send_message(QueueUrl="https://sqs.eu-west-1.amazonaws.com/579154747729/Team2-extract-to-tranform", MessageBody=json.dumps(data))
    # msg = sqs_client.send_message(QueueUrl="https://sqs.eu-west-1.amazonaws.com/579154747729/Team2-extract-to-tranform", MessageBody=json.dumps(data))
    print(f"{file_key} is done.")
    
    return