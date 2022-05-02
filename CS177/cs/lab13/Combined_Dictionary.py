A = {'a':7, 'b':2, 'c':5, 'd':1}
B = {'a':3, 'd':11, 'e':6}
C={}

for i in A:
    for j in B:
        C[i]=A[i]
        C[j]=B[j]
for i in A:
    for j in B:
        if i==j:
            if A[i]>B[i]:
                C[i]=A[i]
            else:
                C[i]=B[i]
            
print("Dictionary A = ",A)
print("Dictionary B = ",B)
print("The combined dictionary is:",C)
