import os
from twilio.rest import Client
import requests
from dotenv import load_dotenv
import json

# CONFIG
load_dotenv()
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token  = os.getenv('TWILIO_AUTH_TOKEN')
consumers   = os.getenv('AFFIRMATION_SMS_CONSUMERS').split(',')
from_       = os.getenv('FROM')
testing     = os.getenv('TESTING') == 'true'

print_seperator = "-" * 10

config_print = f'''
  account_sid: {account_sid}
  auth_token: {auth_token}
  consumers: {consumers}
  testing: {testing}
'''

client = Client(account_sid, auth_token)

if testing:
  consumers = consumers[0]

def main(client=client, consumers=consumers):
  r = requests.get('https://www.affirmations.dev/', headers={"Accept": "application/json"})
  
  message = "AffirmationSMS: "
  if r.status_code == 200:
    message += r.json()["affirmation"]
  else:
    message +=  "Sorry there appears to be a problem with the AffirmationSMS service today. Don't worry suisuss will have gotten this message too, and will get around to fixing the service ASAP. Thank you for your understanding"

  message_response = client.api.account.messages.create(
          body   =message,
          from_  =from_,
          to     =consumers
      )



  message_print = f'''
  status_code: {r.status_code}
  message: "{message}"
  message_response: {message_response.sid}
  '''

  print(message_print)
  


if __name__ == '__main__':
  print("Executing...")
  print(config_print)
  main()
  print("Done")
  print(print_seperator)