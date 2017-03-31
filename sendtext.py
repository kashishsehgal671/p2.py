from twilio.rest import TwilioRestClient

account_sid = "AC3801547f4d3c43d346fed2e5f9ec74a4" # Your Account SID from www.twilio.com/console
auth_token  = "199fdeadad8c8f030e923619564a115e"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello . How you doing? ",
    to="+918800362127",    # Replace with your phone number
    from_="+16199284927") # Replace with your Twilio number

print(message.sid)
