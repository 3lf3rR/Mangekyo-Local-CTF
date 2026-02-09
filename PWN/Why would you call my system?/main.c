/*
SROP
should call read  , overwrite 'i'
prepare everything in bss
then ret2syscall with i=15 ( sigreturn )
rsp = somewhere bss, rdi = &"bin/sh" rsi=0 rdx=0
rip = syscall
rax = 59
compile : gcc main.c -o main -fno-stack-protector -Wl,-z,relro,-z,now
*/
#include <stdio.h>
#include <stdlib.h>

void callme(){
    __asm__("syscall;");
}
void setup(){
    setbuf(stdout,0);
    setbuf(stdin,0); 
    setbuf(stderr,0);
}
int vuln(){
    unsigned long int i=0x1337;
    char buf[0x20];
    printf("I have %li things to do!\n",&vuln);
    fgets(buf,0x200,stdin);
    if(i==10) exit(0xdead);
    return i;
}
void main(){
    setup();
    vuln();
}

