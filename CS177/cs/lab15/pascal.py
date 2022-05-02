def pascal(n):
    if n==1:
        return [[1]]
    rows=pascal(n-1)
    lastRow=rows[-1]
    newRow=[]
    newRow.append(1)
    for i in range(1,n-1):
        newRow.append(lastRow[i]+lastRow[i-1])
    newRow.append(1)
    rows.append(newRow)
    return rows

print(pascal(4))

#member name:Henry Hamann
#my name:Shiqi Tang
    
