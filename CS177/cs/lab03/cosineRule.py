import math

def main():
    a=eval(input("Enter length of side a: "))
    b=eval(input("Enter length of side b: "))
    c=eval(input("Enter length of side c: "))

    #ab
    val1=a**2+b**2-c**2
    val2=val1/2/a/b
    rad= math.acos(val2)
    deg= math.degrees(rad)
    degf=round(deg,2)
    print("The angle between a and b is:", degf, "degrees")

    #bc
    val1=b**2+c**2-a**2
    val2=val1/2/c/b
    rad= math.acos(val2)
    deg= math.degrees(rad)
    degf=round(deg,2)
    print("The angle between b and c is:", degf, "degrees")
    
    #ca
    val1=c**2+a**2-b**2
    val2=val1/2/c/a
    rad= math.acos(val2)
    deg= math.degrees(rad)
    degf=round(deg,2)
    print("The angle between c and a is:", degf, "degrees")

main()
    
