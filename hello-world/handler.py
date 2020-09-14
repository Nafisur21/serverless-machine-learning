import json


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your hello-world function executed successfully!",
        "input": event
    }
    print(body['message'])
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


if __name__ == '__main__':
    res = hello(event={"name": "Nafisur", "title": "Rahman"}, context='None')
    print(res)
