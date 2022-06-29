n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
a = []
for i in n:
    print(a)
    if n.count(i)>1 and i not in a:
        a.append(i)
print(a)
    # if i > 1: