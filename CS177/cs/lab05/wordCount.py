def wordCount():

    File1= open('c.txt', 'r')
    lines=File1.readlines()

    File2 = open('d.txt','w') 

    for line in lines:
        sum=0

        for token in line.split():
            if (token == 'apple'):
                sum=sum+1
        File2.write(str(sum) + '\n')

    File1.close()
    File2.close()
    
wordCount()
    
