import os,time,datetime
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	cmdr='adb logcat -b radio | grep  -i call > Call_log'+'&'
	os.system(cmdr)
def test_call(div,num):
		cmd ="adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num+""
		rc = os.system(cmd)
		time.sleep(10)
		cmd2 = "adb shell input  keyevent 6"
		os.system(cmd2)
		return rc
def iter_status(iter,dev,num):
	collect_logs()
	for i in range(iter):
		mind = test_call(dev,num)
		if mind == 0:
			print "Test passed"
		else:
			print "Test Failed"
		
div = "HQ541YL17255"
num = "+917799221479"
iter=3
iter_status(iter,div,num)
		