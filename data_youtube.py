import os,time,datetime
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	cmdr='adb logcat -b radio  > sms_log'+'&'
	os.system(cmdr)

def Data_enable(div):
		cmd="adb -s "+div+" shell svc data enable"
		rc=os.system(cmd)
		print "mobile data Enabled" 
		time.sleep(5)
                return rc

def open_browser():
             cmd= "adb -s "+div+" shell am start -a android.intent.action.VIEW -d http://www.youtube.com/watch?v=xko3vld5Wds"
             rc=os.system(cmd)
             print "google opened"
             time.sleep(5)
             return rc
def not_browser():
             cmd= "adb -s "+div+" shell am start -a android.intent.action.VIEW -d http://www.youtube.com/watch?v=xko3vld5Wds"
             rc=os.system(cmd)
             print "google notopened"
             time.sleep(5)
             return rc

def Data_disable(div):
		cmd="adb -s "+div+" shell svc data disable"
		rc=os.system(cmd)
		print "mobile data Disable"
		time.sleep(5)
                return rc


def iter_status(iterations,div):
        collect_logs()
        for i in range(iterations):
                print i+1
                on=Data_enable(div)
                on1=open_browser()
                off=Data_disable(div)
                off1=not_browser()
div = "HQ541YL17255"
iterations=3
iter_status(iterations,div)

