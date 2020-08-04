#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <netdb.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define PORTNUMBER 12543

int main(void)
{
    int resultado;
	int s;
	int longitud;
    char buf[1024];
    char hostname[64];
    struct hostent *hp;
    struct sockaddr_in name;

    gethostname(hostname,sizeof(hostname));

    hp = gethostbyname(hostname);
    
    s = socket(PF_INET,SOCK_DGRAM,0);
    name.sin_family=AF_INET;
    name.sin_port=htons(PORTNUMBER);

    memcpy(&name.sin_addr,hp->h_addr_list[0],hp->h_length);
    longitud = sizeof(struct sockaddr_in);
    
    
    while((resultado = read(0,buf,sizeof(buf)))>0)
		sendto(s,buf,resultado,0, (struct sokaddr*) &name,longitud);
   
    close(s);
}