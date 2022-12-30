filein = open("sequence_li4.fasta","r")
n = 0
seq = ''
for i in filein:
    if i[0] == '>' and seq == '':
        header = i
    elif i[0] != '>':
        seq = seq + i
    elif i[0] == '>' and seq != '':
        if i[0] == '>':
            print(header + seq)
            n += 1
            fileout = open("P45_1_{}.fasta".format(n),"w")
            fileout.writelines(header + seq)
        seq = ''
        header = i
filein.close()
fileout.close()