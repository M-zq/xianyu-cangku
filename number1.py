lst = eval(input('请输入列表lst: '))
lst2 = []
for i in lst:
    if lst.count(i) == 1:
        lst2.append(i)
print(lst2)