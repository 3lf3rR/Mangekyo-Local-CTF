Challenge: Why would you call my system?

- Vulnerability: PIE binary with a vuln function that allows ROP and a sigreturn
  technique to perform an execve syscall.
- Goal: compute binary base from a leaked address, pivot to .bss, then use a
  crafted SigreturnFrame to call execve("/bin/sh",0,0).

Approach:
- Leak PIE base from the service output, compute gadgets/addresses relative to base.
- Perform a ROP pivot into .bss and craft a payload that triggers a sigreturn
  (building a SigreturnFrame) to set registers for `execve`.

Notes:
- `solve.py` contains comments explaining each stage (leak, pivot, sigreturn).
