import json
# import boto3
# import os
def lambda_handler(event, context):
    message = 'Hello World V1'
    print(message)
    resp={"statusCode": 200,"body":message}
    return json.dumps(resp)