from flask import Flask, request, jsonify
from exceptions import CustomException
from users import get_users_db,create_user_db,update_user_db

import boto3
from boto3.dynamodb.conditions import Key, Attr


app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    try:
        usernmae=request.json['usernmae']
        userType=request.json['userType']
        publicInfo=request.json['publicInfo']
        protectedInfo=request.json['protectedInfo']
        privateInfo=request.json['privateInfo']
        create_user_db(usernmae,userType,publicInfo,protectedInfo,privateInfo)
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
        user = get_users_db(username)
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

@app.route('/users', methods=['PUT'])
def put_user(username):
    try:
        usernmae=request.json['usernmae']
        userType=request.json['userType']
        publicInfo=request.json['publicInfo']
        protectedInfo=request.json['protectedInfo']
        privateInfo=request.json['privateInfo']
        update_user_db(usernmae,userType,publicInfo,protectedInfo,privateInfo)
    except Exception as e:
        raise CustomException(
            status_code=500,
            message="Server Error")
        return
    user = {'status':'success'}
    return (user,201)

@app.errorhandler(CustomException)
def error_handler(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response



if __name__ == "__main__":
    app.run(debug=True)
