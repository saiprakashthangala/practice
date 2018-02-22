import os,time,datetime,re
def test_call1():
		os.chdir(mydir)
		cmdr='adb logcat -b radio | grep  -i call > Radio_ITER_'+str(i+1)+'&'
		cmde='adb logcat > log_ITER_'+str(i+1)+'&'
		os.system(cmdr)
		os.system(cmde)
		div = "HQ541YL17255"
   		num = "+917799221479"
		cmd ="adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num+""
       		os.system(cmd)
		time.sleep(8)
		cmd2 = "adb shell input  keyevent 6"
		os.system(cmd2)

def Test_status():
	state=open('Radio_ITER_'+str(i+1),'r+')
	stat=state.readlines()
	print type(stat)
	for line in stat:
		stri=re.search('id=1,DIALING',line)	
		if stri is not None :
			print "pass"
			break
			# assertTrue(stri in line) 
	
mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
os.makedirs(mydir)
for i in range(2):
	print "Execution counter : ",i+1
	test_call1()
	Test_status()
