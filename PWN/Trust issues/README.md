Challenge: Trust issues

- Vulnerability: format-string / information leak.
- Goal: discover stack addresses via `%i$p` style format-string and reconstruct the flag.

Approach:
- The solver iterates over several stack indexes, sends `%<index>$p`, and collects
  non-NULL pointers. These are converted from hex strings and concatenated to form
  the flag bytes.

Notes:
- Tweak the index range if the layout changes; avoid crashing the service.
