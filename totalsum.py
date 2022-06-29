number = 30
t=0
m=[]
j=[]
n = [10, 11, 12, 13, 14, 17, 18, 19]
t=n
for i in n:
    for p in t:
        if n[i]+t[p]==number:
            list(n[i]&t[p]).append(m)
            m.extend(j)
        print(j)
