from bucket_functions.trigger import get_event_file_key, big_red_button
from bucket_functions.extract import get_csv_data_from_bucket
from sqs_functions.queue import send_sqs_data

# This lambda is triggered by a file being put inside of the s3 bucket, 
# it retrieves that file key and then reads the data into the variable 
# called data in the form of a list of lists where each line is a its 
# own list

def lambda_handler(event, context):
    big_red_button(True, "11/10/2020", "11/10/2020") # "dd/mm/yyyy", To get 1 day, have the dates the same
    
    # bucketname = "cafe-etl"
    
    bucketname = "cafe-transactions-group-2"
    
    # file_key = "2020/10/11/craigavon_11-10-2020_19-49-27.csv"
    
    if event:
        file_key = get_event_file_key(event)
        data = get_csv_data_from_bucket(bucketname, file_key)
        send_sqs_data(data, file_key)

    return