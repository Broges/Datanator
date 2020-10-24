from datetime import date, timedelta, datetime
import boto3
from bucket_functions.extract import get_csv_data_from_bucket
from sqs_functions.queue import send_sqs_data

def get_event_file_key(event):
    # this returns the file key from the event record
    records = [x for x in event.get('Records', []) if x.get('eventName') == 'ObjectCreated:Put']
    sorted_events = sorted(records, key=lambda e: e.get('eventTime'))
    latest_event = sorted_events[-1] if sorted_events else {}
    info = latest_event.get('s3', {})
    file_key = info.get('object', {}).get('key')
    return file_key
    
def big_red_button(hard_restart, start_date, end_date, bucketname):
    # The purpose of this function is to retrieve the data from the files
    # dated the dates inbetween the start and end date to act as a hard restart
    # hard restart should be set as False in normal use
    if hard_restart == False:
        pass
    else:
        days = inbetween_days(start_date, end_date)
        filename_list = []
        
        s3 = boto3.resource('s3')
        my_bucket = s3.Bucket(bucketname)
        for my_bucket_object in my_bucket.objects.all():
            for day in days:
                if day in my_bucket_object.key:
                    filename_list.append(my_bucket_object.key)
        print(f"Bewteen the dates of {start_date} and {end_date}, there are {len(filename_list)} files that are about to be extracted")

        file_no = 1
        for file in filename_list:
            data = get_csv_data_from_bucket(bucketname, file)
            print(f"{file_no}:")
            send_sqs_data(data, file)
            file_no += 1
    print("Extraction complete, I hope it worked for you.")
    return

def inbetween_days(sdate, edate):
    # this returns a list of dates ("dd-mm-yyyy") inbetween the start
    # and end date
    sdate = sdate.split('/')
    edate = edate.split('/')
    
    sdate = date(int(sdate[2]),int(sdate[1]),int(sdate[0]))   # start date
    edate = date(int(edate[2]),int(edate[1]),int(edate[0]))   # end date

    delta = edate - sdate   # as timedelta
    
    days = []
    for i in range(delta.days + 1):
        day = sdate + timedelta(days=i)
        day = datetime.strptime(str(day), '%Y-%m-%d').strftime('%d-%m-%Y')
        day = str(day)
        days.append(day)
    return days