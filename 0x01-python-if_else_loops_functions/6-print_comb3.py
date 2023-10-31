#!/usr/bin/python3
j = 1
for i in range(0,100):
	if (i < 99):
		if ((i % 10) == 0):
			i = i + j
			j+=1
		print("{:02d}".format(i), end=', ')
	else:
		print("{:02d}".format(i), end='\n')
