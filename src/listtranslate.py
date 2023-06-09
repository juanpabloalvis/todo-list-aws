import json
import decimalencoder
import todoList
import boto3


def list(event, context):
    translate = boto3.client(service_name='translate',
                             region_name='us-east-1',
                             use_ssl=True)
    # Obtener los parámetros del evento
    target_language = event['pathParameters']['language']
    print(type(target_language))
    print(target_language)
    items = todoList.get_items()
    print(type(items))

    [print(i) for i in items]
    print(items)
    for item in items:
        text = item['text']
        item['text'] = translate \
            .translate_text(Text=text,
                            SourceLanguageCode="en",
                            TargetLanguageCode=target_language)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(items, cls=decimalencoder.DecimalEncoder)
    }
    return response
