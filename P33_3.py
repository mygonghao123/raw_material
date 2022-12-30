filein = open("P33_3.txt","r")
ge = "ATCG"
for jian in filein:
    jian = jian.strip()
count_d = {}
for i in ge:
    n = jian.count(i)
    count_d[i] = n
    print("{}:{}".format(i,n))
ls = list(count_d.items())
ls.sort(key=lambda x:x[1],reverse=True)
print('最常见的碱基出现频率为{}:{}'.format(ls[0][0],ls[0][1]))
filein.close()