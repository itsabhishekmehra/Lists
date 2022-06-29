print("Welcome To Koun Banega Crorepati")
kitna_paisa_hai = [3000, 600000, 
324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
l = 0 
p = 0
k = 0
for i in kitna_paisa_hai:
    if 100000  <= i < 10000000 :
        l += 1
    elif i > 10000000 :
        p += 1
    else:
        k += 1
print("Lakhpatis are: ",l,"\nCrorepatis are: ",p,"\nDilwales are: ",k)


# p=2
# p+=1
# print(p)


# p=+1
# print(p)