#This program is to send SMS to phone. It uses twilio API
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf9f7979e6452e5e16953163109083aab"
# Your Auth Token from twilio.com/console
auth_token  = "804f65441fce204ee12aaba9a1130e62"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+6596102208", 
    from_="+18062166002",
    body="Hello Monic!")

print(message.sid)


