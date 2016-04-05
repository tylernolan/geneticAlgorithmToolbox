import random

f = open("config2.txt", 'w')
strFormat = ""
for i in range(24):
	strFormat += "{},"
strFormat += "{}\n"

for i in range(25):
	string=[]
	for j in range(25):
		string.append(random.randint(1,200))
	f.write(strFormat.format(*string))
	
f.close()