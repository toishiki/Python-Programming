from part3 import *
from part4 import*
import matplotlib.pyplot as pyplot


def plotBarChart(states):
    pos = [1,3,5,7,9,11,13,15,17,19]
  
    name=[]
    number=[]
    for i in range(10):
        name. append(states[i][0])
        number.append(states[i][1])
  
    bar = pyplot.bar(pos, number, width=1, color='LightCoral', align='center')

    pyplot.xticks(pos, name)
  
    pyplot.title('State Statistics')
    pyplot.ylabel('# of students')
    pyplot.setp(pyplot.xticks()[1], rotation=-15)
    pyplot.axis([0,20,0,20])
    pyplot.show()
    

def plotPieChart(counts):

    labels = 'Both Python and Java','Only Python','Only Java'
    colors = ['LightCoral','yellowgreen','gold']
    pyplot.pie(counts, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=90)
    pyplot.legend(loc=3)
    pyplot.axis('equal')
    pyplot.show()
    

