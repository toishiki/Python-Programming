def makeZero(matrix):
    m = len(matrix)
    n = len(matrix[0])
    idm=[]
    idn=[]
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                idm.append(i)
                idn.append(j)
    for id1 in range(len(idm)):
        for k in range(m):
            matrix[k][idn[id1]]=0
        for l in range(n):
            matrix[idm[id1]][l]=0
                
                
    return matrix

def main():
    matrix=eval(input("Enter a matrix: "))
    print("The matrix after making Zeros is: ", makeZero(matrix))

main()
    
