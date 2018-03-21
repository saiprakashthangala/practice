import os,time,datetime
import device,number
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	cmdr='adb logcat -b radio | grep  -i call > Call_log'+'&'
	os.system(cmdr)

def call(div,num):
		cmd1 ="adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num+""
		rc = os.system(cmd1)
                return rc
def wifi_on():
             cmd= "adb -s "+div+" shell svc wifi enable"
             rc=os.system(cmd)
             print "wifi enabled"
             time.sleep(2)
             return rc
def Data_disable(div):
		cmd="adb -s "+div+" shell svc data disable"
		rc=os.system(cmd)
		print "mobile data disabled" 
		time.sleep(10)
                return rc
def google():
             cmd= "adb -s "+div+" shell am start -a android.intent.action.VIEW -d http://www.google.com"
             rc=os.system(cmd)
             print "google opened"
             time.sleep(5)
             return rc
def end_call():
                cmd2 = "adb shell input  keyevent 6"
		rc=os.system(cmd2)
                print "call ended"
		return rc

def iter_status(iterations,div):
        collect_logs()
        for i in range(iterations):
                print i+1
                call_on = call(div,num)
                on=wifi_on()
                on1=Data_disable(div)
                open1=google()
                end=end_call()
div = device.main()
num = number.number()
iterations=input("Enter no off iterations :")
iter_status(iterations,div)
