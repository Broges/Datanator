import unittest
from bucket_functions.trigger import inbetween_days, get_event_file_key

class Test_functions(unittest.TestCase):
    def test_inbetween_days(self):
        date1 = "28/12/2020"
        date2 = "30/12/2020"
        date3 = "01/01/2021"
        answer1 = ["28-12-2020", "29-12-2020", "30-12-2020"]
        answer2 = ["30-12-2020", "31-12-2020", "01-01-2021"]
        answer3 = []
        self.assertEqual(inbetween_days(date1, date2), answer1)
        self.assertEqual(inbetween_days(date2, date3), answer2)
        self.assertEqual(inbetween_days(date3, date1), answer3)

    def test_get_event_file_key(self):
        json_event ={
            "Records": [
                {
                    "eventVersion": "2.0",
                    "eventSource": "aws:s3",
                    "awsRegion": "eu-west-1",
                    "eventTime": "1970-01-01T00:00:00.000Z",
                    "eventName": "ObjectCreated:Put",
                    "userIdentity": {
                        "principalId": "EXAMPLE"
                    },
                    "requestParameters": {
                        "sourceIPAddress": "127.0.0.1"
                    },
                    "responseElements": {
                        "x-amz-request-id": "EXAMPLE123456789",
                        "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
                    },
                    "s3": {
                        "s3SchemaVersion": "1.0",
                        "configurationId": "testConfigRule",
                        "bucket": {
                            "name": "example-bucket",
                            "ownerIdentity": {
                                "principalId": "EXAMPLE"
                            },
                            "arn": "arn:aws:s3:::example-bucket"
                        },
                        "object": {
                            "key": "isle_of_wight_30-09-2020_16-30-00.csv",
                            "size": 1024,
                            "eTag": "0123456789abcdef0123456789abcdef",
                            "sequencer": "0A1B2C3D4E5F678901"
                        }
                    }
                }
            ]
        }

        file_key = 'isle_of_wight_30-09-2020_16-30-00.csv'
        
        self.assertEqual(get_event_file_key(json_event), file_key)

if __name__ == '__main__':
    unittest.main()