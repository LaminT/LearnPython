# Use the file name mbox-short.txt as the file name

import re
fname = input("Enter file name: ")
fh = open(fname)

numlist = list()
for line in fh:
	line = line.rstrip()
	x = re.findall('New Revision: ([0-9]+)', line)
	if len(x) == 1:
		val = float(x[0])
		numlist.append(val)
		average = sum(numlist) / len(numlist)
print 'Average:', average
			