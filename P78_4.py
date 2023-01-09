table = []
for line in open('P78_3.txt'):
    table.append(line.strip().split(' '))
table[0].insert(0,'')
seq1='AGCAUCUA'
seq2='ACCGUUCU'
similar = 0
z = zip(seq1,seq2)
#print(list(z))
for base1,base2 in z:
    num1 = 'AGCU'.find(base1)
    #print(num1)
    num2 = 'AGCU'.find(base2)
    similar += eval(table[num1+1][num2+1])
print(similar)