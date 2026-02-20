# RANDOM

You are given a binary named `random` (stripped, PIE, dynamically linked).

## Steps to solve

1. Extract the encrypted bytes from the binary using `objdump` or `hexdump`:

```bash
objdump -s -j .rodata random | grep -A 10 'Contents of section'  # or
hexdump -C random | less
```

Locate the hardcoded encrypted sequence and concatenate it into a single hex string.

Example extract (from objdump):

```
2060 ::::fccaccda ddc6c1ca dbdce6fc fbe6ecd4
2070 ::::fd9bc1cb c0c2f0c1 9bc2cd9c dddcf09b
2080 ::::dd9cc188 9ef0db9f 9ff0dd9b c1cb9fc2
2090 ::::8e8ed2
```

2. Paste all bytes into the solver script.

## Full Python solver

```python
# Random CTF task solver

def rolw(value, shift):
    """16-bit rotate left"""
    shift = shift & 7  # Only 3 bits matter for 16-bit rotate
    return ((value << shift) | (value >> (16 - shift))) & 0xFFFF


def transform_magic_number(magic):
    """Replicate the transformation in the binary"""
    rdx_1 = magic ^ 0xbeef
    for _ in range(5):
        rax_6 = ((rdx_1 << 7) ^ rdx_1) & 0xFFFF
        rdx_2 = rax_6 >> 9
        rax_7 = rax_6 ^ rdx_2
        rax_8 = ((rax_7 ^ (rax_7 << 8)) * 0x6255) & 0xFFFF
        temp = (rax_8 + 0x3619) & 0xFFFF
        rdx_1 = rolw(temp, temp & 7)
    return rdx_1


def solve():
    encrypted_hex = "fccaccdaddc6c1cadbdce6fcfbe6ecd4fd9bc1cbc0c2f0c19bc2cd9cdddcf09bdd9cc1889ef0db9f9ff0dd9bc1cb9fc28e8ed2"
    encrypted_bytes = bytes.fromhex(encrypted_hex)
    known_prefix = b"SecurinetsISTIC{"

    for magic in range(65536):
        key = transform_magic_number(magic)
        xor_key = (key & 0xFF) ^ ((key >> 8) & 0xFF)

        # Quick prefix check
        if (encrypted_bytes[0] ^ xor_key) != ord('S'):
            continue

        valid = True
        for i in range(len(known_prefix)):
            if (encrypted_bytes[i] ^ xor_key) != known_prefix[i]:
                valid = False
                break

        if valid:
            flag_bytes = bytearray(byte ^ xor_key for byte in encrypted_bytes)
            flag = flag_bytes.decode('ascii', errors='ignore')
            print(f"[+] FOUND MAGIC NUMBER: {magic} (0x{magic:04x})")
            print(f"[+] FLAG: {flag}")
            return flag

    print("[-] No valid magic number found")
    return None


if __name__ == "__main__":
    solve()
```

The script will brute-force all possible magic numbers, derive the XOR key, decrypt the flag, and print it when found.

## Flag

```
SecurinetsISTIC{R4ndom_n4mb3rs_4r3n'1_t00_r4nd0m!!}
```

---

Notes:

- This is a classic brute-force+key-derivation pattern — find the magic number, derive xor key, xor-decrypt.
- If runtime is slow, you can parallelize the outer loop (split magic range across workers).

