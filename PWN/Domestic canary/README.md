Challenge: Domestic canary

- Vulnerability: stack canary bypass via leaked partial canary and buffer overflow.
- Goal: reconstruct the stack canary from a leak and craft a payload that preserves
  the canary while overwriting the return address to call `win`.

Approach:
- Parse the leaked partial canary from the program banner, reconstruct the full
  8-byte canary, then place it in the payload at the correct offset before the
  return address. The solver demonstrates this reconstruction and payload layout.

