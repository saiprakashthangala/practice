import os,time,datetime
import device,number
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('Audio call_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	os.chdir(mydir)
	cmdr='adb logcat -b event > event_log'+'&'
	os.system(cmdr)
	cmde='adb logcat -b radio > radio_log'+'&'
	os.system(cmde)
def call(div,num):
		cmd1 ="adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num+""
		rc = os.system(cmd1)
                return rc	
def play_audio():
		cmd= "adb shell am start -a android.intent.action.VIEW -d file:/sdcard/Samsung/Music/Over the Horizon.mp3/ -t mp3/ogg"
		rc=os.system(cmd)
                time.sleep(15)
		print "audio played"
		time.sleep(0)
                return rc

def iter_status(iterations,div):
        collect_logs()
        for i in range(iterations):                
		play=play_audio()
		if play==0:
			print "audio played"
		else:
			print " audio not played "
			break;
                call_on = call(div,num) 
                print "iteration",i+1
                
div = device.main()
num = number.number()
iterations=input("Enter number of iterations : ")
iter_status(iterations,div)
