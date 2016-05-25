import boto3
from flask import Flask, request, jsonify
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')

def call_get_users(username):
    table = dynamodb.Table('Users')
    response = table.query(
    KeyConditionExpression=Key('username').eq(username)
    )
    for i in response['Items']:
        return i

def create_user(username):
   return

def update_user(username):
   return
