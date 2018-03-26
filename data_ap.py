import os,time,datetime,csv,random
import device;
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	cmdr='adb logcat -b radio  > sms_log'+'&'
	os.system(cmdr)
def number():
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	numbers=your_list[0]
        return random.choice(numbers[1::])
def iterations():
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	iters=your_list[2]
        return int(random.choice(iters[1::]))
def ap_on():
        cmd1 ="adb shell settings put global airplane_mode_on 1;adb shell am broadcast -a android.intent.action.AIRPLANE_MODE" # Enable Airplane mode 
	rc = os.system(cmd1)	#ariplane mode on 
	time.sleep(5)
	print "Airplane mode is on"
        cmd2 = "adb shell settings put global airplane_mode_on 0;adb shell am broadcast -a android.intent.action.AIRPLANE_MODE"
        rc = os.system(cmd2)	#ariplane mode off
	time.sleep(5)
        print "Airplane mode is off"
        return rc 

def call(div,num):
		cmd1 ="adb shell am start -a android.intent.action.CALL -d tel:"+num+""
		rc = os.system(cmd1)
                time.sleep(15)
                return rc
def iter_status(iteration,div):
        
       for i in range(iteration):
                print i+1
                call_on = call(div,num)
                apon = ap_on()
                call_on = call(div,num)
       collect_logs()         
div = device.main()
print div
num= number()
iteration=iterations()
iter_status(iteration,div)
