
import re
fname = input("Enter file name: ")
fh = open(fname)
sum = 0
for line in fh:
	line = line.rstrip()
	line = re.findall('([0-9]+)', line)
	
	for indek in line:
		indek = int(indek)
		print indek
		sum = sum + indek

print "Sum:",sum
	
		