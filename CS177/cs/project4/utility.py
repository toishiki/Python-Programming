from graphics import *

def savePoints(points, fileName):
   file = open(fileName,'w')
   for i in points:
      file.write(str(i[0])+','+str(i[1])+'\n')
   pass 
   
def readPoints(fileName):
   a=[]
   file= open(fileName,'r')
   if False:
      return a
   else:
      lines=file.readlines()
      for line in lines:
         for number in line.split(','):
            number=float(number)
            a.append(number)
   b=[]
   for i in range(0,len(a),2):
      b.append((a[i],a[i+1]))
   return(b)
   
def plotPoints(points, win, color):
   for i in range(len(points)):
      pt=Circle(Point(points[i][0],points[i][1]),3)
      pt.draw(win)
      pt.setFill(color)
   pass

