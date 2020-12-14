#!/usr/bin/env python3
import json,urllib3

def lambda_handler(event, context):
  ########################################### Global Variables #####################################################
  BASE_URL = "https://www.teslafi.com/feed.php?command=lastGood&token="
  EVENT_HEADERS = event["headers"]
  EVENT_PARAMETERS = event["queryStringParameters"] or ""
  
  # If X-Forwarded-For exists then set CLIENT_IP_ADDRESS accordingly
  if "X-Forwarded-For" in EVENT_HEADERS:
    CLIENT_IP_ADDRESS = EVENT_HEADERS["X-Forwarded-For"]
  else:
    CLIENT_IP_ADDRESS = "127.0.0.1"

  if "TOKEN" in EVENT_PARAMETERS: 
    # Variables
    TOKEN = EVENT_PARAMETERS["TOKEN"]

    if TOKEN == "test_token":
      TESTVAR = "TESTVAR_VALUE"
      
      print("Executing the appropriate test on behalf of " + CLIENT_IP_ADDRESS)
      RETURN_DATA = {
        "statusCode": 200,
        "body": TESTVAR
      }

      RETURN_DATA_STR = json.dumps(RETURN_DATA)
    else:
      # Variables
      HEADERS = {
        'Content-Type': 'application/json'
      }
      URL = BASE_URL + TOKEN
      HTTP = urllib3.PoolManager()
      HTTP_REQUEST = HTTP.request(
        'GET',
        URL,
        headers=HEADERS
      )
      HTTP_REQUEST_STATUS_CODE = HTTP_REQUEST.status

      if HTTP_REQUEST_STATUS_CODE == 200 and TOKEN:
        VEHICLE_DATA = json.loads(HTTP_REQUEST.data.decode('utf-8'))
        BATTERY_LEVEL = VEHICLE_DATA["battery_level"]
        BATTERY_CHARGE_LIMIT = VEHICLE_DATA["charge_limit_soc"]
        
        BATTERY_OUTPUT = BATTERY_LEVEL + " / " + BATTERY_CHARGE_LIMIT + " %"
        
        print("Retrieving the requested data from TeslaFi on behalf of " + CLIENT_IP_ADDRESS)
        RETURN_DATA = {
          "statusCode": 200,
          "body": BATTERY_OUTPUT
        }

        RETURN_DATA_STR = json.dumps(RETURN_DATA)
      else:
        print("ERROR: Exiting as communication with TeslaFi's APIs failed on behalf of " + CLIENT_IP_ADDRESS)
        RETURN_DATA = {
          "statusCode": 400,
          "body": "ERROR: TeslaFi connection error encountered, please check your token and try again"
        }

        RETURN_DATA_STR = json.dumps(RETURN_DATA)
  else:
    print("ERROR: Exiting as a TeslaFi token was not specified with the request by " + CLIENT_IP_ADDRESS)

    RETURN_DATA = {
      "statusCode": 400,
      "body": "ERROR: A TeslaFi token was not specified with the request, please specify a token and try again"
    }

    RETURN_DATA_STR = json.dumps(RETURN_DATA)
  
  return {
    'headers': {'Content-Type': 'application/json'},
    'body': RETURN_DATA_STR
  }
