numbers = input('input elements of the list: ')
numbers=numbers.split(',')
print(numbers)
# numbers=[]
# numbers.append(numbers)
num1=0
for i in range(0,len(numbers)):
    num2=int(numbers[i])
li=[]
    for p in range(0,len(numbers)):
        if num1<num2:
            num1=num2
        else:
            continue
print(num1)


# num1=0
# for i in range(0,len(numbers)):
#     num2=numbers[i]
#     for p in range(0,len(numbers)):
#         if num1<num2:
#             num1=num2
#         else:
#             continue
# print(num1)









# for i in range(0,len(numbers)):
#     for p in range(0,len(numbers)):
#         if numbers[i]>numbers[p]:
#             print(numbers[i])
#         else :
#             break