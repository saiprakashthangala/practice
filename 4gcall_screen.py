import os,time,datetime,csv,random
import device;
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
        os.chdir(mydir)
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
                time.sleep(10)
                return rc
def log():
          f1=open("sms_log","r+")
          f2=f1.read()
          var="imsPhone.isVolteEnabled()=true"
          if var in f2:
	           print "its a volte call"
          else:
	           print "its a 4g/3g/2g call"
def screencap1():
                cmd1 = "adb -s "+div+" shell screencap -p /sdcard/screen.png"
                cmd2 ="adb -s "+div+" pull /sdcard/screen.png"
                rc=os.system(cmd1)
                os.system(cmd2)
                time.sleep(5)
                print "screenshot taken"
                return rc 
def screencap2():
                cmd1 = "adb -s "+div+" shell screencap -p /sdcard/screen1.png"
                cmd2 ="adb -s "+div+" pull /sdcard/screen1.png"
                rc=os.system(cmd1)
                os.system(cmd2)
                print "screenshot taken"
                time.sleep(10)
                return rc                       
def end_call():
                cmd2 = "adb shell input  keyevent 6"
		rc=os.system(cmd2)
                print "call ended"
                return rc
def iter_status(iteration,div):
       collect_logs() 
       for i in range(iteration):
                print i+1
                screen = screencap1()
                call_on = call(div,num)
                screen1= screencap2()
                end= end_call()
                log1=log()
div = device.main()
print div
num= number()
iteration=iterations()
iter_status(iteration,div)
