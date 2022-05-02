
def stddev(list1):
    var=0
    N=len(list1)
    mu=sum(list1)/N
    for i in range (0,N):
        var=(list1[i]-mu)**2+var
        varf=(var/N)**(1/2)
    print("mean:",mu)
    print("stddev:",varf)
        

def main():
    file1=open('b.txt','r')
    lines=file1.readlines()
    for line in lines:
        floatlist = line.split() 
        for i in range(len(floatlist)):
            floatlist[i] = float(floatlist[i])

        stddev(floatlist)

main()
    
