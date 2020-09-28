kong = ''
list1 = []
list2 = []
len_max = 0

with open('G:\\0.0\\demo.py','r') as p:
    all_list = p.readlines()
row = len(all_list)
for space in all_list:
    len_str = len(space)
    if len_str > len_max:
        len_max = len_str
    if space[-1] == '\n':
        list1.append(space[:-1])
    else:
        list1.append(space)
for i in list1:
    while True:
        if len(i)+len(kong) == len_max:
            list2.append(i+kong+'#')
            kong = ''
            break
        else:
            kong += ' '
with open('G:\\0.0\\demo_new.py','w') as fff:
    for ff in range(1,row+1):
        fff.write(list2[ff-1]+str(ff)+'\n')