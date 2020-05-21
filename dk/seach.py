# author : Sazxt
# coding by orang gans
# ga ngerti? ga usah make kntl..
import re,sys
pi = '64203d2025730a6b203d2025730a65203d2027270a692c6a203d2028302c30290a7768696c6520313a0a2020202069662069203e3d206c656e2864293a20627265616b0a202020206966206a203e3d206c656e286b293a206a203d20300a2020202065202b3d2063687228645b695d205e206b5b6a5d290a2020202069202b3d20310a202020206a202b3d2031'
class dk_dec:
	k = list()
	d = list()

	def __init__(self,file):
		self.file = file
		
	def convert_int(self,num):
		assert type(num).__name__ == 'list'
		return (lambda foc : 
			[int(i) for i in foc]
		)(num)

	def cek(self,file, xor = 0, add = 0, subcr = 0, compr = 0):
		print "[*] cek obfuscate file .."
		offset_line = re.findall(r"(\d+)\D+\>\>",self.file)
		pars = re.findall(r"\w+",self.file)
		comp = re.findall(r"COMPARE_OP \D+.(\W+)",self.file)
		if 'EXEC_STMT' in pars and 'SETUP_LOOP' in pars:
			i = 0
			print ("[*] Get Victim Opcode .. ")
			while len(pars) > i:
				if 'BINARY_XOR' in pars[i]:
					xor += 1
				elif 'BINARY_SUBSCR' in pars[i]:
					subcr += 1
				elif 'INPLACE_ADD' in pars[i]:
					add += 1
				i += 1
		else:
			exit("opcode not found!!")
		if comp:
			for i in comp:
				if re.sub("\s","",i) == '(>=)':
					compr += 1
		if xor == 1 and add is 3 and subcr == 2 and compr is 2:
			return True
		else:
			return False

	def d_pars(self,num_list):
		max = len(num_list)-3
		coq = num_list[:max]
		return coq

	def search_dk(self, out=None):
		if self.cek(self.file):
			pass
		else:
			exit("abort !")
		ops = (lambda fi 
			: re.findall(r"\((\d+)\)",fi)
						)(self.file)
		dat = self.d_pars(ops)
		pf = self.convert_int(dat)
		o = len(pf)-1
		print ("[*] parsing dk..")
		while file and ops:
			if len(self.k) > 254:
				if 0 > o:
					break
				self.d.append(pf[o])
			else:
				self.k.append(pf[o])
			o -= 1
		print ("[*] Succesfuly Get dk ..")
		self.d.reverse()
		self.k.reverse()
		del self.d[len(self.d)-2:]
		dec = pi.decode("hex")%(self.d,self.k)
		if out:
			with open(out,"w") as f:
				f.write(dec)
				print ("[*] Savefile as %s"%(out))
		else:
			print dec

if (1 < len(sys.argv)):
	try:
		ox = open(sys.argv[1]).read()
	except IOError:
		exit("filename not found!")
	if (3 <= len(sys.argv)):
		dk_dec(ox).search_dk(sys.argv[2])
	else:
		dk_dec(ox).search_dk()
else:
	exit("usage : seach <file.dis> <outfile>")