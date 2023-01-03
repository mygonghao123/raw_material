filein = open("protein2.txt","r")
i = 0
for line in filein:
    i += 1
    if i%2 == 0:
        print(line.strip())
filein.close()