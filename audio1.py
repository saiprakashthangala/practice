import os,time,datetime

def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('Audio palying_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	cmdr='adb logcat -b radio  > sms_log'+'&'
	os.system(cmdr)
def play_audio():
		cmd= "adb shell am start -a android.intent.action.VIEW -d file:/storage/emulated/0/Music/sound.mp3 -t audio/mp3"
		rc=os.system(cmd)
                time.sleep(7)
                cmd1="adb shell input keyevent 127" #To stop the player
                rc=os.system(cmd1)
		print "audio played" 
		time.sleep(10)
                return rc

def iter_status(iterations,div):
        collect_logs()
        for i in range(iterations):
                play=play_audio()
                print i+1
                
div = "ZX1D64GJW6"
iterations=3
iter_status(iterations,div)

