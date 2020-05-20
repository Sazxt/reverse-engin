import re
string = open("4.dis").read()#files
x = re.findall(r"\(\d+\)",string)#regex
print x