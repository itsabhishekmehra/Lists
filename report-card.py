marks = [78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78],[87, 67, 49, 68, 88]
import itertools
flatlist=list(itertools.chain(*marks))
print(flatlist, len(flatlist))
total=0
for i in range(0,len(flatlist)):
    total=total+flatlist[i]
print(total)



# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78]]
# total=0
# for i in marks:
#     print(i,sum(i))
#     total=total+sum(i)
# print(total)


