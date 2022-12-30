import math
data = []
filein = open("P33_1.txt","r")
for i in filein:
    length = float(i.strip())
    data.append(length)
s = sum(data)
l = len(data)
aver = s/l
for j in data:
    biao = math.sqrt(((j-aver)**2)/l)
fileout = open("P33_2.txt","w")
fileout.write("平均数为：%.2f \n" %(aver))
fileout.write("标准差为：%.2f \n" %(biao))