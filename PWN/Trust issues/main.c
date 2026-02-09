/* compile: gcc -o main main.c
*/ 
#include <unistd.h>
#include <string.h>

#include <stdio.h>
#include <stdlib.h>


void setup(){
    setbuf(stdout,0);
    setbuf(stdin,0); 
    setbuf(stderr,0);
}
void main(){
    setup();
    char flag[0x38];
    FILE* fd = fopen("flag","r");
    fread(flag,1,0x38,fd);
    fclose(fd);
    char buf[0x50];
    puts("I trust u <3");
    read(0,buf,0x50);
    printf(buf);
    
    return;

}
