from flask import Flask, request, jsonify

from exceptions import CustomException
from users import get_users,create_user,update_user
app = Flask(__name__)

@app.route("/")
def defalt():
    return "Hello"

@app.route('/users', methods=['POST'])
def create_user():
    usernmae=request.json['usernmae']
    publicInfo=request.json['publicInfo']
    protectedInfo=request.json['protectedInfo']
    privateInfo=request.json['privateInfo']
    userType=request.json['userType']
    table = dynamodb.Table('Users')
    response = table.put_item(
     Item={
        'UserId': usernmae,
        'UserType': userType,
     })
    return ('success',201)

@app.route('/users/<username>', methods=['GET'])

def get_user(username):
    try:
        user = username
    except IndexError:
        raise CustomException(
            status_code=404,
            message="User Not Found"
            )
    except Exception as e:
        raise CustomException(
            status_code=500,
            message="Server Error"
            )

    return (username,401)

@app.errorhandler(CustomException)
def error_handler(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

if __name__ == "__main__":
    app.run(debug=True)
'''
import json
dynamodb = boto3.resource('dynamodb')
from boto3.dynamodb.conditions import Key, Attr

print("Table status:", table.table_status)

table = dynamodb.Table('TriageIQUsers')

UserId = "danfujita"
UserType = "doctor"

response = table.put_item(
   Item={
        'UserId': UserId,
        'UserType': UserType,
    }
)

table = dynamodb.Table('TriageIQUsers')

print("Movies from 1985")

response = table.query(
    KeyConditionExpression=Key('UserId').eq("danfujita")
)

for i in response['Items']:
    print(i)
'''
