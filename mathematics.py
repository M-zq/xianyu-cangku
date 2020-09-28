import math
num = 10000
x = []
for i in range(0,num+1):
    x.append(2*math.pi/num*i)
y = []
for j in x:
    y.append(abs(math.sin(j)))
print(2*math.pi*sum(y)/num)