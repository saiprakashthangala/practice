import os,time,datetime
import device
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	os.chdir(mydir)
	cmdr='adb logcat -b radio  > sms_log'+'&'
	os.system(cmdr)

def data_on():
             cmd= "adb -s "+div+" shell svc data enable"
             rc=os.system(cmd)
						
             time.sleep(10)
             return rc

def open_browse():
             cmd= "adb -s "+div+" shell am start -a android.intent.action.VIEW -d http://google.com"
             rc=os.system(cmd)
             time.sleep(20)
             return rc
def not_browse():
             cmd= "adb -s "+div+" shell am start -a android.intent.action.VIEW -d http://google.com"
             rc=os.system(cmd)
             print "google notopened"
             time.sleep(10)
             return rc

def data_off():
             cmd= "adb -s "+div+" shell svc data disable"
             rc=os.system(cmd)
             print "data disabled"
             time.sleep(10)
             return rc

def iter_status(iterations,div):
        collect_logs()
        for i in range(iterations):
                print i+1
                on=data_on()
                browse= open_browse()
                off=data_off()
                browse1= not_browse()
div = device.main()
iterations=input("Enter no off iterations :")
iter_status(iterations,div)
