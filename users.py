import boto3
from flask import Flask, request, jsonify
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')

def get_users_from_db(username):
    table = dynamodb.Table('Users')
    response = table.query(
        KeyConditionExpression=Key('username').eq(username)
        )
    return [user for user in response['Items']]

def create_user_in_db(username, user_type, public_info, protected_info, private_info):
    table = dynamodb.Table('Users')
    response = table.put_item(
        Item={
            'username': username,
            'usertype': user_type,
            'publicInfo': public_info,
            'protectedInfo': protected_info,
            'privateInfo': private_info,
            },
        )

def update_user_in_db(username, user_type, public_info, protected_info, private_info):
    table = dynamodb.Table('Users')
    response = table.update_item(
        Key={
            'username': username,
            },
        UpdateExpression="set info.rating = :r, info.plot=:p, info.actors=:a",
        ExpressionAttributeValues={
            ':usertype': user_type,
            ':publicInfo': public_info,
            ':protectedInfo': protected_info,
            ':privateInfo': private_info,
            },
        ReturnValues="UPDATED_NEW",
        )
