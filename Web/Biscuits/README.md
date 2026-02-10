# Biscuits — Cookie Forgery via XOR Writeup (400 pts)

**Challenge name:** Biscuits  
**Author:** Rayene9052  
**Difficulty:** Medium 

---

## Overview

This challenge focuses on **insecure cookie-based authentication** combined with
a weak custom encryption scheme.

The application uses a **Base64-encoded XOR-encrypted cookie** to store session data.
By exploiting a **known-plaintext attack**, we can recover the XOR key, forge an admin
session, and access the protected `/admin` endpoint to retrieve the flag.

---

## Challenge Description

> Like usual  
> The flag is at `/admin`  

![Challenge description](Web/assets/Biscuits_chall.png)

---

## Initial Recon

Visiting the main page shows:

- Status: **Welcome, Guest**
- Role: **Guest**
- Access to `/admin` is denied

![Home page](home_biscuits.png)

Direct access to the admin endpoint:

```
/admin
```

Result:

![Access denied](access_denied.png)

---

## Cookie Analysis

Inspecting the browser cookies reveals a suspicious value:

```
session = CEsYAwkXBQQUFktXUE4CHgAKB0tBUE4EDwgQHUtXUAoEBxYcDg==
```

![Session cookie](session.png)

At first glance, Base64 decoding produces unreadable data:

![Base64 decode attempt](decoding_session.png)

This suggests an additional encoding or encryption layer.


## Cryptographic Weakness

XOR encryption is insecure when:

- The key is reused
- The plaintext is predictable

This allows a **known-plaintext attack**.

---

## Recovering the XOR Key

Using CyberChef:

1. Decode from Base64
2. XOR with known JSON structure

![Recover XOR key](start_xor.png)

Recovered key:

```
simplekey
```

---

## Decoding the Session

![Decoded session](what_we_see.png)

```json
{"username": "guest", "admin": false}
```

---

## Forging an Admin Cookie

Target payload:

```json
{"username": "admin", "admin": true}
```

Steps:

1. XOR with `simplekey`
2. Encode with Base64

![Forge admin session](end_xor.png)

---

## Admin Access

Replacing the cookie and refreshing `/admin`:

![Admin dashboard](final_flag.png)

---

## Flag

```
SecurinetsISTIC{b3rj0uli4_k3sa7_s47b1_x0rrrrrr}
```

---


---

## Source Code Analysis

Although the source is **not provided to players**, reviewing it explains the vulnerability:

```python
user = {
    "username": "guest",
    "admin": False
}

raw = json.dumps(user).encode()
xored = xor_data(raw, XOR_KEY)
encoded = base64.b64encode(xored).decode()

resp.set_cookie("session", encoded)
```

Admin access check:

```python
if user.get("admin") is True:
    return render_template("admin.html")
```

---

## Root Cause

- Client-controlled session state
- Weak XOR-based encryption
- No integrity or signature validation

---

## Key Takeaways

- Never store trust-sensitive data client-side
- XOR is not secure encryption
- Always use signed or server-side sessions

---

Clean cookie forgery challenge with a classic crypto pitfall.
