import math
from graphics import*

def caesarEncipher(textMessage, shift):
    textMessage=textMessage.upper()
    cipher=""
    for i in textMessage:
        num=ord(i)+shift
        if num>0:
            if (num-64)%26>0:
                res=(num-64)%26+64
            else:
                res=90
        elif num<=0:
            if (num+64)%(-26)<0:
                res=(num-64)%(-26)+90
            else:
                res=65
        cipher += chr(res)
    return cipher

def caesarDecipher(cipher, shift):
    cipher=cipher.upper()
    decipher=""
    for i in cipher:
        num=ord(i)-shift
        if num>0:
            if (num-64)%26>0:
                res=(num-64)%26+64
            else:
                res=90
        elif num<=0:
            if (num+64)%(-26)<0:
                res=(num-64)%(-26)+90
            else:
                res=65
        decipher += chr(res)
    return decipher

def Cipher_Wheel(message,cipher):
    win=GraphWin("Cipher Wheel",600,600)
    win.setBackground('yellow')
    c1=Circle(Point(300,250),160)
    c2=Circle(Point(300,250),200)
    c3=Circle(Point(300,250),240)
    c1.draw(win)
    c2.draw(win)
    c3.draw(win)

    length=len(message)

    for a in range(0,361,math.ceil(360/length)):
        b=math.radians(a)
        x1=300+160*math.cos(b)
        y1=250+160*math.sin(b)
        x2=300+240*math.cos(b)
        y2=250+240*math.sin(b)
        spli=Line(Point(x1,y1),Point(x2,y2))
        spli.draw(win)

    count=-1
        
    for c in range(math.ceil(180/length),361,math.ceil(360/length)):
        if count<length-1:
            count=count+1
            d=math.radians(c)
            x3=300+180*math.cos(d)
            y3=250+180*math.sin(d)
            x4=300+220*math.cos(d)
            y4=250+220*math.sin(d)
        
            text1=Text(Point(x4,y4),message[count])
            text1.draw(win)
            text2=Text(Point(x3,y3),cipher[count])
            text2.draw(win)
    
def main():
    encipher=input("Please input the message to encode:")
    svalue=eval(input("Please input a shift value:"))
    cipher=caesarEncipher(encipher, svalue)
    decipher=caesarDecipher(cipher,svalue)
    Cipher_Wheel(encipher,cipher)
    print("CaesarCipher:", cipher)
    print("CaesarDec:",decipher)
 
  

main()

