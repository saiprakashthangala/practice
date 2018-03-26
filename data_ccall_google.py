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

def call(div,num):
		cmd1 ="adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num+""
		rc = os.system(cmd1)
                return rc
def open_browse():
             cmd= "adb shell am start -a android.intent.action.VIEW -d http://google.com"
             rc=os.system(cmd)
             print "google opened"
             time.sleep(5)
             return rc

def Data_enable(div):
		cmd="adb -s "+div+" shell svc data enable"
		rc=os.system(cmd)
		print "mobile data Enabled" 
		time.sleep(4)
                return rc

def iter_status(iteration,div):
        
       for i in range(iteration):
                print i+1
                on1=Data_enable(div)
                call_on = call(div,num)
                open1=open_browse()
       collect_logs()         
div = device.main()
print div
num= number()
iteration=iterations()
iter_status(iteration,div)
