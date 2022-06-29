mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
replacementStr = "on"

splitt = mainStr.split(' ')
for i in range(0,len(splitt)):
    print(splitt[i],i)
    if i==12 and splitt[i]=='over':
        splitt[i]='on'
print(splitt)

# print(splitt)
# print(mainStr.replace("over", "on",1))
# for i in range(0,len(splitt)):
# print(splitt.index('over'))