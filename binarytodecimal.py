binary= [1, 0, 0, 1, 1, 0, 1, 1]
bi=len(binary)
# sum=0
# for o in range(0,bi):
for i in range(bi-1,0):
    for p in range(0,bi):
        sum=binary[i]*(2**p)
        print(sum)