import boto3 # type: ignore
from datetime import datetime

def get_bucket_info():
    s3_client = boto3.client('s3')
    bucket_json = s3_client.list_buckets()

    if (bucket_json['ResponseMetadata']['HTTPStatusCode'] != 200 ):
        print ("Error fetching details")

    current_date = datetime.now()
    old_buckets = []
    new_buckets = []
    for bucket in bucket_json['Buckets']:
        bucket_created = bucket['CreationDate'].replace(tzinfo=None)
        old_buckets.append(bucket["Name"])  if (current_date - bucket_created).days > 30 else new_buckets.append(bucket["Name"])   

    return {
        "Old_Buckets": old_buckets,
        "New_Buckets": new_buckets
    }

print(get_bucket_info())