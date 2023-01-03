filein = open("sequence.fasta","r")
dic = {'TAA':'Stop','TAG':'Stop','TGA':'Stop','ATG':'Start'}
rna = ''
prot = ''
for i in filein:
    if not i.startswith('>'):
        rna = rna + i.strip()
    #print(rna)
for j in range(0,len(rna)):
    codon = rna[j:j+3]
    #print(codon)
    if codon in dic:
        if dic[codon] == 'Stop':
            prot = prot + '*'
            #print(prot)
        elif dic[codon] == 'Start':
            prot = prot + '-'
print("终止密码子的数目:{}".format(prot.count('*')))
print("起始密码子的数目:{}".format(prot.count('-')))
filein.close()