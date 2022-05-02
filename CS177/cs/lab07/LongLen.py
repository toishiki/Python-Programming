def Longlen(x):
    a=x.split()
    lx=len(x[0])
    for i in a:
        if lx < len(i):
            lx=len(i)
            lw=i
    return(lx,lw)
def main():
    st=(input("Enter a string:"))
    a,b=Longlen(st)
    print("The longest word in the given string is",b)
    print("Its length is",a)
main()
