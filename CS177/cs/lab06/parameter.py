
def GetNumbers():
    file1=open('a.txt','r')
    lines=file1.readlines()
    for i in range(len(lines)):
        lines[i] = int(lines[i])
    print(lines)
    return lines

def Update(file2):
    
    for line in file2:
        a=1
        for i in range (1,line+1):
                a=a*i
                print(a)
        

def main():
    Update(GetNumbers())
    
    
main()
    
    
