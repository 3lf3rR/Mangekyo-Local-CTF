/* compile: gcc -o main main.c -pie -no-pie -fno-stack-protector
*/ 
#include <unistd.h>
#include <string.h>

#include <stdio.h>
#include <stdlib.h>


void win(){
    system("/bin/sh");
    
}

void setup(){
    setbuf(stdout,0);
    setbuf(stdin,0); 
    setbuf(stderr,0);
}
void main(){
    setup();
    char buf[0x50];
    read(0,buf,0x90);    
    return;

}
