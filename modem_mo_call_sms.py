'''
Before run the program device.py and Mo_num_msg.csv files having the same folder 
'''

import os,time,datetime,csv
import device
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('Airplane_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)		#create log folder
	os.chdir(mydir)			# change directry 
	cmdr='adb logcat -b radio > Mo_call_sms_log'+'&'
	os.system(cmdr)			# collecting log file

def number():
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	numbers=your_list[0]
	return random.choice(numbers[1::])
def iterations():
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	iters=your_list[2]
	return int(random.choice(iters[1::]))
def test_call(div,num):
	cmd="adb shell input  keyevent 3" 		#set home page
	os.system(cmd)	
	cmd1 ="adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num 
	rc = os.system(cmd1)				#call start 
	print " CALL CONNECTING ......... To ",num
	time.sleep(10)
	#cmd2 = "adb shell input  keyevent 6"		
	#os.system(cmd2)					#Call end 
	os.system(cmd)					#set home page
	return rc

def test_sms(div,num,text):
	cmd="adb shell input  keyevent 3"		#set home page
	os.system(cmd)
	cmd1="adb shell am start -a android.intent.action.SENDTO -d sms:"+num
	cmd2="adb shell input text $(echo {} | sed -e 's/ /\%s/g')".format(text)				
	cmd3 = "adb shell input keyevent 22"		
	cmd4="adb shell input keyevent 66"		
	rc=os.system(cmd1)				#launch messaging aplication
	os.system(cmd2)					#input data
	time.sleep(5)
	os.system(cmd3)					#click_right
	os.system(cmd4)					#click_Enter 
	os.system(cmd)					#set home page
	return rc

def iter_status(iteration,div,num):
	collect_logs()
	print "This program will execute "+str(iteration)+" Iterations"	
	for i in range(iteration):
		call= test_call(div,num)
		if call==0:
			print "Call connecting successfully"
		else:
			print "got error while connecting Call " 
			break;

		msg= test_sms(div,num,text)
		if msg==0:
			print "Message sending while successfully"
		else:
			print "got error while sending Call "
			break;			

		if call == 0 and msg==0:
			print "Test pass"
		elif call==0 and msg !=0:
			print "Call connecting successfully and Message sending while get error"
		elif call !=0 and msg==0:
 			print "Call connecting while get error and Message sending successfully"
		else:
			print "Test Failed"
		
div = device.main()	
print div,"conncected device"
num=number()
iteration=iterations()
iter_status(iteration,div,num)
		
