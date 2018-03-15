import os,time,datetime
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('Audio call_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	cmdr='adb logcat -b event > sms_log'+'&'
	os.system(cmdr)
def call(div,num):
		cmd1 ="adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num+""
		rc = os.system(cmd1)
                return rc
def play_audio():
		cmd= "adb shell am start -a android.intent.action.VIEW -d file:/storage/emulated/0/Music/sound.mp3 -t audio/mp3"
		rc=os.system(cmd)
                time.sleep(5)
		print "audio played"
		time.sleep(5)
                return rc

def iter_status(iterations,div):
        collect_logs()
        for i in range(iterations):
                play=play_audio()
                call_on = call(div,num) 
                print i+1
                
div = "ZX1D64GJW6"
num = "+919000137251"
iterations=3
iter_status(iterations,div)
