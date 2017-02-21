import re
fh = open('mbox.txt')
fname = input("Enter a regular expression: ")
count = 0
for line in fh:
	line = line.rstrip()
	if re.search(fname, line): 
		count = count + 1

print ("mbox.txt had", count, "lines that matched", fname)
