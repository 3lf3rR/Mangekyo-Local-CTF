Challenge: ret2win2

- Vulnerability: simple stack buffer overflow allowing overwrite of return address.
- Goal: overwrite saved return to jump to a function that yields the flag.

Approach:
- Overflow the buffer with 0x50 bytes, then write controlled pointers. We jump to 0x4011a1 to bypass if() checks.

