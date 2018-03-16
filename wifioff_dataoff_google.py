import os,time,datetime

def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime(wifioff_dataoff_google_'%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	cmdr='adb logcat -b radio  > radio_log'+'&'
	os.system(cmdr)
	cmde='adb logcat -b event  > event_log'+'&'
	os.system(cmde)

def wifi_off():
             cmd= "adb -s "+div+" shell svc wifi disable"
             rc=os.system(cmd)
             print "wifii disabled"
             time.sleep(5)
             return rc
def data_off(div):
             cmd= "adb -s "+div+" shell svc data disable"
             rc=os.system(cmd)
             print "data disabled"
             time.sleep(10)
             return rc
def open_browse():
             cmd= "adb -s "+div+" shell am start -a android.intent.action.VIEW -d http://google.com"
             rc=os.system(cmd)
             print "google opened"
             time.sleep(20)
             return rc


def iter_status(iterations,div):
        collect_logs()
        for i in range(iterations):
                print i+1
                off=wifi_off()
                off=data_off(div)
                open1=open_browse()
div = "ZX1D64GJW6"
iterations=3
iter_status(iterations,div)
