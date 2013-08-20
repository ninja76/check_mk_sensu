#!/usr/bin/python
import time
import os
import telnetlib

tn = telnetlib.Telnet('192.168.0.2','6556')
#print tn.read_all()
yourResult = tn.read_all()
yourResult = yourResult.split('\n')
tn.close()
# For testing I am just using a cached copy.  Need to stream in via nc 
#inputfile = open("out.txt", 'r')
#yourResult = os.system("telnet 192.168.0.2 6556")
# Placeholder until I bring it in from the command line
host = "windows.vizualmedium.com"
#yourResult = [line.split(',') for line in inputfile.readlines()]
c = 0
cc = 0
cpu_line = 0
ts = str(time.time()).split('.')[0]
for i in yourResult:
	c += 1
	var = 'mem'
	data = i;
	if '<<<mem>>>' in i:
		for x in range(0,8):
			print host + '.memory' + ' ' + str(yourResult[c+x]).split()[0][:-1]  + ' ' + str(yourResult[c+x]).split()[1] + ' ' + str(ts)
	if '<<<df>>>' in i:
		cc = c
		while str(yourResult[cc])[2:-4] not in '<<<ps>>>':		
			print host + '.' + 'disk' + '.' + str(yourResult[cc]).split()[-1][:-2] + ' ' + 'Total' + ' ' + str(yourResult[cc]).split()[2]  + ' ' + str(ts)
			print host + '.' + 'disk' + '.' + str(yourResult[cc]).split()[-1][:-2] + ' ' + 'Used' + ' ' + str(yourResult[cc]).split()[3] + ' ' + str(ts)
			print host + '.' + 'disk' + '.' + str(yourResult[cc]).split()[-1][:-2] + ' ' + 'Free' + ' ' + str(yourResult[cc]).split()[4] + ' ' + str(ts)
			print host + '.' + 'disk' + '.' + str(yourResult[cc]).split()[-1][:-2] + ' ' + 'PercentUsed' + ' ' + str(yourResult[cc]).split()[5][:-1] + ' ' + str(ts)
			cc += 1	
 

