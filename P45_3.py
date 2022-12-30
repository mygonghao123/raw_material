filein = open("Homo sapiens.fasta","r")
buck = []
total = 0
for i in filein:
    if i[0] != '>':
        seq = i.strip()
        buck.append(seq)
        line = "".join(buck)
        #print(line)
        for j in 'ATGC':
            line.count(j)
        total += float(len(seq))
print("核苷酸序列的总长度为{}".format(total))
for i in 'ATGC':
    print("{}:{}".format(i,line.count(i)))
    print("{}出现的频率为{}".format(i,line.count(i)/total))