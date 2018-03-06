import os,time,datetime
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('modem_mo_call_sms_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	os.chdir(mydir)
	cmdr='adb logcat -b radio | grep  -i call > Call_sms_log'+'&'
	os.system(cmdr)
def test_call(div,num):
		cmd ="adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num+""
		rc = os.system(cmd)
		
		#time.sleep(10)
		#cmd2 = "adb shell input  keyevent 6"
		#os.system(cmd2)
		return rc

def test_sms(div,num,text):
		cmd="adb shell am start -a android.intent.action.SENDTO -d sms:"+num
		cmd2="adb shell input text $(echo {} | sed -e 's/ /\%s/g')".format(text)
		#time.sleep(10)
		cmd3 = "adb shell input keyevent 22"
		cmd4="adb shell input keyevent 66"
		rc=os.system(cmd)
		os.system(cmd2)
		os.system(cmd3)
		os.system(cmd4)
		return rc
	
def iter_status(iteration,div,num,text):
	collect_logs()
	for i in range(iteration):
		call = test_call(div,num)
		if call !=0:
			print "Test Fail"
			break
		else :
			print "Pass"
		sms =test_sms(div,num,text)
		if sms !=0:
			print "Test fail"	
			break
		else:
			print "Test pass"
			break;
		
		
text= "keee thanks"
div = "HQ541YL17255"
num = "+917799221479"
iteration=3
iter_status(iteration,div,num,text)
		