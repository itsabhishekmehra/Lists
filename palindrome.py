
name = input('Enter the palindrome name to check: ')
ls=list(name)
length=len(ls)
jo=[]
for i in range(0,length):
    jo=ls[length-i-1]
if jo==ls:
    print('Ha ye Palindrome hai')
else:
    print('Nahi ye Palindrome nahi hai')


# ye code b chalta hai
# name = input('Enter the palindrome name to check: ')
# ls=list(name)
# length=len(ls)
# print(ls[::-1])
# if (ls[::-1])==ls:
#     print('Ha ye Palindrome hai')
# else:
#     print('Nahi ye Palindrome nahi hai')

