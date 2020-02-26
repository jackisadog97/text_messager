# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="CRAB MEAT CRAB MEAT CRAB MEAT",
                     from_='+12058138171',
                     to='+610422585389'
                 )

print(message.sid)