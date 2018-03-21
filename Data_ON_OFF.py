import os,time,datetime,csv,random
import device
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('Data_ON_OFF_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	os.chdir(mydir)
	cmdr='adb logcat -b > Data_log'+'&'
	os.system(cmdr)
def iterations():
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	iters=your_list[2]
	return int(random.choice(iters[1::]))

def Data_enable(div):
	cmd="adb shell input keyevent 3"
	os.system(cmd)			#set home page 
	cmd1="adb -s "+div+" shell svc data enable"
	rc=os.system(cmd1)
	print "mobile data Enabled" 
	time.sleep(5)
	return rc
def Data_disable(div):
	cmd="adb shell input keyevent 3"
	os.system(cmd)			#set home page
	cmd1="adb -s "+div+" shell svc data disable"
	rc=os.system(cmd1)
	print "mobile data Disable"
	time.sleep(5)
	return rc
def iter_status(ite,div):
	collect_logs()
	for i in range(ite):
		on= Data_enable(div)
		off=Data_disable(div)
		if on==off:
			print "Test passed"
		else:
			print "Test Failed"


div =device.main()
iterations=iterations()
iter_status(iterations,div)
