import sys,time
from random import choice as cos

class TesBruh(object):
	def __init__(self,Assemble):
		self.Assemble = Assemble
		self.color = ['\033[1;31m','\033[1;34m','\033[1;37m','\033[1;33m','\033[1;36m']
		self.__main__()
	def __main__(self):
		try:
			for i in self.Assemble +'\n':
				sys.stdout.write(cos(self.color)+str(i))
				sys.stdout.flush()
				time.sleep(0.040)
		except:
			pass

if __name__=="__main__":
	try:
		TesBruh('[ <----{[(Ezz-Kun)]}----> ]')
	except:
		pass
