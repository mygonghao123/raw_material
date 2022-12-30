filein = open("random_1.txt","r")
fileout = open("P33_1.txt","w")
n = 0
for i in filein:
    n += 1
    fileout.write(i)
print("总有{}个神经长度，random_1.txt的各神经长度已另保存到P33_1.txt中".format(n))
filein.close
fileout.close