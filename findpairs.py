number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
e=[]
for i in range(0,len(n)):
    for h in range(1,len(n)):
        if n[i]+n[h]==30:
            n[i].append(e)
            n[h].append(e)
        else:
            continue
print(e)

