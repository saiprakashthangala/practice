import os,time,datetime
import device, number
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('Call_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	os.chdir(mydir)
	cmdr='adb logcat -b radio | grep  -i call > Call_log'+'&'  # call Logs
	os.system(cmdr)
def test_call(div,num):
		cmd ="adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num # call start 
		rc = os.system(cmd)
		print " CALL CONNECTING ........"
		time.sleep(40)
		cmd2 = "adb shell input  keyevent 6" # Call end 
		os.system(cmd2)
		return rc
def iter_status(iteration,div,num):
	collect_logs()
	for i in range(iteration):
		call= test_call(div,num)
		if call == 0:
			print "Test passed"
		else:
			print "Test Failed"
		
div = device.main()	
print div,"conncected device "
num=str(number.number())
#num = "+917799221479"
iteration=3
iter_status(iteration,div,num)
		