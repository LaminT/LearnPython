fh = open("C:\Users\Lata01\Desktop\driftinfo.txt", "r")

count = 0
for line in fh:
	print line.strip()
	count = count + 1
print count,"Lines"
	