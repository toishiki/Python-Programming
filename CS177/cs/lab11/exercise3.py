import matplotlib.pyplot as pyplot

import random

data1=[0]*40
pos1=list()
for k in range(40):
    pos1.append(k+1)

for i in range(100000):
    a=random.randint(1,10)
    b=random.randint(1,10)
    c=random.randint(1,10)
    d=random.randint(1,10)
    e=a+b+c+d
    for j in range(40):
        if e==pos1[j]:
            data1[j]+=1
    
 
bar1 = pyplot.bar(pos1, data1, width=1, color='yellow', align='center')
 
pyplot.savefig('exercise3.png')
