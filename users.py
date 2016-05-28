import boto3
from flask import Flask, request, jsonify
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')

def get_users_from_db(username):
    table = dynamodb.Table('Users')
    response = table.query(
        KeyConditionExpression=Key('username').eq(username)
        )
    return [user for user in response['Items']]

def create_user_in_db(username,userType,publicInfo,protectedInfo,privateInfo):
    table = dynamodb.Table('Users')
    response = table.put_item(
        Item={
            'username': usernmae,
            'usertype': userType,
            'publicInfo': publicInfo,
            'protectedInfo': protectedInfo,
            'privateInfo': privateInfo,
            },
        )
    return

def update_user_in_db(username,userType,publicInfo,protectedInfo,privateInfo):
    table = dynamodb.Table('Users')
    response = table.update_item(
        Key={
            'username': usernmae,
            },
        UpdateExpression="set info.rating = :r, info.plot=:p, info.actors=:a",
        ExpressionAttributeValues={
            ':usertype': userType,
            ':publicInfo': publicInfo,
            ':protectedInfo': protectedInfo,
            ':privateInfo': privateInfo,
            },
        ReturnValues="UPDATED_NEW",
        )
    return
