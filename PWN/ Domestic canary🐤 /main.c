/* compile: gcc -o main main.c -pie -no-pie
*/ 
#include <unistd.h>
#include <string.h>

#include <stdio.h>
#include <stdlib.h>

void win(){
    printf("Ok you got me !! GG <3\n");
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
    printf("Yo bro i got you sth! %s\n",buf+0x58+1);
    read(0,buf,112);
    
    if (strlen(buf)>0x50){
        printf("what kind of person do you think i am ?");
        exit(0);}
    return;

}
