char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
emp=[]
lot=[]

# for i in char_list:
#     print(lot)
#      if i not in lot:
# #         emp.append([i,char_list.count(i)])
# #         lot.append(i)
# print(emp)
# for i in emp:
#     print(i[0], '-',i[1],'times')
for i in set(char_list):
    emp.append([i,char_list.count(i)])
print(emp)
for i in emp:
    print(i[0], '-',i[1],'times')