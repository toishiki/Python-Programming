import matplotlib.pyplot as pyplot

import random

data1=[0]*20
pos1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]


for i in range(100000):
    a=random.randint(1,10)
    b=random.randint(1,10)
    c=a+b
    for j in range(20):
        if c==pos1[j]:
            data1[j]+=1
    a=0
    b=0
    c=0
    
 
bar1 = pyplot.bar(pos1, data1, width=1, color='yellow', align='center')
 
pyplot.savefig('exercise2.png')
