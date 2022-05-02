from graphics import *
from utility import *
import random

def generatePoint(meanX, meanY, sigmaX, sigmaY):
    x=random.gauss(meanX,sigmaX)
    y=random.gauss(meanY,sigmaY)
    x=round(x,1)
    y=round(y,1)
    return (x,y)
   
def generatePoints(meanX, meanY, sigmaX, sigmaY, numPoints):
    l=[]
    for i in range(numPoints):
        t=generatePoint(meanX,meanY, sigmaX,sigmaY)
        l.append(t)
        t=0
    return l

def main():
   win = GraphWin("Data Collector", 500, 500)
   
   print("Please click on window for meanX and meanY for blue samples.")
   p=win.getMouse()
   meanX=p.getX()
   meanY=p.getY()
   sigmaX=eval(input("Please enter sigmaX for blue:"))
   sigmaY=eval(input("Please enter sigmaY for blue:"))
   numPoints=eval(input("How many blue samples:"))
   points=generatePoints(meanX,meanY,sigmaX,sigmaY,numPoints)
   savePoints(points,'blues.txt')
   plotPoints(points,win,'blue')
   print(numPoints,"blue samples has written to blues.txt.")

   print("Please click on window for meanX and meanY for red samples.")
   p=win.getMouse()
   meanX=p.getX()
   meanY=p.getY()
   sigmaX=eval(input("Please enter sigmaX for red:"))
   sigmaY=eval(input("Please enter sigmaY for red:"))
   numPoints=eval(input("How many red samples:"))
   points=generatePoints(meanX,meanY,sigmaX,sigmaY,numPoints)
   savePoints(points,'reds.txt')
   plotPoints(points,win,'red')
   print(numPoints,"red samples has written to reds.txt.")

   print("Data generator has successfully finished.")
   print("Please click to close the window.")
   win.getMouse()
   win.close()

main()

