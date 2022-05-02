def secLargest(mlist):
    n1=n2=mlist[0]
    maxpos=pos=0
    for i in range(len(mlist)):
        if mlist[i] > n1:
            n1,n2=mlist[i],n1
            pos = maxpos
            maxpos= i
        else:
            if n1>mlist[i]>n2:
                n2=mlist[i]
                pos=i
    
    return(n2,pos+1)

def main():
    mylist=eval(input("Enter a list of numbers:"))
    a,b=secLargest(mylist)
    print("The second largest number is",a, "and is found at the",b,"position in the list.")
    
main()
