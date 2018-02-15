import os,time,datetime
import unittest
class Test_call(unittest.TestCase):	
	div = "HQ541YL17255"
	num = "+917799221479"
	def setUp(self):
		pass
	# def Test_log(self):
	# 	cmdr='adb logcat -b radio > time.ctime.txt'
	# 	cmde='adb logcat -b event > time.ctime.txt'
	# 	os.system(cmdr)
		# os.system(cmde)
	def test_call1(self):
		os.chdir(mydir)
		#cmdr='adb shell dumpsys telephony.registry | grep CALL_TRANSACTION >> Itreation'+str(i+1)+'th'		
		cmdr='adb logcat -b radio | grep  -i call > Radio_ITER_'+str(i+1)+'&' # datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+'&'
		cmde='adb logcat -b event > Event_ITER_'+str(i+1)+'&'
		os.system(cmdr)
		os.system(cmde)
		div = "192.168.4.125:5555"
   		num = "+918019642892"
		cmd ="adb -s "+div+" shell am start -a android.intent.action.CALL -d tel:"+num+""
       		os.system(cmd)
		time.sleep(10)
		cmd2 = "adb shell input  keyevent 6"
		os.system(cmd2)
		


if __name__ =='__main__':
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	for i in range(3):
		print "Execution counter : ",i+1
		suite = unittest.TestLoader().loadTestsFromTestCase(Test_call)
		unittest.TextTestRunner(verbosity=2).run(suite)
	
		
