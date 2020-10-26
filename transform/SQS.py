import boto3
import json
import sys

def send_sqs_message(queue_name, msg_body):
    sqs_client = boto3.client('sqs')
    # print(json.dumps(msg_body))

    lst = []
    lst.append(msg_body)
    for sub_list in lst:
        while sys.getsizeof(json.dumps(sub_list)) > 250000:
            x = len(sub_list) // 2
            sub1, sub2 = sub_list[0:x], sub_list[x:]
            temp = lst.index(sub_list)
            lst[temp] = sub1
            lst.insert(temp + 1, sub2)
            sub_list = sub1

    for sub_list in lst:
        print(sys.getsizeof(json.dumps(sub_list)))
        msg = sqs_client.send_message(QueueUrl="https://sqs.eu-west-1.amazonaws.com/579154747729/Team2transformtoload", MessageBody=json.dumps(sub_list))
    
    return

def recieve_sqs_message(event):
    for record in event['Records']:
        payload=record["body"]
        return str(payload)