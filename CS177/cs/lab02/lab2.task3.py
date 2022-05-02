import math
def main():
    height = eval(input("Enter a height?"))
    value = (2*height)/9.81
    result= math. sqrt(value)
    final = 1/result
    print("The time to fall is:", final)
main()
