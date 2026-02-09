/* compile: gcc -o main main.c
*/ 
#include <unistd.h>
#include <string.h>

#include <stdio.h>
#include <stdlib.h>

void gadgets(){
    __asm__("pop %rdi;ret;");
    __asm__("pop %rsi;ret;");
}
void win(long int a,long int b){
    char flag[0x38];
    FILE* fd = fopen("flag","r");
    fread(flag,1,0x38,fd);
    fclose(fd);
    if (a==0xdeadbeef && b==0xc0feebabe){
        printf("%s",flag);
    }
    
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
