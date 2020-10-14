def recieve_sqs_message(event):
    for record in event['Records']:
        payload=record["body"]
        #print(str(payload))
        return str(payload)