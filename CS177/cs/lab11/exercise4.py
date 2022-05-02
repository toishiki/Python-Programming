import matplotlib.pyplot as pyplot
import random

xs1=[]
ys1=[]
xs2=[]
ys2=[]
for i in range(10000):
        x=random.randint(-100,100)
        y=random.randint(-100,100)
        if (x**2+y**2<10000):
            xs1.append(x)
            ys1.append(y)
        else:
            xs2.append(x)
            ys2.append(y)
            
pyplot.axis('equal')
pyplot.scatter(xs1,ys1,color='blue')
pyplot.scatter(xs2,ys2,color='green')
pyplot.savefig('exercies4.png')
