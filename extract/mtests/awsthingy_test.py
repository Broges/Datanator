from s3_handler import S3Handler
import boto3
from moto import mock_s3


@mock_s3
def test_upload_s3_file():
    print(1)
    s3_client = boto3.client("s3")
    print(2)
    s3_client.create_bucket(Bucket="my_bucket")
    print(3)
    s3_handler = S3Handler()
    print(4)
    s3_handler.upload_s3_file()

test_upload_s3_file()