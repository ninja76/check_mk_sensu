#!/usr/bin/python
import time
import os
import telnetlib
import sys

host = sys.argv[1]
port = "6556"

#open connection to port 6556 and parase output
tn = telnetlib.Telnet(host, port)
yourResult = tn.read_all()
yourResult = yourResult.split('\n')
tn.close()
c = 0
cc = 0
cpu_line = 0

#Get Epoch timestamp
ts = str(time.time()).split('.')[0]
for i in yourResult:
	c += 1
	var = 'mem'
	data = i;
	# Parse Memory Data
	if '<<<mem>>>' in i:
		for x in range(0,8):
			# Kick out Graphite formatted data
			print host + '.memory' + ' ' + str(yourResult[c+x]).split()[0][:-1]  + ' ' + str(yourResult[c+x]).split()[1] + ' ' + str(ts)
	# Parse Disk Data			
	if '<<<df>>>' in i:
		cc = c
		while str(yourResult[cc])[2:-4] not in '<<<ps>>>':
			# Kick out Graphite formatted data
			print host + '.' + 'disk' + '.' + str(yourResult[cc]).split()[-1][:-2] + ' ' + 'Total' + ' ' + str(yourResult[cc]).split()[2]  + ' ' + str(ts)
			print host + '.' + 'disk' + '.' + str(yourResult[cc]).split()[-1][:-2] + ' ' + 'Used' + ' ' + str(yourResult[cc]).split()[3] + ' ' + str(ts)
			print host + '.' + 'disk' + '.' + str(yourResult[cc]).split()[-1][:-2] + ' ' + 'Free' + ' ' + str(yourResult[cc]).split()[4] + ' ' + str(ts)
			print host + '.' + 'disk' + '.' + str(yourResult[cc]).split()[-1][:-2] + ' ' + 'PercentUsed' + ' ' + str(yourResult[cc]).split()[5][:-1] + ' ' + str(ts)
			cc += 1	
 

