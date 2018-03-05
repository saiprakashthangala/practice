import os,time,datetime
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('Data_ON_OFF_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	os.chdir(mydir)
	cmdr='adb logcat -b > Data_log'+'&'
	os.system(cmdr)
def Data_enable(div):
		cmd="adb -s "+div+" shell svc data enable"
		rc=os.system(cmd)
		print "mobile data Enabled" 
		time.sleep(5)
		return rc
def Data_disable(div):
		cmd="adb -s "+div+" shell svc data disable"
		rc=os.system(cmd)
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


div = "HQ541YL17255"
iterations=3
iter_status(iterations,div)
