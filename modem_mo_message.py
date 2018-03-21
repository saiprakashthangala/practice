import os,time,datetime
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	cmdr='adb logcat -b radio  > sms_log'+'&'
	os.system(cmdr)
def test_sms(div,num,text):
		cmd="adb shell am start -a android.intent.action.SENDTO -d sms:"+num+" -e stream 'file:///storage/sdcard0/Sk.png/' -t image/png"
		cmd2="adb shell input text $(echo {} | sed -e 's/ /\%s/g')".format(text)
		time.sleep(10)
		cmd3 = "adb shell input keyevent 22"
		cmd4="adb shell input keyevent 66"
		rc=os.system(cmd)
		os.system(cmd2)
		os.system(cmd3)
		os.system(cmd4)
		return rc
def iter_status(ite,div,num):
	collect_logs()
	for i in range(ite):
		mind = test_sms(div,num,text)
		if mind == 0:
			print "Test passed"
		else:
			print "Test Failed"

			
text="saiprakash is a gud boy"
div = "HQ541YL17255"
num = "+917799221479"
iterations=3
iter_status(iterations,div,num)