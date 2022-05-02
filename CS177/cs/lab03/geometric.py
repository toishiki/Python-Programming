import math
def geometricSum(a,r,n):
    geometricSum=0
    total = 0
    for i in range(1,n+1):
        geometricSum = geometricSum+(a*(r**(i-1)))
        print("Term",i,"= %.2f" % (a*(r**(i-1))))
    return geometricSum

def main():
    
    print("Calculate the sum of geometric series")

    a=eval(input("a? "))
    r=eval(input("r? "))
    n=eval(input("n? "))
    total = geometricSum(a,r,n)
    print("Sum =", total)
     
           
  
main()
