from twilio.rest import Client
from decouple import config

account_sid = "AC6cf5f4e1fafdc4a8eaf198b0102d1d6b"
auth_token = config("TWILIO_AUTH_TOKEN")

def send_sms(body, to_number="+12505890269"):
  client = Client(account_sid, auth_token)

  message = client.messages.create(
    body=body,
    from_="+12057828390",
    to=to_number
)
  print(message.sid)

if __name__ == "__main__":
  send_sms(body="Hello from Python!")