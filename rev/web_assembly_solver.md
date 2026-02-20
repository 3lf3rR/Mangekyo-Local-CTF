# WEBASSEMBLY ATTACH

You are given the following files:

```
Dockerfile  index.html  puzzle.wasm  readme.txt
```

The task hint: a WebAssembly module is loaded in the web app using JavaScript:

```javascript
fetch('puzzle.wasm')
  .then(res => res.arrayBuffer())
  .then(bytes => WebAssembly.instantiate(bytes, {}))
  .then(obj => {
    wasmInstance = obj.instance;
  });
```

## Steps to solve

### Step 1 – Decompile the WebAssembly

```bash
wasm-decompile puzzle.wasm -o puzzle.dcmp
```

This generates a readable pseudo-C file.

- At offset 64: a 3-byte block `Bn\15`
- At offset 80: a 50-byte encrypted blob

In the exported `validate()` function:

```c
if (b != 50) return 0;
int seed = d_a[0] & 255;   // 0x42
int a    = d_a[1] & 255;   // 0x6e
int c    = d_a[2] & 255;   // 0x15

for (int i = 0; i < 50; i++) {
    seed = (seed * a + c) & 0xff;
    int ks = seed;
    int enc = data_80[i];
    int dec = enc ^ ks;
    if (input[i] != dec) return 0;
}
return 1;
```

It is a simple XOR with an LCG keystream.

### Step 2 – Extract the encrypted bytes

From the decompiled output:

```text
c6 7c 12 25 1e 59 d2 c3 c4 fe e4 e3 fe f4 cc 84
c1 84 d9 e8 c0 84 d5 e8 d4 87 c2 db d3 e8 df c2
d9 d3 db 84 e8 d6 c4 c4 84 da d5 db ce 96 96 96 ca
```

### Step 3 – Recreate the generator in Python

```python
# WebAssembly attach task solver

seed, a, c = 0x42, 110, 21
enc = [
0xc6,0x7c,0x12,0x25,0x1e,0x59,0xd2,0xc3,0xc4,0xfe,0xe4,0xe3,0xfe,0xf4,
0xcc,0x84,0xc1,0x84,0xd9,0xe8,0xc0,0x84,0xd5,0xe8,0xd4,0x87,0xc2,0xdb,
0xd3,0xe8,0xdf,0xc2,0xd9,0xd3,0xdb,0x84,0xe8,0xd6,0xc4,0xc4,0x84,0xda,
0xd5,0xdb,0xce,0x96,0x96,0x96,0xca
]

flag = []
for e in enc:
    seed = (seed * a + c) & 0xff
    flag.append(e ^ seed)

print(bytes(flag).decode())
```

### Step 4 – Run the solver

```bash
python3 solve.py
```

### Flag

```
SecurinetsISTIC{3v3n_w3b_c0uld_hundl3_ass3mbly!!!}
```

---



