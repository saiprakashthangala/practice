'''
Before run the program device.py and Mo_num_msg.csv files having the same folder 
'''
import os,time,datetime,csv,random
import device
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('Audio palying_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	os.chdir(mydir)
	cmdr='adb logcat -b event  > event_log'+'&'
	os.system(cmdr)
	cmde='adb logcat -b radio  > radio_log'+'&'
	os.system(cmde)
def play_audio():
		cmd="adb shell input keyevent 3"
		os.system(cmd)
		cmd1= "adb shell am start -a android.intent.action.VIEW -d file:/sdcard/Samsung/Music/Over the Horizon.mp3/ -t mp3/wav"

		rc=os.system(cmd1)
                time.sleep(7)
                cmd2="adb shell input keyevent 127" #To stop the player
                rc=os.system(cmd2)
		print "audio played" 
		time.sleep(10)
                return rc
def iterations():
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	iters=your_list[2]
	return int(random.choice(iters[1::]))

def iter_status(iterations,div):
        collect_logs()
        for i in range(iterations):
                play=play_audio()
                print i+1
                
div =device.main()
iterations=iterations()
iter_status(iterations,div)


