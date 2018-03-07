import os,time,datetime
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	cmdr='adb logcat -b radio | grep  -i call > Call_log'+'&'
	os.system(cmdr)

def reject_call(div,num):
		cmd1 ="adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num+""
		rc = os.system(cmd1)
		time.sleep(5)
		cmd2 = "adb shell input  keyevent 6"
		os.system(cmd2)
		return rc

def iter_status(iter,dev,num):
	collect_logs()
	for i in range(iter):
		mind = reject_call(div,num)
		if mind == 0:
			print "Test Passed"
		else:
			print "Test Failed"
		
div = "HQ541YL17255"
num = "+919066516916"
iter=3
iter_status(iter,div,num)
		
