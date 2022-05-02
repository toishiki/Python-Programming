import math
from graphics import *
from utility import *
from collections import Counter

def distance(x, y):
   xd=x[0]-y[0]
   yd=x[1]-y[1]
   d=(xd**2+yd**2)**(1/2)
   return d

def majority(myList):
   b=0
   r=0
   for i in range(len(myList)):
      if myList[i]=='blue':
         b+=1
      elif myList[i]=='red':
         r+=1
   if b>r:
      return 'blue'
   else:
      return 'red'

def classify(bluePoints, redPoints, newPoint, k):
   bl=[]
   rl=[]
   for i in range(len(bluePoints)):
      d=distance(bluePoints[i],newPoint)
      bl.append(d)
   for j in range(len(redPoints)):
      d=distance(redPoints[j],newPoint)
      rl.append(d)
   bl.sort()
   rl.sort()
   comb=[]
   count=0
   i=0
   j=0
   while count<=k:
      if bl[i]<rl[j]:
         comb.append('blue')
         i+=1
      else:
         comb.append('red')
         j+=1
      count+=1
   return majority(comb)

def main():
   win = GraphWin("K-NN Classifier", 500, 500)
   
   points1=readPoints('blues.txt')
   plotPoints(points1,win,'blue')
   print("Blue points has read from blues.txt and plotted.")
   points2=readPoints('reds.txt')
   plotPoints(points2,win,'red')
   print("Red points has read from reds.txt and plotted.")
   k=eval(input("Please enter k for k-NN classfier:"))

   while True:
      print("Please click for the new point to be classified.")
      NewPoint=win.getMouse()
      x=NewPoint.getX()
      y=NewPoint.getY()
      pt=(x,y)
      color=classify(points1,points2,pt,k)
      print("This point is classified as:",color)
      npt=Circle(Point(x,y),3)
      npt.draw(win)
      npt.setFill(color)

main()
