#!/usr/bin/python
import socket
import random
stuff = ['chikkenz', 'hax', 'niggaz']
network = 'irc.freenode.com'
port = 6667
owner = "IRC_ROBOT"
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect (( network, port))
irc.send ( 'NICK IRC_ROBOT\r\n' )
irc.send ( 'USER PyIRC PyIRC PyIRC :Python IRC\r\n' )
irc.send ( 'JOIN #test_irc \r\n' )
irc.send ( 'PRIVMSG #test_irc : 大家好\r\n' )
#=======
while True:
   data = irc.recv ( 4096 )
   #irc.send(data)
   lines = data.split('\r\n')
   for line in lines:
      word = line.split()
      print(word)
      #be live
      if line.find ( 'PING' ) != -1:
         irc.send ( 'PONG ' + word[1] + '\r\n' )
         #COMMANDS:
      if len(word) > 1:
		  if word[1] == 'PRIVMSG':
				irc.send('PRIVMSG '+word[2]+' :' +word[3]+'\r\n')
				if word[0].split('!')[0] == owner: # Put priveleged commands in this indented block.
					if line.find('!IRC_ROBOT') != -1:
						irc.send('PRIVMSG #test_irc :hi'+random.choice(stuff)+'?')
				if line.find('!version') != -1:
					irc.send('PRIVMSG #test_irc :I am version 1.0\r\n')
				if line.find('hello') != -1:
					irc.send('PRIVMSG #test_irc :Cocks!\r\n')
				if line.find('!quit') != -1:
					irc.send('PRIVMSG '+owner+' :QUITTING\r\n')
					irc.send('QUIT\r\n')
					irc.close()
				if word[3] == ('!status'):
				   irc.send('PRIVMSG #test_irc : Working')
   print (data)

