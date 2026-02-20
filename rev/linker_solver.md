# LINKER

ur giving a binary named main ,, and the only hint here is the task name ,, 

tracing the binarie's linkage we simple find the flag : 

```
ltrace -s 200 ./main
```

When prompted, type anything.

Example `ltrace` output:

```
printf("Enter password: ")                                  = 16
__isoc99_scanf(0x5631b9767015, 0x7ffd47221720, 0, 0Enter password: hello
)        = 1
strcmp("hello", "SecurinetsISTIC{L1nK4g3_1s_1mp0rt4nt!!}")  = 21
puts("ACCESS DENIED")                                       = 14
+++ exited (status 0) +++
```

Flag:

```
SecurinetsISTIC{L1nK4g3_1s_1mp0rt4nt!!}
```

