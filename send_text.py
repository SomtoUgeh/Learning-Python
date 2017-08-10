from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC00bba6e64fbba6182fd2a888eeb0cf8c"
# Your Auth Token from twilio.com/console
auth_token  = "476fffbff28338b05cf41621ac676cd2"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+2348135110477", 
    from_="+1 415-903-7868 ",
    body="Hi, its Somto. Have a wonderful day!")

print(message.sid)

