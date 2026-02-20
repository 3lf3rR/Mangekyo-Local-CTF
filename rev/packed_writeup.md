# Packed — Short Humanized Write-up

A compact, clear set of steps to solve the **Packed** task from MANGEKYO ctf.

## Steps

ur giving a binary 'main'

1. **Spot the packer**

   - Run `file main` and `strings main `. If you see `UPX!` the binary is UPX-packed.

2. **Unpack**

   - Make a copy and unpack with UPX:
     ```bash
     cp main main.packed
     upx -d main.packed
     ```
   - Verify the copy is now unpacked (re-run `file` / `strings`).

3. **Quick static check**

   - Open the unpacked binary in your decompiler (Ghidra/IDA/radare2). Look for:
     - A hard-coded byte array (`enc_flag`).
     - A small loop that XORs each byte with a single-byte key.

4. **Run the solver**

   - Use this Python script to reproduce the decryption and print the flag.

```python
#!/usr/bin/env python3
enc_flag = [
    0x64,0x52,0x54,0x42,0x45,0x5e,0x59,0x52,0x43,0x44,0x7e,0x64,
    0x63,0x7e,0x74,0x4c,0x60,0x04,0x5b,0x5b,0x68,0x62,0x67,0x6f,
    0x68,0x06,0x44,0x68,0x03,0x68,0x70,0x07,0x07,0x53,0x68,0x40,
    0x03,0x4e,0x68,0x43,0x07,0x68,0x5b,0x04,0x03,0x45,0x59,0x68,
    0x67,0x03,0x54,0x7c,0x06,0x59,0x70,0x68,0x74,0x07,0x59,0x54,
    0x04,0x47,0x43,0x16,0x16,0x4a,0x00
]
key = 0x37
print(bytes(b ^ key for b in enc_flag if b != 0).decode())
```

5. **Result**
   - Running the script prints the flag:
     `SecurinetsISTIC{W3ll_UPX_1s_4_G00d_w4y_t0_l34rn_P4cK1nG_C0nc3pt!!}`

---



