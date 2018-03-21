import os,time,datetime,csv,random
import device
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('data_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	os.chdir(mydir)
	cmdr='adb logcat -b radio  > data_log'+'&'
	os.system(cmdr)

def iterations():
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	iters=your_list[2]
	return int(random.choice(iters[1::]))

def data_on(div):
	cmd="adb shell input  keyevent 3"
	os.system(cmd)				# set home page 
	cmd1= "adb -s "+div+" shell svc data enable"
	try:
		rc=os.system(cmd1)	
		print "data enabled"
	except:
		print "Data not enabled "	
	time.sleep(10)
	return rc

def open_browse():
	cmd="adb shell input  keyevent 3"
	os.system(cmd)				#set home page
	cmd1= "adb -s "+div+" shell am start -a android.intent.action.VIEW -d "+address
	rc=os.system(cmd1)			# open browser 
	print "google opened"
	time.sleep(20)
	return rc
def not_browse():
	cmd="adb shell input  keyevent 3"
	os.system(cmd)				#set home page
	cmd1= "adb -s "+div+" shell am start -a android.intent.action.VIEW -d "+address
	rc=os.system(cmd1)			
	print "google notopened"
	time.sleep(10)
	return rc

def data_off():
	cmd="adb shell input  keyevent 3"
	os.system(cmd)				#set home page
	cmd1= "adb -s "+div+" shell svc data disable"
	rc=os.system(cmd1)
	print "data disabled"
	time.sleep(10)
	return rc

def iter_status(iterations,div,address):
	collect_logs()
	for i in range(iterations):
		on=data_on(div)
		browse=open_browse()
		off=data_off()
		browse1= not_browse()

div =device.main()
print div," device Connected "
address="http://google.com"
iterations=iterations()
iter_status(iterations,div,address)


