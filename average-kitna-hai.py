elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
e=[]
o=[]
for i in elements:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
e.sort()
o.sort()
print("For Even Average is",sum(e)/len(e),"\nFor Even Average is",sum(o)/len(o))