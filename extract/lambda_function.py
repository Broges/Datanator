from bucket_functions.trigger import get_event_file_key
from bucket_functions.extract import get_csv_data_from_bucket
from sqs_functions.queue import send_sqs_data

def lambda_handler(event, context):
    bucketname = "cafe-etl"
    
    file_key = get_event_file_key(event)
    
    print(file_key)
    
    data = get_csv_data_from_bucket(bucketname, file_key)

    send_sqs_data(data, file_key)
    
    return