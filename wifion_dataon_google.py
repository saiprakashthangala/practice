import os,time,datetime
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('wifion_dataon_google_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	cmdr='adb logcat -b radio  > radio_log'+'&'
	os.system(cmdr)
	cmde='adb logcat -b event  > event_log'+'&'
	os.system(cmde)

def wifi_on():
             cmd= "adb -s "+div+" shell svc wifi enable"
             rc=os.system(cmd)
             print "wifi enabled"
             time.sleep(10)
             return rc
def Data_enable(div):
		cmd="adb -s "+div+" shell svc data enable"
		rc=os.system(cmd)
		print "mobile data Enabled" 
		time.sleep(10)
                return rc

def google():
             cmd= "adb -s "+div+" shell am start -a android.intent.action.VIEW -d http://google.com"
             rc=os.system(cmd)
             print "google opened"
             time.sleep(20)
             return rc

def iter_status(iterations,div):
        collect_logs()
        for i in range(iterations):
                print i+1
                on=wifi_on()
                on1=Data_enable(div)
                open1=google()

div = "ZX1D64GJW6"
iterations=3
iter_status(iterations,div)

