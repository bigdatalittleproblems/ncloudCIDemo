import json
# import boto3
import os
destBucket = os.environ['Dest_Bucket']
def lambda_handler(event, context):
    message = 'Hello World V1'
    print(message)
    return {"statusCode": 200,"response":message}