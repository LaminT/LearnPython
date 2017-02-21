try:
	inp = raw_input("Enter Score:")
	score = float(inp)
	
except:
	print "Error, please enter numeric input"
	quit()
	
#print rate, hours
if score == 0.0 and 0.1 :
	print "Bad Score"
elif score >= 0.9 :
	print "A"
elif score >= 0.8 :
	print "B"
elif score >= 0.7 :
	print "C"
elif score >= 0.6 :
	print "D"
elif score < 0.6 :
	print "F"
	#pay = rate * 40 + (rate * 1.5 * (hours - 40))
#print pay
	