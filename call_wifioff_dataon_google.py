import os,time,datetime
import device,number
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('call_wifioff_dataton_google_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	cmdr='adb logcat -b radio  > sms_log'+'&'
	os.system(cmdr)
	cmde='adb logcat -b radio  > sms_log'+'&'
	os.system(cmde)
def call(div,num):
		cmd1 ="adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num+""
		rc = os.system(cmd1)
                return rc
def wifi_off():
             cmd= "adb -s "+div+" shell svc wifi disable"
             rc=os.system(cmd)
             print "wifi disabled"
             time.sleep(2)
             return rc
def Data_enable(div):
		cmd="adb -s "+div+" shell svc data enable"
		rc=os.system(cmd)
		print "mobile data enabled" 
		time.sleep(10)
                return rc
def google():
             cmd= "adb -s "+div+" shell am start -a android.intent.action.VIEW -d http://www.google.com"
             rc=os.system(cmd)
             print "google opened"
             time.sleep(10)
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
                off=wifi_off()
                on1=Data_enable(div)
                open1=google()
                end=end_call()
div = device.main()
num = number.number()
iterations=input("Enter no off iterations :")
iter_status(iterations,div)
