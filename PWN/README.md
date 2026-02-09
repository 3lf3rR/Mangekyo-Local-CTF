# PWN Challenges — Quick Reference

A concise index of the challenges in this folder with the primary vulnerability
and a short description. Use this as a quick cheat-sheet when scanning the
problems or picking a solver to run.

| Challenge | Vulnerability | Short description |
|---|---|---|
| Domestic canary 🐤 | Stack canary leak + buffer overflow | Partial canary leaked in banner; reconstruct canary and overflow to reach `win`. |
| Hope Exploitation | Heap pointer XOR leak / UAF | Heap pointers are XORed; recover XOR key, compute flag address, overwrite pointer to print flag. |
| Why would you call my system? | PIE + Sigreturn ROP | Leak PIE base, pivot to `.bss`, craft a SigreturnFrame to call `execve("/bin/sh")`. |
| ret2win0 | Stack buffer overflow | Simple overflow to overwrite return and jump to `win`. |
| ret2win1 | ROP / ret2win | Overflow + ROP gadgets (`pop rdi`, `pop rsi`, ...) to set registers and call target gadget. |
| ret2win2 | Stack buffer overflow/ret2win | Overflow that writes controlled pointer(s) and returns to a function. |
| Trust issues | Format-string info leak | Use `%<index>$p` to leak stack pointers and reconstruct flag bytes. |

How to use
- Each challenge folder includes a `solve.py` script that contains the exploit. Set `DEBUG=1` inside a solver to test locally and adjust `context.terminal` if needed.
- To run a solver locally (example):

```bash
cd PWN/ret2win0
python3 solve.py
```

## Contact

If you'd like to credit me or get in touch, here are my social links:

- **Facebook:** https://www.facebook.com/m1taaz
- **LinkedIn:** https://www.linkedin.com/in/moetezzouari/

Thanks for checking out the challenges — happy hacking!

