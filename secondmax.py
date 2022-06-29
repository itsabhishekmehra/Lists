numbers = input('Enter you list: ')
numbers.split(',')
li=[]
print(numbers)
for p in range(0,100):
    for i in range(0,len(numbers)):
        if p==numbers[i]:
            li.append(numbers[i])
        else:
            continue
print(li)
print(li[-2])


# This code is good to go
# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# li=[]
# for p in range(0,100):
#     for i in range(0,len(numbers)):
#         if p==numbers[i]:
#             li.append(numbers[i])
#         else:
#             continue
# print(li)

# print(li[-2])