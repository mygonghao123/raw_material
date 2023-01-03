filein = open("CALM2.txt","r")
n = 0
line = ''
for i in filein:
    line = line + i.strip()
if "CALM2" in line:
    print('找到了')
else:
    print('没找到')