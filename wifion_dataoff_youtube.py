import os,time,datetime
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	cmdr='adb logcat -b radio  > sms_log'+'&'
	os.system(cmdr)
def wifi_on():
             cmd= "adb -s "+div+" shell svc wifi enable"
             rc=os.system(cmd)
             print "wifi enabled"
             time.sleep(10)
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
             print "youtube opened"
             time.sleep(10)
             return rc

def iter_status(iterations,div):
        collect_logs()
        for i in range(iterations):
                print i+1
                on=wifi_on()
                on1=data_off(div)
                play=youtube()
div = "ZX1D64GJW6"
iterations=3
iter_status(iterations,div)
