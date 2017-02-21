fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)

counts = dict()

for line in fh:
	if not line.startswith('From ') : continue
	word = line.split()
	word = word[5]
	word = word.split(':')
	word = word[0]
	counts[word] = counts.get(word, 0) + 1

for k, v in sorted(counts.items(), None):
    print k, v