#include <stdio.h> 
#include <stdlib.h> 
#include <errno.h> 
#include <string.h> 
#include <unistd.h>
#include <sys/types.h> 
#include <netinet/in.h> 
#include <netdb.h>
#include <sys/socket.h> 
#include <sys/wait.h> 

#define PORT 6667 /* 客户机连接远程主机的端口 */  
#define MAXDATASIZE 4096 /* 每次可以接收的最大字节 */  

/**
 *功能	: count the number of a character in a string 
 *参数	: 
 * */
int count_char(char *str, char c) 
{  
    int count = 0;  
    char *p = str;  
    while ( *p ) {  
        if ( *p == c )  
            count++;  
        p++;  
    }  
    return count;  
} 

/**
 *功能	: 将一个string 分割进word中，使用之后需要释放word内存
 *参数	: 
 * */
int splitString(char ***words, char *line, char delim)
{  
    int word_counter = count_char(line, delim) + 1;  
    *words = (char **) malloc(sizeof(char *) * word_counter);  
    int i = 0;  
    char *p = line;  
    while ( 1 ) {  
        char *s = p;  
        p = strchr(p, delim);  
        int len = ( p ) ? p - s : strlen(s);  
        (*words)[i] = (char *) malloc(sizeof(char) * (len + 1));  
        strncpy((*words)[i], s, len);  
        (*words)[i][len] = 0;  
        if ( !p ) break;  
        p++;  
        i++;  
    }  
    return word_counter;  
} 

ssize_t my_send(int sockfd,const void *buf, ssize_t len, int flags)
{
	ssize_t result;
	if ( (result=send(sockfd, buf, len, flags)) == -1)  
	{
		perror("send");  
		close(sockfd);  
		exit(0);  
	}
	return result;
}

int main(int argc, char *argv[])  
{  
	int sockfd, numbytes;  
	char buf[MAXDATASIZE];  
	struct hostent *he;  
	
	char *dataLine=NULL;
	char **word;
	char sendBuf[MAXDATASIZE];
	int count;
	
	char *useName="cdecl";
	char chanlList[][20]={"#test_irc","00"};
	char *helloWord="大家好,目前我可以解析c语言的声明，使用方法 cdecl char *p;";
	
	int sendBufLen;
	
	struct sockaddr_in their_addr; /* connector's address information */  
	
	if ((he=gethostbyname("irc.freenode.com")) == NULL) 
	{ /* get the host info */  
		perror("gethostbyname");  
		exit(1);  
	} 
	if ((sockfd = socket(AF_INET, SOCK_STREAM, 0)) == -1)
	{  
		perror("socket");  
		exit(1);  
	} 
	their_addr.sin_family = AF_INET; /* host byte order */  
	their_addr.sin_port = htons(PORT); /* short, network byte order */  
	their_addr.sin_addr = *((struct in_addr *)he->h_addr);  
	bzero(&(their_addr.sin_zero), sizeof(their_addr.sin_zero)); /* zero the rest of the struct */  
	printf("connect ...\n");
	if (connect(sockfd, (struct sockaddr *)&their_addr,sizeof(struct sockaddr)) == -1) 
	{  
		perror("connect");  
		exit(1);  
	}
	
	/*连接设置*/
	sendBufLen=snprintf(sendBuf, MAXDATASIZE,"NICK %s\r\n",useName);
	send(sockfd, sendBuf, sendBufLen, 0);
	
	sendBufLen=snprintf(sendBuf, MAXDATASIZE, "USER %s 8 * : yandong\r\n",useName); 
	send(sockfd, sendBuf, sendBufLen, 0);
	
	int i=0;
	while(strcmp(chanlList[i], "00"))
	{
		sendBufLen=snprintf(sendBuf, MAXDATASIZE, "JOIN %s\r\n",chanlList[i]);
		send(sockfd, sendBuf, sendBufLen, 0);
		sendBufLen=snprintf(sendBuf, MAXDATASIZE, "PRIVMSG %s : %s\r\n", chanlList[i], helloWord);
		send(sockfd, sendBuf, sendBufLen, 0);
		i++;
	}
	
	printf("recv send\n");
	while ((numbytes=recv(sockfd, buf, MAXDATASIZE, 0)) != -1)
	{  
		buf[numbytes]='\0';
		dataLine = strtok(buf, "\r\n");
		printf("read dataLine: %s \n", dataLine);
		while(NULL!=dataLine)
		{
			count=splitString(&word, dataLine, ' ');
			if(strstr(dataLine, "PING")!=NULL)
			{
				/*ping pong相应*/
				sendBufLen=snprintf(sendBuf, MAXDATASIZE, "PONG %s\r\n", word[1]);
				send(sockfd, sendBuf, sendBufLen, 0);
				free(word);
				dataLine = strtok(NULL, "\r\n");
				continue;
			}
			
			if(!strcmp(word[1], "PRIVMSG"))
			{
				printf("PRIVMSG...\n");
			}
			
			free(word);
			dataLine = strtok(NULL, "\r\n");
		}
	}
	
	if(-1 == numbytes)
	{
		perror("recv");  
		exit(1); 
	}
	close(sockfd);  
	return 0;  
}  