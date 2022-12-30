fasta_file = open('protein.fasta','r')
out_file = open('P45_2.txt','w')
seq = ''
for line in fasta_file:
    if line[0] == '>' and seq == '':
        header = line
    elif line[0] != '>':
        seq = seq + line
    elif line[0] == '>' and seq != '':          
        if seq[0] == 'M' and seq.count('W') > 1:
            out_file.write(header + seq)
        seq = ''
        header = line
if seq[0] == 'M' and seq.count('W') > 1:
    #print(header + seq)
    out_file.write(header + seq)
fasta_file.close()
out_file.close()