from flask import Flask, request, jsonify
from exceptions import CustomException
from users import call_get_users,create_user,update_user

import boto3
from boto3.dynamodb.conditions import Key, Attr


app = Flask(__name__)

@app.route("/")
def defalt():
    return "Hello"

@app.route('/users', methods=['POST'])
def create_user():
    try:
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
    except Exception as e:
        raise CustomException(
            status_code=500,
            message="Server Error")
            return
    user = {'status':'success'}
    return (user,201)

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = {}
    try:
        user = call_get_users(username)
        return (jsonify(user),201)

    except IndexError:
        raise CustomException(
            status_code=404,
            message="User Not Found"
            )
        return
    except Exception as e:
        raise CustomException(
            status_code=500,
            message="Server Error"
            )
        return
@app.route('/users/<username>', methods=['PUT'])
def get_user(username):
    user = {}
    try:
        user = call_get_users(username)
        return (jsonify(user),201)

    except IndexError:
        raise CustomException(
            status_code=404,
            message="User Not Found"
            )
        return
    except Exception as e:
        raise CustomException(
            status_code=500,
            message="Server Error"
            )
        return

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
