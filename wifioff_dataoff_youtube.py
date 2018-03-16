import os,time,datetime

def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('wifioff_dataoff_youtube_%Y-%m-%d_%H-%M-%S'))
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
def youtube():
             cmd= "adb -s "+div+" shell am start -a android.intent.action.VIEW -d http://www.youtube.com/watch?v=xko3vld5Wds"
             rc=os.system(cmd)
             print "youtube not opened"
             time.sleep(10)
             return rc
def iter_status(iterations,div):
        collect_logs()
        for i in range(iterations):
                print i+1
                off=wifi_off()
                off=data_off(div)
                play=youtube()
div = "ZX1D64GJW6"
iterations=3
iter_status(iterations,div)
