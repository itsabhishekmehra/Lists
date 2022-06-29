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
print("Count For Even is:",len(e),"\nCount For Odd is:",len(o))
print("\nCount of all the numbers is:",len(elements))
print("\nSum For Even",sum(e), "\nSum For Odd",sum(o))
print("\nSum of all the numbers is",sum(elements))
print("\nFor Even Average is",sum(e)/len(e),"\nFor Even Average is",sum(o)/len(o))
print("\nAverage of all the numbers is",sum(elements)/len(elements))