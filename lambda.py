import datetime
import json
import boto3
import logging
import uuid
import jwt


getMethod= 'GET'
postMethod= 'POST'
deleteMethod= 'DELETE'
patchMethod= 'PATCH'
bucketName= 'Bucket'
jwtSecret = 'secret'

def lambda_handler(event, context):
    httpMethod= event['httpMethod']
    path =event['path']
    token=event['authorizationToken']
    try:
        jwt.decode(token, jwtSecret, algorithms=['HS256'])
    except jwt.exceptions.InvalidSignatureError:
        return getError(401, {'error': 'Invalid token'})
    if event['authorizationToken'] is not None:
        response=getError(404)
    elif httpMethod == getMethod and path == '/': 
        response =getRes(event['queryStringParameters']['id'])
    elif httpMethod == postMethod and path == '/':
        response =postRes(json.loads(event['body']),token)
    elif httpMethod == deleteMethod and path == '/':
        requestBody=json.loads(event['body'])
        response =deleteRes(requestBody['id'])
    elif httpMethod == patchMethod and path == '/':
        requestBody=json.loads(event['body'])
        response =patchRes(requestBody['id'], requestBody['body'],token)
    else:
        response =getError(404)
    return response


def getRes(id):
    s3 = boto3.resource('s3')
    content_object = s3.Object(bucketName,  str(id)+'.json')
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    response ={
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(json_content)
    }
    return response

def postRes(body, token):
    try:    
        s3 = boto3.resource('s3')
        body['createdAt'] = str(datetime.datetime.now())
        body['createdBy'] = jwt.decode(token, jwtSecret, algorithms=['HS256'])['name']
        body['id']= uuid.uuid3()
        s3.put_object(
            Body=json.dumps(body),
            Bucket=bucketName,
        )
        response ={
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(body)
        }
        return response
    except Exception as e:
        return getError(400, {'error': str(e)})

def deleteRes(id):
    try:
        s3 = boto3.resource('s3')
        s3.Object(bucketName, str(id)+'.json').delete()
        response ={
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'id': id})
        }
        return response
    except Exception as e:
        return getError(400, {'error': str(e)})

def patchRes(id, body, token):
    try:
        s3=boto3.resource('s3')
        body['updatedAt'] = str(datetime.datetime.now())
        body['updatedBy'] = jwt.decode(token, jwtSecret, algorithms=['HS256'])['name']
        content_object = s3.Object(bucketName,  str(id)+'.json')
        file_content = content_object.get()['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)
        json_content.update(body)
        s3.Object(bucketName, str(id)+'.json').put(Body=json.dumps(json_content))
        response ={
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(json_content)
        }
        return response
    except Exception as e:
        return getError(400, {'error': str(e)})

def getError(statusCode, body=None):
    response={
        'statusCode': statusCode,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True
        },
    }
    if body is not None:
        response['body'] = json.dumps(body)
    return response