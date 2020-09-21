k = [i for i in range(1, 29)]#创建列表
def move(k, s):#自定义函数将不需要删除的数移到列表的最后面
    for i in range(s):
        tem = k.pop(0)
        k.append(tem)
while len(k) > 2:
    move(k, 2)
    print(k.pop(0))#被剔除的位置
print("安全位置是：{0}".format(k))