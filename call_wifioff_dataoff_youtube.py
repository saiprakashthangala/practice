import os,time,datetime
import device,number
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('call_wifioff_dataoff_youtube_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	cmdr='adb logcat -b radio  > sms_log'+'&'
	os.system(cmdr)
	cmde='adb logcat -b event  > sms_log'+'&'
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
def Data_disable(div):
		cmd="adb -s "+div+" shell svc data disable"
		rc=os.system(cmd)
		print "mobile data disabled" 
		time.sleep(7)
                return rc
def youtube():
             cmd= "adb -s "+div+" shell am start -a android.intent.action.VIEW -d http://www.youtube.com/watch?v=xko3vld5Wds"
             rc=os.system(cmd)
             print "youtube opened"
             time.sleep(7)
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
                on1=Data_disable(div)
                play=youtube()
                end=end_call()
div = device.main()
num = number.number()
iterations=input("Enter no off iterations :")
iter_status(iterations,div)
