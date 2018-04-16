import os,time,datetime,csv,random
import device
''' Before run the program device.py and Mo_num_msg.csv files having the same folder 
'''
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('sms+sms_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)		#create log folder
	os.chdir(mydir)			# change directry 
	cmdr='adb logcat -b radio  > sms+sms_log'+'&'
	os.system(cmdr)			# collecting log file
def number1():
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	global numbers
	numbers=your_list[0]
	global num1
	num1=random.choice(numbers[1::])
	return num1
def number2():
	numbers.remove(num1)
        num2=random.choice(numbers[1::])
	return num2
def message():
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	msg=your_list[1]
	return random.choice(msg[1::])
def iterations():
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	iters=your_list[2]
	return int(random.choice(iters[1::]))
def test_sms(div,numm1,numm2,text):
	cmd="adb shell input  keyevent 3"		
	os.system(cmd)					#set home page
	cmd1="adb shell am start -a android.intent.action.SENDTO -d sms:"+numm1+","+numm2
	cmd2="adb shell input text $(echo {} | sed -e 's/ /\%s/g')".format(text)
	cmd3 = "adb shell input keyevent 22"
	cmd4="adb shell input keyevent 66"
	rc=os.system(cmd1)				# open msg app and take TO addrese
	time.sleep(5)
	os.system(cmd2)					# Message text Entry
	time.sleep(5)
	os.system(cmd3)				
	time.sleep(2)
	os.system(cmd4)					# Enter send button
 	os.system(cmd)
	return rc
def iter_status(ite,div,numm1,numm2,text):
	collect_logs()
	print "This program will execute "+str(ite)+" Iterations"	
	for i in range(ite):
		msg = test_sms(div,numm1,numm2,text)
		if msg == 0:
			print "Test passed"
		else:
			print "Test Failed"
			break;
div =device.main()
print div,"conncected device"
numm1 = number1()
numm2=number2()
text=message()
print "'",text,"'" ,"\n This message is sending .....TO ",numm1,"&",numm2 
iteration=iterations()
iter_status(iteration,div,numm1,numm2,text)
