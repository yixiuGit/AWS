import json
import boto3
import urllib.parse
from botocore.errorfactory import ClientError

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    s3Resource=boto3.resource('s3')
    print(event)
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    print(key)
    response = s3.get_object(Bucket='my-bucket-in-sydney-without-content', Key=key)
    sourceBucket={'Bucket':"my-bucket-in-sydney-without-content", 'Key':key}
    photoBucket=s3Resource.Bucket('my-bucket-with-jpeg')
    print(response)
    filetype=response['ContentType']
    print(filetype)
    if "jpeg" in filetype:
        s3Resource.meta.client.copy(sourceBucket, 'my-bucket-with-jpeg', key)
    elif "csv" in filetype:
        try:
            s3.head_object(Bucket='my-bucket-with-csv', Key=key)
            print('exist')
        except ClientError:
            print("not exist")
            s3Resource.meta.client.copy(sourceBucket, 'my-bucket-with-csv', key)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
