import boto3

import boto3
import os

s3 = boto3.client('s3',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY'),
    region_name='us-east-1')
bucket_name = 'healthadvisorchatbot'
folder_path = r'C:\health_advisor_chatbot'

for filename in os.listdir(folder_path):
    local_file = os.path.join(folder_path, filename)
    if os.path.isfile(local_file):
        s3.upload_file(local_file, bucket_name, filename)
        print(f"Uploaded {local_file} to s3://{bucket_name}/{filename}")