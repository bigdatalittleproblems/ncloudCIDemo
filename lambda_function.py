import json
# import boto3
# import os


def lambda_handler(event, context):
    message = "Hello World! From Christian Ramirez App V2"
    print(message)
    return {"statusCode": 200, "body": message}