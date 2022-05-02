def leapYear(x):
    if x%400==0:
        print("The year",x, "is a leap year")
    else:
        if ((x%4==0) and (x%100!=0)):
            print("The year",x,"is a leap year")
        else:
            print("The year",x,"is not a leap year")
        
def main():
    x=eval(input("Enter the year:"))
    leapYear(x)
main()
