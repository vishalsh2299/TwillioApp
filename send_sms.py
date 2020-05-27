from twilio.rest import Client
from TwilioApp import account_sid, auth_token, my_cell, my_twilio

client = Client(account_sid,auth_token)

my_msg = ''.join(['silly bob\n' for i in range(10)])

message = client.messages.create(to=my_cell, from_=my_twilio,
                                 body=my_msg)