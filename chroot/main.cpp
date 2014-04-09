/*
 * =====================================================================================
 *
 *       Filename:  chroot.cpp
 *
 *    Description:  挂在镜像，chroot环境
 *
 *        Version:  1.0
 *        Created:  2012年09月103日 17时41分04秒
 *       Revision:  none
 *       Compiler:  g++
 *
 *         Author:  yandong (www.yandong.org), toyandong@gmail.com
 *   Organization:  iie
 *
 * =====================================================================================
 */
#include <unistd.h>
#include <guestfs.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <sstream>
#include <sys/dir.h>
#include <sys/stat.h>
#include <signal.h>
using namespace std;
#define MAXLINE 1024


static void sig_pipe(int signo)
{
	printf("SIGPIPE caught\n");
	exit(1);
}


/*使用协同进程*/
int main(int argc, char **argv) 
{
	int n, fd1[2], fd2[2];
	pid_t pid;
	char line[MAXLINE];
	
	if(signal(SIGPIPE, sig_pipe) == SIG_ERR)
	{
		perror("signal error");
	}
	
	if(pipe(fd1) < 0 || pipe(fd2) <0)
	{
		perror("pipe error");
	}
	
	if((pid=fork()) < 0)
	{
		perror("fork error");
	}else if(pid > 0)/*parent*/
	{
		/*两个 半双工, 0读 1写*/
		close(fd1[0]);
		close(fd2[1]);
		/*挂载镜像 guestmount*/
		/*预处理*/
		/*chroot到geust的shell环境*/
		/*apt-get tazpkg yum安装*/
		
		
		while(fgets(line, MAXLINE, stdin) != NULL)
		{
			n = strlen(line);
			if(write(fd1[1], line , n) != n)
			{
				perror("write error");
			}
			if((n = read(fd2[0], line, MAXLINE)) <0 )
			{
				perror("read error");
			}
			if(0==n)
			{
				perror("child closed pipe");
			}
			line[n]=0;
			if(fputs(line, stdout) == EOF)
			{
				perror("fputs error");
			}
		}
		
		
	}else/*child*/
	{
		/*两个 半双工, 0读 1写*/
		close(fd1[1]);
		close(fd2[0]);
		
		/*重定向输入输出*/
		if(fd1[0] != STDIN_FILENO)
		{
			if(dup2(fd1[0], STDIN_FILENO) != STDIN_FILENO)
				perror("dup2 error");
			close(fd1[0]);
		}
		
		if(fd2[1] != STDOUT_FILENO)
		{
			if(dup2(fd2[1], STDOUT_FILENO) != STDOUT_FILENO)
				perror("dup2 error");
			close(fd2[1]);
		}
		
		/*chroot到guest的shell环境*/
		if(execl("/usr/sbin/chroot", "/usr/sbin/chroot", "/mnt/slitaz20/", "/bin/ash", (char *)0))
		{
			perror("execl error");
		}
	}

	return 0;
}





















