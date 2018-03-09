import os,time,datetime

def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	cmdr='adb logcat -b radio  > sms_log'+'&'
	os.system(cmdr)
def unlock_call(div,num):
		cmd1 ="adb shell input  keyevent 26"
		rc = os.system(cmd1)
		time.sleep(10)
		cmd2 = "adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num+""
		os.system(cmd2)
                time.sleep(10)
		return rc

def iter_status(iter,dev,num):
	collect_logs()
	for i in range(iter):
                unlk = unlock_call(div,num)
		if unlk == 0:
			print "Test Passed"
		else:
			print "Test Failed"
		
div = "9f6ad657"
num = "+919100122805"
iter=3
iter_status(iter,div,num)
		
