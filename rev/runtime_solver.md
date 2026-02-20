# RUNTIME

You are given a binary named `runtime`:

```
runtime: ELF 64-bit LSB pie executable, x86-64, dynamically linked, not stripped
```

After decompiling the binary ive found taht the flag is generated at runtime; it is not stored statically , so we need to use a debugger to fetch decrypted bytes at runtime from the memory .

## Steps to solve

### Step 1 – Start debugging

Open in GDB:

```bash
gdb ./runtime
```

- Start the program.
- Note the entry point address (example: `0x555555555100`).

### Step 2 – Set a breakpoint after the decode loop

The loop that constructs the flag ends at the `jne` after the `mmap@plt` call.

- Address of the `jne`: `0x555555555254`
- Set breakpoint:

```gdb
break *0x555555555254
run
```

### Step 3 – Fetch the flag bytes

- After hitting the breakpoint, inspect `rbx` where the flag is constructed:

```gdb
x/s $rbx
```

- Continue execution step by step (or use `continue`) until the full flag is revealed byte by byte.

### Step 4 – Flag

```
SecurinetsISTIC{Run1iM3_D3bUG_DUmP}
```

---



