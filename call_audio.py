import os,time,datetime
import device,number
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('call_audio_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	os.chdir(mydir)
	cmdr='adb logcat -b radio  > sms_log'+'&'
	os.system(cmdr)
def call(div,num):
		cmd1 ="adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num+""
		rc = os.system(cmd1)
                return rc
def play_audio():
		cmd= "adb shell am start -a android.intent.action.VIEW -d file:/storage/emulated/0/Music/sound.mp3 -t audio/mp3"
		rc=os.system(cmd)
                time.sleep(10)
                cmd1="adb shell input keyevent 127"
                rc=os.system(cmd1)
		print "audio played" 
		time.sleep(7)
                return rc

def iter_status(iterations,div):
        collect_logs()
        for i in range(iterations):
                call_on = call(div,num)
                play=play_audio() 
                print i+1
                
div = device.main()
num = number.number()
iterations=input("Enter number off iterations :")
iter_status(iterations,div)
