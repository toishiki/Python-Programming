def mergeLists(l1,l2):
    i=0
    j=0
    m=l1+l2
    for i in range(len(m-1),1,-1):
        for j in range(1,i):
            if m[j-1]>m[j]:
                m[j-1],m[j]=m[j-1],m[j]
        
    return m


def main():
    l1=eval(input("first list:"))
    l2=eval(input("second list:"))
    print(mergeLists(l1,l2))
 
main()

#I tried to use the comparison between two numbers and do some exchange, but it seems the while loop does not give the right decision

