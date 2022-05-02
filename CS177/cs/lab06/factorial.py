def fac(x):
    a=1
    for i in range(1,x+1):
        a=a*i
    return a

def main():
    n=eval(input("Please enter a number:"))
    print("the factorial of",n,"is:", fac(n))

main()
    
