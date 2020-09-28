def num(x):
    sum = 0
    list = []
    for i in x:
        if i%2 == 0:
            sum += 1
            list.append(i)
    print(sum)
    print(list)
num([1,2,2,21,2,2,1,21,21,21,21,2])