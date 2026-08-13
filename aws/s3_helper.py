import boto3
from botocore.exceptions import ClientError

def download_s3_file(bucket, key, dest_path):
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket, key, dest_path)
        return True
    except ClientError:
        return False

def upload_s3_file(bucket, key, src_path):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(src_path, bucket, key)
        return True
    except ClientError:
        return False
