Challenge: ret2win1

- Vulnerability: stack buffer overflow with ROP-capable gadgets present.
- Goal: craft a ROP chain to prepare arguments and call the target function.

Approach:
- Overflow 0x50 bytes, align the stack, then use `pop rdi`/`pop rsi` gadgets to set
  up register arguments for the function we want to call. The solver demonstrates
  the gadget sequence and placeholder argument values.

Notes:
- Replace placeholder argument values (e.g., 0xdeadbeef) as needed for the binary.
