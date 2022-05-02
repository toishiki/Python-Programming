def series(n):
    sum = 0
    c = 1
    for i in range(1, 2*n+1, 2):
        sum = sum + c * 4/(i)
        c = -1 * c
    return sum
 
def main():
    print("Program that estimates pi")
    term = eval(input("Number of terms? "))
    s = series(term)
    print("Approximation of pi= ",s)
 
main()
