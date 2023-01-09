filein = open('P88_4.txt','r')
buck = []
seq = ''
for line in filein:
    if line[0] == '>' and seq == '':
        header = line
        AC = line.split('|')[1]
    elif line[0] != '>':
        seq += line
    elif line[0] == '>' and seq != '': 
        buck.append([AC,header,seq])
        seq = ''
        header = line
        AC = line.split('|')[1]
buck.append([AC,header,seq])
#print(buck)
buck=sorted(buck,key=lambda x:x[0])
dic = {}
for item in buck:
    dic[item[0]] = item[2].replace('\n','')
print(dic)
filein.close()