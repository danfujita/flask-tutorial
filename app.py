import boto3
from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def defalt():
    return "shalom!!!!!!"

@app.route('/hello', methods=['POST'])
def test():
    username=request.json['username']
    print (username)
    password=request.json['password']
    print (password)
    return ('test',401)

@app.route('/hello', methods=['POST'])
def test():
    username=request.json['username']
    print (username)
    password=request.json['password']
    print (password)
    return ('test',401)

if __name__ == "__main__":
    app.run(debug=True)
'''
import json
dynamodb = boto3.resource('dynamodb')
from boto3.dynamodb.conditions import Key, Attr

table = dynamodb.create_table(
    TableName='TriageIQUsers',
    KeySchema=[
        {
            'AttributeName': 'UserId',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'UserType',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'UserId',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'UserType',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
)
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
