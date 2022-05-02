def calculateASCIISum():
    word= input('Please enter a word:')
    length=len(word)
    sum=0
    for i in range (0,length):
        letter=word[i]
        asciicode=ord(letter)
        sum=sum+asciicode
    print(sum)
    
calculateASCIISum()
