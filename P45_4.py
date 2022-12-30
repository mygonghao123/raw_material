inputfile = open("sequence_li4.fasta","r")
seq = ''
for i in inputfile:
    if i[0] == '>' and seq == '':
        header = i
    elif i[0] != '>':
        seq = seq + i.strip()
    elif i[0] == '>' and seq != '':
        if i[0] == '>':
            print(header + seq)
            for j in 'ATGC':
                m = seq.count(j)
                n = len(seq)
                print("{}:{}".format(j,m))
                print("{}出现的频率为{}".format(j,m/n))
            print("该序列总长度为{}".format(n))
        seq = ''
        header = i
inputfile.close()