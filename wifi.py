import os,time,datetime
import device
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('wifi_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	cmdr='adb logcat -b radio  > radio_log'+'&'
	os.system(cmdr)
	cmde='adb logcat -b event  > event_log'+'&'
	os.system(cmde)

def wifi_on():
             #cmd= "adb -s "+div+" shell svc wifi enable"
             cmd1="adb shell su -c 'svc wifi enable'"
	     rc=os.system(cmd)
             print "wifii enabled"
             time.sleep(5)
             return rc
def wifi_off():
            # cmd= "adb -s "+div+" shell svc wifi disable"
             cmd2="adb shell su -c 'svc wifi disable'"
	     rc=os.system(cmd)
             print "wifii disabled"
             time.sleep(5)
             return rc

def iter_status(iterations,div):
        collect_logs()
        for i in range(iterations):
                print i+1
                on=wifi_on()
                off=wifi_off()
div = device.main()
iterations=3
iter_status(iterations,div)

