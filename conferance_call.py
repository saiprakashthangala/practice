import os,time,datetime
import device
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	cmdr="adb shell dumpsys telephony.registry | grep 'mCallState' > call_logs"+"&"
	os.system(cmdr)

def reject_call(div,num,num2):
	cmd1 ="adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num+""
	rc = os.system(cmd1)
	time.sleep(10)
	cmd1 ="adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num2+""
	rc = os.system(cmd1)
	time.sleep(10)
	cmd1 ="adb -s "+div+" shell am start -a android.intent.category.DEFAULT "
	rc = os.system(cmd1)
	time.sleep(10)
	cmd2 = "adb shell input  keyevent 5"
	#os.system(cmd2)
	cmd2 = "adb shell input  keyevent 6"
	#os.system(cmd2)
	return rc

def iter_status(iter,dev,num,num2):
	collect_logs()
	for i in range(iter):
		mind = reject_call(div,num,num2)
		if mind == 0:
			print "Test Passed"
		else:
			print "Test Failed"
		
div = device.main()
num = "9550767558"
num2="7799221479"
iter=1
iter_status(iter,div,num,num2)
		
