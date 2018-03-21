'''
Before executing this program, "device.py" and "Mo_num_msg.csv" files should present in same folder 
'''

import os,time,datetime,csv,random
import device
def collect_logs():
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('Airplane_%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)		#create log folder
	os.chdir(mydir)			# change directry 
	cmdr='adb logcat -b main | grep  -i AIRPLANE > AIRPLANE_log'+'&'
	os.system(cmdr)			# collecting log file
def iterations():
	f=open('Mo_num_msg.csv', 'r')
	reader = csv.reader(f)
	your_list = list(reader)
	iters=your_list[2]
	return int(random.choice(iters[1::]))
	
def airplane_on():
	cmd="adb shell input keyevent 3"
	os.system(cmd)			#set home page 
	cmd1 ="adb shell settings put global airplane_mode_on 1;adb shell am broadcast -a android.intent.action.AIRPLANE_MODE" # Enable Airplane mode 
	rc = os.system(cmd1)	#ariplane mode on 
	time.sleep(20)
	print "Airplane mode is on"
	return rc  				#return code 
def airplane_off():
	cmd2 = "adb shell settings put global airplane_mode_on 0" # Disable Airplane mode
	rc=os.system(cmd2) 		#arirplane mode off 
  	time.sleep(20)
	print "Airplane mode is off"
	return rc    			#return code 
def iter_status(iterations,div):
	collect_logs()
	for i in range(iterations):
		on=airplane_on()	#call airplane on function 
		off=airplane_off()	#call airplane off function
		if on == off:
			print "Test passed"
		else:
			print "Test Failed"
		
div =device.main()
iterations=iterations()
iter_status(iterations,div)
