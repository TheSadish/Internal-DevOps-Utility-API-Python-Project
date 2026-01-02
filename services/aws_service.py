import boto3 # type: ignore

def get_bucket_info():
    s3_client = boto3.client('s3')
    bucket_json = s3_client.list_buckets()
    print ("Error fetching details") if (bucket_json['ResponseMetadata']['HTTPStatusCode'] != 200 ) else print("Bucket Names:")
    
    # for bucket in bucket_json['Buckets']:
    #     print(f"- {bucket['Name']}")

    return bucket_json['Buckets']

print(get_bucket_info())

