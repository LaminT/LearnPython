fhand = open('romeo.txt')
counts = dict() 
for line in fhand:
	words = line.split()
	for word in words:
		wrd = word.lower()
		counts[wrd] = counts.get(wrd, 0) + 1

flipped = list()
for k, v in counts.items() :
	newtup = (v, k)
	flipped.append(newtup)

flipped.sort(reverse=True)

for kay, val in flipped[:5]:
	print kay, val