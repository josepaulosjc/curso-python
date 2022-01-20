import boto3

print(f"{boto.client('sts').get_caller_identity().get('ResponseMatadata').get('RequestId')}")

session = boto3.Session()
credentials = session.get_credentials()
credentials = credentials.access_key
credentials = credentials.secret_key

print(credentials)
print(f"{boto3.client('sts').get_caller_identity()}")