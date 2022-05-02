import matplotlib.pyplot as pyplot

def plotBarGraph(applicationlist):
    
    
    pos1 = [1,6,11,16]
    pos2 = [2,7,12,17]
    pos3 = [3,8,13,18]
    pos4 = [2.5,7.5,12.5,17.5]
    d90=applicationlist[1]
    d00=applicationlist[2]
    d10=applicationlist[3]
 
    names = applicationlist[0]
 
    bar1 = pyplot.bar(pos1, d90, width=1, color='blue', align='center')
    bar2 = pyplot.bar(pos2, d00, width=1, color='pink', align='center')
    bar3 = pyplot.bar(pos3, d10, width=1, color='red', align='center')
 
    pyplot.legend((bar1, bar2, bar3), ('1990','2000','2010'), loc=1)
    pyplot.xticks(pos4, names)
 
    pyplot.ylabel('Number of Student Applications')
    pyplot.setp(pyplot.xticks()[1], rotation=15)
    pyplot.axis([0,20,500,4500])
    pyplot.show()

def scatterPlot(X,Y,Z):
    pyplot.plot(X,Y , linestyle = '-', color='blue',label = 'Pizza')
    pyplot.plot(X,Z , linestyle = '--',color='red',marker='o',label = 'Chips and Fish')
    pyplot.xlabel('Year')
    pyplot.ylabel('Number of items eaten per year')
    pyplot.title('Consumption of fast food by Australian teenagers')
    pyplot.legend()
    pyplot.show()

def Piechart(X):
    labels = 'Germany', 'France', 'United Kingdom', 'Italy','Spain','Poland','All other countries'
    colors = ['yellowgreen','gold','lightskyblue','pink','red','brown','yellow','maroon']
    pyplot.pie(X, labels=labels, colors=colors,autopct='%1.1f%%', shadow=True, startangle=90)
    pyplot.legend(loc=2)
    pyplot.axis('equal')
    pyplot.show()
   
def main():
    applicationlist=[['Biology', 'Engineering','Business,','Social Work'],
                     [3000,4000,2000,1000],
                     [1500,2500,3000,1400],
                     [800,600,4000,1800]]
    plotBarGraph(applicationlist)
    
    Year=[1975,1980,1985,1990,1995,2000]
    amP=[5,18,38,60,83,83]
    amF=[100,85,93,65,50,38]
    scatterPlot(Year,amP,amF)

    sizes = [16.6,12.8,12.3,11.9,9,7.7,29.7]
    Piechart(sizes)
    
main()
