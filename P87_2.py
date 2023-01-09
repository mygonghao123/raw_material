filein = open('sequence_li4.fasta','r')
fileout = open('P87_2.txt','w')
seq = ''
buck = []
for line in filein:
    if line[0] == '>' and seq == '':
        header = line
    elif line[0] != '>':
        seq += line
    elif line[0] == '>' and seq != '':
        buck.append([len(seq),header,seq]) 
        seq = ''
        header = line         
buck.append([len(seq),header,seq])
buck = sorted(buck,key=lambda x:x[0])
other = ''
for i in buck:
    for j in range(len(i)):
        other += str(i[j])
#print(other)
fileout.write(other)
filein.close
fileout.close