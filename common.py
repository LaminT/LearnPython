name = raw_input('Enter file name:')
handle = open(name)
text = handle.read()
words = text.split()

cou = dict()
for wrd in words:
	cou[wrd] = cou.get(wrd,0) + 1

maxval = None
maxkee = None
for kee, val in cou.items():
	if maxval == None or maxval < val:
		maxval = val
		maxkee = kee
print maxkee, maxval