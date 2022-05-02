def addStrings(s1,s2):
    i=len(s1)-1
    j=len(s2)-1
    carry = 0
    result =""
    
    while (carry > 0 or i >=0 or j>=0):
        if i>=0:
            a=ord(s1[i])-ord('0')
        else:
            a=0
        if j>=0:
            b=ord(s2[j])-ord('0')
        else:
            b=0
            
        s3=a+b+carry
        
        result=str(s3%10)+result
        carry=s3//10
        
        i-=1
        j-=1
        
    return result

def main():
    str1=input('input string 1:')
    str2=input('input string 2:')
    print(addStrings(str1,str2))


main()
