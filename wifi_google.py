import os,time,datetime
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime(wifi_google_'%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	cmdr='adb logcat -b radio  > radio_log'+'&'
	os.system(cmdr)
	cmde='adb logcat -b event  > event_log'+'&'
	os.system(cmde)


def wifi_on():
             cmd= "adb -s "+div+" shell svc wifi enable"
             rc=os.system(cmd)
             print "wifii enabled"
             time.sleep(5)
             return rc

def open_browse():
             cmd= "adb -s "+div+" shell am start -a android.intent.action.VIEW -d http://google.com"
             rc=os.system(cmd)
             print "google opened"
             time.sleep(5)
             return rc
def not_browse():
             cmd= "adb -s "+div+" shell am start -a android.intent.action.VIEW -d http://google.com"
             rc=os.system(cmd)
             print "google notopened"
             time.sleep(5)
             return rc

def wifi_off():
             cmd= "adb -s "+div+" shell svc wifi disable"
             rc=os.system(cmd)
             print "wifii disabled"
             time.sleep(5)
             return rc

def iter_status(iterations,div):
        collect_logs()
        for i in range(iterations):
                print i+1
                on=wifi_on()
                browse= open_browse()
                off=wifi_off()
                browse1= not_browse()
div = "HQ541YL17255"
iterations=3
iter_status(iterations,div)

