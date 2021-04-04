import json
# import boto3
# import os
def lambda_handler(event, context):
    message = "Hello World V1"
    print(message)
    return json.dumps({
        "statusCode": 200,
        "body": {
            "message": message,
        },
        "headers":{ 'Access-Control-Allow-Origin' : '*' },  
        "isBase64Encoded": "false"
    })