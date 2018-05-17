try:
	N=int(raw_input())
	if(N>=1 and N<=100000):
	                      print "positive"
	elif(N>100000):
	               print "beyond the limit"
	elif(N<0): 
	          print "negative"	
	elif(N==0):
		print "zero"
except:
	print "enter a valid input"
