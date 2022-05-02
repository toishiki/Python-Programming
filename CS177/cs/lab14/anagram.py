def anagram_checkoff(s1,s2):
    a1=[]
    a2=[]
    l=len(s1)
    n=0
    for i in range(l):
        a1.append(s1[i])
        a2.append(s2[i])
    isStillOK=True
    i=0
    j=0
    while (i<l) and isStillOK:
        j=0
        found=False
        while (j<len(a2)) and not found:
            n+=1
            if a1[i]==a2[j]:
                found=True
            else:
                j+=1
        if found:
            a2[j]=None
        else:
            isStillOK = False
            
        i+=1                
    print('Number of Visits:',n)
    return(isStillOK)

def anagram_sort(s1,s2):
    a1=[]
    a2=[]
    l=len(s1)
    v=0
    for i in range(l):
        a1.append(s1[i])
        a2.append(s2[i])
    a1.sort()
    a2.sort()
    matches=True
    for i in range(l):
        for j in range(l):
            if i==j and a1[i]==a2[j]:
                a1[i]=None
                a2[j]=None
                v+=1
                matches=True
            else:
                matches=False
    print('Number of Visits:',v)
    return(matches)

def anagram_count_compare(s1,s2):
    c1 = [0]*26
    c2 = [0]*26
    number_of_vists1=0
    number_of_vists2=0
    number_of_vists3=0
    l=len(s1)

    for i in range(l):
        pos1 = ord(s1[i])-ord('a')
        c1[pos1] = c1[pos1] + 1
        number_of_vists1+=1
    #print(c1,number_of_vists1)
    for i in range(l):
        pos2 = ord(s2[i])-ord('a')
        c2[pos2] = c2[pos2] + 1
        number_of_vists2+=1
    #print(c2,number_of_vists2)
    j=0
    stillOK=True
    while (j<26) and stillOK:
        if c1[j]==c2[j]:
            j+=1
            number_of_vists3+=1
            stillOK=True
        else:
            stillOK=False
    summ=number_of_vists1+number_of_vists2+number_of_vists3
    print('Number of Visits:',summ)
    return stillOK

print(anagram_checkoff('python','typhon'))
print(anagram_checkoff('heart','earth'))

print(anagram_sort('heart','earth'))
print(anagram_sort('python','typhon'))

print(anagram_count_compare('python','typhon'))
print(anagram_count_compare('steel','sleet'))


#Sorry I accidently overwrite the old code, the anagram_ one is the old one before the 1:30pm. The submitted time was overlapped.
#Updated code before 1:50pm and emailed Ruby for extension since we only had one TA. Thanks for the help

