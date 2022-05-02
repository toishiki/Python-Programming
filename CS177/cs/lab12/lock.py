from random import randrange
from graphics import * 
 
class Lock:
    def __init__(self):
        self.password = 'LOCK'
        self.errMsg = ''
        self.status = 'New'  
        self.drawInitLock()   
 
    def drawInitLock(self):
        self.win = GraphWin('Resettable combination lock',500,500)
        self.win.setCoords(0, 0 , 500, 500)
        self.rect = Rectangle(Point(50, 100),Point(450,400))
        self.rect.setFill('Lavender')
        self.rect.draw(self.win)
        
        cir1 = Circle(Point(100,300), 40)
        cir2 = Circle(Point(200,300), 40)
        cir3 = Circle(Point(300,300), 40)
        cir4 = Circle(Point(400,300), 40)
        self.circles = [cir1, cir2, cir3, cir4]
 
        for cir in self.circles:
            cir.setFill('Pink')
            cir.draw(self.win)
 
   
        text1 = Text(Point(100,300), 'L')
        text2 = Text(Point(200,300), 'O')
        text3 = Text(Point(300,300), 'C')
        text4 = Text(Point(400,300), 'K')
        self.texts = [text1, text2, text3, text4]
 
        for text in self.texts:
            text.setSize(20)
            text.draw(self.win)
 
    
        self.label = Text(Point(250, 200), self.status)
        self.label.setSize(20)
        self.label.draw(self.win)
        
    def updateTexts(self, value):
        for i in range(4):
            self.texts[i].setText(value[i])
 
    def updateLabel(self):
        self.label.setText(self.status + '\n' +self.errMsg)
 
    def reset(self, password):
        if password=='':
            self.errMsg="(The password should not be empty.)"
            self.updateLabel()
            return False
        elif len(password)!=4:
            self.errMsg="(The password length should be 4.)"
            self.updateLabel()
            return False
        else:
            self.password=password
            self.errMsg=''
            self.status='Reset'
            self.updateTexts(password)
            self.updateLabel()
            return True
                              
 
    def close(self):
        for i in range(4):
            r=randrange(65,91)
            self.texts[i].setText(chr(r))
            self.status="Closed"
            self.updateLabel()
            
 
    def open(self, password):
        if password!=self.password:
            self.errMsg="(The password you entered is incorrect!)"
            self.updateLabel()
            return False
        else:
            self.errMsg=""
            self.status="Opened"
            self.updateTexts(password)
            self.updateLabel()
            return True
 
def main():
    while(True):
        lock = Lock()
 
        password = input('\nPlease enter a new password to reset: ')
        while not lock.reset(password):
            password = input('\nPlease enter a new password to reset: ')
 

        answer = input('\nWant to play with the lock you just created? (yes/no) ')
        if answer.lower() == 'yes':
            lock.close()
 
            attempt = input("\nPlease enter the password to open: ")
            count = 0
            while not lock.open(attempt):
                count += 1
                if count < 3:           
                    print('\nYou only have ' + str(3-count) + ' chances left to enter password.')
                    attempt = input("Try again: ")            
                else:
                    print('\nYou have failed 3 times! You cannot open it anymore!')
                    break
 
        answer = input('\nWant to play with a new lock?(yes/no) ')
        if answer.lower() == 'no':
            lock.win.close()
            break
        else:
            lock.win.close()
 
main()
