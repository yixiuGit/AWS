import json
import boto3
import urllib.parse
def lambda_handler(event, context):
    s3 = boto3.client('s3')

    s3.create_bucket(Bucket='my-bucket-in-sydney-without-content',
                     CreateBucketConfiguration={
                         'LocationConstraint': 'ap-southeast-2'
 })
