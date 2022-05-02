def calculator(x,y,z):
    if z=='+':
        res=x+y
    if z=='-':
        res=x-y
    if z=='*':
        res=x*y
    if z=='/':
        res=x/y
    print("The result of the arithmetric operation",z,"on the two numbers is",res)

def main():
    a=eval(input("Enter the first number:"))
    b=eval(input("Enter the second number:"))
    c=input("Enter the arithmetic operation:")
           
    calculator(a,b,c)

main()
