import math

def horizontalHit(d1, d2, h):   
    t=math.sqrt(2*h/9.8)
    v=(d1+d2)/(2*t)
    return(t,v)
    
    
def rampHit(d1,d2,h,a):
    deg=math. radians(a)
    t=math.sqrt (((2*h+math.tan(deg)*(d1+d2))/9.8))
    v=(d1+d2)/(2*(math.cos(deg))*t)
    return(t,v)

def main():
    d1=eval(input("Enter the distance d1: "))
    d2=eval(input("Enter the distance d2: "))
    h=eval(input("Enter the height of the stage: "))
    a=eval(input("Enter the angle of the ramp: "))

    t1,v1= horizontalHit(d1,d2,h)
    t2,v2= rampHit(d1,d2,h,a)

    print("\n It takes",round(t1,2),"seconds for the bird to hit the pig.")
    print(" The bird must travel at a velocity of %.2f."%v1)
    print("\n It takes",round(t2,2),"seconds for the bird to hit the pig when the bird is running on the ramp.")
    print(" The bird must travel at a velocity of", round(v2,2), "when the bird is running on the ramp.") 

main()
