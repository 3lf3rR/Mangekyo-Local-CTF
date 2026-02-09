Challenge: ret2win0

- Vulnerability: classic stack buffer overflow leading to a `win` function.
- Goal: overwrite saved return to call `win` and get the flag.

Approach:
- Overflow with 0x50 bytes and set return to `win`. The solver sets `win+1` to
  avoid undesirable instructions at the exact function entry (common trick).

Notes:
- Update `DEBUG` in `solve.py` to test locally.
