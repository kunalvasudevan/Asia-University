def lambda_handler(event, context):
    entity = event["currentIntent"]["slots"]["Name"].title()
    intent = event["currentIntent"]["name"]
    
    response =  {
                  
    "sessionAttributes": {
    "key1": "value1",
    "key2": "value2"
  },
                        "dialogAction":
                        {
                            "fulfillmentState":"Fulfilled",
                            "type":"Close",
                            "message":
                                {
                                    "contentType":"PlainText",
                                    "content": "The intent you are in now is "+intent+"!"
                                }
                        }
                    
                }
    return response
