def getASCIIDecoding():

    File1= open('a.txt', 'r')
    lines=File1.readlines()

    File2 = open('b.txt','w')

    for line in lines:
        value=int(line)
        asdecode=chr(value)
        File2.write(asdecode + '\n')

    File1.close()
    File2.close()
    
getASCIIDecoding()
    
