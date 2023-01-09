from operator import itemgetter
table = [
    ['protein', 'ext1', 'ext2', 'ext3'],
    [0.16, 0.038, 0.044, 0.040],
    [0.66, 0.184, 0.191, 0.191],
    [0.33, 0.089, 0.095, 0.091],
    [1.32, 0.365, 0.367, 0.365],
    [1.00, 0.280, 0.292, 0.283],
    [1.66, 0.441, 0.443, 0.444]
    ]
table = table[1:]
p,e1,e2,e3 = zip(*table)
e = e1 + e2 + e3
p = p * 3
t = list(zip(p,e))
for i in t:
    t_sort = sorted(t,key = itemgetter(1))
print(t_sort[0],t_sort[1],t_sort[2])