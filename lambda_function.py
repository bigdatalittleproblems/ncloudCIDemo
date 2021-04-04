import json
# import boto3
# import os


def lambda_handler(event, context):
    message = "Hello World V1"
    print(message)
    return {
        "statusCode": "200",
        "body": {
            "message": json.dumps({'message': message}),
        },
        "headers": {
            "Access-Control-Allow-Origin": '*'},
        "isBase64Encoded": "false",
        "Content-Type": "application/json"
    }
