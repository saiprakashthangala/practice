import os,time,datetime
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('Airplane_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	os.chdir(mydir)
	cmdr='adb logcat -b main | grep  -i AIRPLANE > AIRPLANE_log'+'&'
	os.system(cmdr)
def airplane_on():
		cmd ="adb shell settings put global airplane_mode_on 1;adb shell am broadcast -a android.intent.action.AIRPLANE_MODE" # Enable Airplane mode 
		rc = os.system(cmd)
		time.sleep(20)
		print "Airplane mode is on"
		return rc 
def airplane_off():
		cmd2 = "adb shell settings put global airplane_mode_on 0" # Disable Airplane mode
		rc=os.system(cmd2)
		time.sleep(20)
		print "Airplane mode is off"
		return rc
def iter_status(iterations,div):
	collect_logs()
	for i in range(iterations):
		print i+1
		on=airplane_on()
		off=airplane_off()
		if on == off:
			print "Test passed"
		else:
			print "Test Failed"
		
div = "HQ541YL17255"
iterations=3
iter_status(iterations,div)
