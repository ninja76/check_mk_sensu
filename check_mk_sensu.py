import time
# For testing I am just using a cached copy.  Need to stream in via nc 
inputfile = open("out.txt", 'r')
# Placeholder until I bring it in from the command line
host = "windows.vizualmedium.com"
yourResult = [line.split(',') for line in inputfile.readlines()]
c = 0
cc = 0
cpu_line = 0
ts = str(time.time()).split('.')[0]
for i in yourResult:
	c += 1
	var = 'mem'
	data = i;
	if '<<<mem>>>' in str(i):
		for x in range(0,8):
			print host + '.memory' + ' ' + str(yourResult[c+x]).split()[0][2:-1]  + ' ' + str(yourResult[c+x]).split()[1] + ' ' + str(ts)
	if '<<<df>>>' in str(i):
		cc = c
		while str(yourResult[cc])[2:-4] != '<<<ps>>>':		
			print host + '.' + 'disk' + '.' + str(yourResult[cc]).split()[-1][:-7] + ' ' + 'Total' + ' ' + str(yourResult[cc]).split()[2]  + ' ' + str(ts)
			print host + '.' + 'disk' + '.' + str(yourResult[cc]).split()[-1][:-7] + ' ' + 'Used' + ' ' + str(yourResult[cc]).split()[3] + ' ' + str(ts)
			print host + '.' + 'disk' + '.' + str(yourResult[cc]).split()[-1][:-7] + ' ' + 'Free' + ' ' + str(yourResult[cc]).split()[4] + ' ' + str(ts)
			print host + '.' + 'disk' + '.' + str(yourResult[cc]).split()[-1][:-7] + ' ' + 'PercentUsed' + ' ' + str(yourResult[cc]).split()[5][:-1] + ' ' + str(ts)
			cc += 1	
 

