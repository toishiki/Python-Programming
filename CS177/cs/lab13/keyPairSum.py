
df1=[]
df2=[]

def keyPairsum(d,number):
    keys=list(d.keys())
    for i in range(len(keys)):
        for j in range(i+1,len(keys)):
            if d[keys[i]] + d[keys[j]] == number:
                   
    #alternative:
    #for i in d:
    #    for j in d:
    #        if i!=j:
    #            if d[i]+d[j]==number:
    #               df1.append(i)
    #               df2.append(j)
    
                    df1.append(keys[i])
                    df2.append(keys[j])
    return(df1,df2)

def main():
    d=eval(input("Enter a dictionary: "))
    number=eval(input("Enter a number: "))
    l1,l2=keyPairsum(d,number)
    #a=len(l1)//2
    for i in range(len(l1)):
        print(l1[i],"and",l2[i],"forms a pair whose sum is squal to",number)

main()
