# sqli1 — Basic SQL Injection

## Category
Web

## Difficulty
Easy

---

## Description

The admin of this website has a secret hidden in his dashboard.

But… are you **him**?

Players are given only a login page and are told that the flag is accessible
**only if they manage to log in as the admin user**.

![Challenge description and points](/Web/assets/sqli1_chall.png)

---

## Initial Observation (Black‑Box)

The application provides a classic login form with:
- a username field
- a password field

Trying random credentials fails, but testing common SQL injection payloads
reveals abnormal behavior.

For example, using the following payload:

```
' OR 1=1--
```

allows bypassing authentication, but the dashboard shows:

> *You are not admin. No flag for you*

![Guest access](guest.png)

This indicates:
- Authentication was bypassed
- But the **role matters**
- The flag is shown **only for the admin user**

---

## Exploitation Strategy

Since the application distinguishes users by **username**, the goal is not just
to bypass authentication, but to **force the session to log in as `admin`**.

This means our payload must:
- Bypass the password check
- Explicitly select the `admin` user

---

## Successful Payload

Using the following payload in the **username field**:

```
admin'--
```

The password field can contain **any value**.

![Exploit payload](exploit.png)

This forces the backend to treat the user as `admin`, successfully bypassing
authentication **and** gaining admin privileges.

---

## Result

After logging in as admin, the dashboard reveals the flag:

![Solved challenge](solved.png)

```
SecurinetsISTIC{SQLi_Inj3ction_s0_common!!}
```

---

## Behind the Scenes (Source Code Explanation)


The login query is built like this:

```python
query = f"SELECT username FROM users WHERE username = '{username}' AND password = '{password}'"
```

User input is directly concatenated into the SQL query without sanitization.
The comment sequence (`--`) disables the password check entirely.


This results in the following SQL query:

```sql
SELECT username FROM users WHERE username = 'admin'--' AND password = '...'
```

---

## Conclusion

This challenge demonstrates a classic **authentication‑bypass SQL injection**.

Key lessons:
- Authentication bypass ≠ privilege escalation
- Always test role‑based logic
- Never concatenate user input into SQL queries
- Parameterized queries prevent this entirely

A foundational SQLi challenge that every beginner should master 🔥
