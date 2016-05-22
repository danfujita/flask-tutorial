import boto3

def get_users(username):
    response = table.query(
        KeyConditionExpression=Key('UserId').eq(username)
    )
    return response['Items']

def create_user(username):
   return

def update_user(username):
   return
