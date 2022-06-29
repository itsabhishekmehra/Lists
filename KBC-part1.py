question_list = ["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai?"]
options_list = [[4, 9 , 7 , 8],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
isfifty = True
solution_list = [3, 4, 1]
for i in range(0,len(question_list)):
    print(solution_list[i], "heee\n")
    print(i+1,'.', question_list[i])
    list2 = options_list[i]
    for u in range(0,len(list2)):
        print(u+1,'.', list2[u])
    a = int(input("Enter the answer: "))
    if a == 5:
        if isfifty:
            print('Welcome to 50:50 Lifeline')
            print(1,'.',list2.pop(solution_list[i]-1))
            print(2,'.',list2[0])
            a = int(input("Enter correct choice:"))
            if a==1:
                print(solution_list[i], "hello sol")    
                a = solution_list[i]
            isfifty = False
        else:
            print("Sale kitni bar karega.")
            a = int(input("Enter the answer: "))
    if a == solution_list[i]:
        print("Congrats! Aapka answer sahi hai")
    else:
        print("Sadly aapka javab ga1lat hai.")
        break