import json
# import boto3
# import os
def lambda_handler(event, context):
    message = 'Hello World V1'
    print(message)
    return {"statusCode": 200,"response":message}