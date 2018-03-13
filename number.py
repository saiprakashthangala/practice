def number():
	print "Please Enter number \n Number should be valid phone number and 10 Digits" 
	number=raw_input(">>")
	length=len(number)
	state=False
	while state==False:
		length=len(number)
		if length==10 and number.isdigit():
			print number
			state=True
		else:
			print "Please Enter number \n Number should be valid phone number and 10 Digits" 
			number=raw_input(">>")
	return number	
			
if __name__=="__main__":

