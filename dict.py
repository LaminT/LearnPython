name = raw_input("Enter file name: ")
if len(name) < 1 : name = "mbox-short.txt"

handle = open(name)
counts = dict() 

for line in handle:
	word = line.split()
	if line.startswith('From ') : 
		counts[word[1]] = counts.get(word[1], 0) + 1
		
bigcount = None
bigword = None
for word,count in counts.items():
	if bigcount == None or count > bigcount:
		bigword = word
		bigcount = count

print bigword, bigcount
