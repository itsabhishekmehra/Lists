que=["Who is the prime minister of israel?","How many contries has veto power ?","which is the smallest nation in world by area ?","when was Himachal pradesh established","where is horn of Africa ?"]
Op1=["1) Neftali Benet","1) 6","1) Italy ","1) 1972 ","1) East africa"]
Op2=["2) Berjamin netnyhay",'2) 7',"2) vetican city","2) 1971","2) west africa"]
Op3=['3) Yasle leaweli','3) 5',"3) mexico ","3) 1975","3) central africa"]
Op4=["4) Nareadra medi","4) 8", '4) panama',"4) 1980","4) south africa."]
Ans=[1,3,2,2,1]

for i in range(0,len(que)):
    print(que[i])
    print(Op1[i])
    print(Op2[i])
    print(Op3[i])
    print(Op4[i])
    input1= int(input('Enter your option number: '))
    if input1 == Ans[i]:
        print('Your option is correct')
    else:
        print('Your ans is wrong, so you are out of game')
        break