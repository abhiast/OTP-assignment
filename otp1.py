import random
from twilio.rest import Client


account_sid = "AC5e2c13017a36a96c62527e24281cf9f1"
auth_token = "50d82397d702b678b5fed876374279a7"
twilio_number = '+13233067978'
target_number = '+918623043699'

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_via_sms(phone_number, otp):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Your OTP is: {otp}",
        from_=twilio_number,
        to=phone_number
    )
    print("OTP sent successfully.")

if __name__ == "__main__":
    otp = generate_otp()
    send_otp_via_sms(target_number, otp)
