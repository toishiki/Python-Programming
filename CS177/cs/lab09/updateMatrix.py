def updateMatrix(matrix):
    raw=len(matrix)
    for i in range(raw):
        for j in range(len(matrix[i])):
            if i%2==0:
                matrix[i][j]+=1
            else:
                matrix[i][j]+=2
                
    print(matrix)

def main():
    matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    updateMatrix(matrix)

main()
