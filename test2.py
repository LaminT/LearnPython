numlist = list()
while True:
	inp = raw_input('enter number: ')
	if inp == 'done':break
	try:
		value = float(inp)
	except:
		print 'Invalid input'
		continue
numlist.append(value)
average = sum(numlist) / len(numlist)
print 'Average:', average