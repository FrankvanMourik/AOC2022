testsite_array = []
with open('exercise1.txt') as my_file:
    for line in my_file:
        testsite_array.append(int(line))
for i in testsite_array:
    for j in testsite_array:
        for k in testsite_array:
            if i+j+k == 2020:
                print("Numbers are ", i, " and ", j, " and ", k," multiplied: ",i*j*k)