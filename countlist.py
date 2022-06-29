numbers = [12,23,34,43,55,41,24,37,40,20]

for i in range(20, 41) :
    for p in range(0, len(numbers)) :
        if (numbers[p] == i) :
            print(numbers[p], p)