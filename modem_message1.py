import os,time,datetime
import unittest
class Test_call(unittest.TestCase):	
	div = "HQ541YL17255"
	num = "+917799221479"
	def setUp(self):
		pass
	def test_SMS1(self):
		os.chdir(mydir)		
		cmdr='adb logcat -b radio | grep  -i SMS > Radio_ITER_'+str(i+1)+'&' # datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+'&'
		cmde='adb logcat -b event > Event_ITER_'+str(i+1)+'&'
		os.system(cmdr)  
		os.system(cmde)
		div = "HQ541YL17255"
   		num = "+917799221479"
		Text="saiprakash is a gud boy"
		cmd="adb shell am start -a android.intent.action.SENDTO -d sms:"+num
       		os.system(cmd)
		cmd2="adb shell input text $(echo {} | sed -e 's/ /\%s/g')".format(Text)
		os.system(cmd2)
		time.sleep(10)
		cmd3 = "adb shell input keyevent 22"
		os.system(cmd3)
		cmd4="adb shell input keyevent 66"
		os.system(cmd4)

#adb shell am start -a android.intent.action.SENDTO -d sms:+1-222-333-4444
#adb shell input text "sampletexthere"
#adb shell input keyevent 66



if __name__ =='__main__':
	mydir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
	os.makedirs(mydir)
	for i in range(1):
		print "Execution counter : ",i+1
		suite = unittest.TestLoader().loadTestsFromTestCase(Test_call)
		unittest.TextTestRunner(verbosity=2).run(suite)
	
		
