import json
import boto3
from botocore.errorfactory import ClientError

s3 = boto3.client('s3')
def lambda_handler(event, context):

    try:
        s3.head_object(Bucket='my-bucket-with-csv', Key='80441.csv')
        print('exist')
    except ClientError:
    # Not found
        pass
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
