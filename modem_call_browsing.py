'''
Before executing this program, "device.py" and "Mo_num_msg.csv" files should present in same folder and check mobile dada disable
 
'''
import os,time,datetime,csv,random
import device;
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('call_data_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	os.chdir(mydir)
	cmd='adb logcat -b radio | grep call > call_log'+'&'
	os.system(cmd)
	cmd1='adb logcat -b main  > main_log'+'&'
	os.system(cmd1)
def number():				#get number from Mo_num_msg.csv 
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	numbers=your_list[0]
        return random.choice(numbers[1::])
def iterations():			#get no.of iterations from Mo_num_msg.csv 
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	iters=your_list[2]
        return int(random.choice(iters[1::]))
Total 5 (delta 3), reused 0 (delta 0)

def call(div,num):
	cmd="adb shell input  keyevent 3" 	#set home page
	os.system(cmd)	
	cmd1 ="adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num+"&"
	rc = os.system(cmd1)			# mo_call	
	time.sleep(10)
        return rc
def open_browse():
	cmd="adb shell input  keyevent 3" 	#set home page
	os.system(cmd)	
	cmd= "adb shell am start -a android.intent.action.VIEW -d http://votarytech.com"+"&"
        rc=os.system(cmd)			#opening web page
	time.sleep(5)	
	print "webpage is opened"
        time.sleep(5)
        return rc

def Data_enable(div):
	cmd="adb -s "+div+" shell svc data enable"
	rc=os.system(cmd)			# data enable
	print "mobile data Enabled" 
	time.sleep(4)
        return rc

def iter_status(iteration,div):
	collect_logs() 
	print "This program will execute "+str(iteration)+" Iterations"	
	for i in range(iteration):
		cal=call(div,num)
		if cal==0:
			print "Call connecting.. TO",num
		else:
			print "got error while connecting Call " 
			break;

		data = Data_enable(div)
		browse = open_browse()
		time.sleep(5)
		cmd="adb shell input  keyevent 6" 		
		os.system(cmd)				#End Call	
		if data==0 and browse==0:
			print "Data Browsing successfully "
		else:
			print "got error while data browsing  "
			break;			

		if cal == 0 and data==0 and browse ==0:
			print "Test pass"
		elif cal==0 and (data !=0 or browse !=0):
			print "Call connecting successfully and got error while Data Browsing"
		elif cal !=0 and data ==0:
 			print "got error while connecting Call "
		else:
			print "Test Failed"       
         
div = device.main()
num= number()
iteration=iterations()
iter_status(iteration,div)
