t=15
ms= [
[8, 3, 4],
[1, 5, 9],
[6, 7, 2]]
if len(ms[0])==len(ms[1])==len(ms[2]):
    if (sum(ms[0]))==(sum(ms[1]))==(sum(ms[2])):#Rows k lie
        if ms[0][0]+ms[1][0]+ms[2][0]==t:#1st Columns k lie
            if ms[0][1]+ms[1][1]+ms[2][1]==t:#2nd Columns k lie
                if ms[0][2]+ms[1][2]+ms[2][2]==t:#3rd Columns k lie
                    if ms[0][0]+ms[1][1]+ms[2][2]==t:#1st Diogonal
                        if ms[0][2]+ms[1][1]+ms[2][0]==t:#2nd Diogonal
                            print("It's a Magic Square:)*****")
                        else:
                            print("it's not a Magic Square")
                    else:
                        print("it's not a Magic Square")
                else:
                    print("it's not a Magic Square")
            else:
                print("it's not a Magic Square")
        else:
            print("it's not a Magic Square")
    else:
        print("it's not a Magic Square")
else:
    print("it's not a Magic square")