import matplotlib.pyplot as pyplot

import random

data1=[0,0,0,0,0,0,0,0,0,0]
pos1 = [1,2,3,4,5,6,7,8,9,10]


for i in range(100000):
    x=random.randint(1,10)
    for j in range(10):
        if x==pos1[j]:
            data1[j]+=1
    x=0
    
 
bar1 = pyplot.bar(pos1, data1, width=1, color='yellow', align='center')
 
pyplot.savefig('exercise1.png')
