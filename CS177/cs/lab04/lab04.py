from graphics import*

def main():
    win = GraphWin("Lab04", 400,400)
    win.setCoords(0, 0, 400, 400)

    cir=Circle(Point(100,50),40)
    cir.draw(win)
    rect=Rectangle(Point(300,300),Point(350,350))
    rect.draw(win)

    cir.setFill("red")
    rect.setFill("blue")

    t1=cir.getCenter()
    x1=t1.getX()
    y1=t1.getY()

    t1text=Text(Point(x1,y1),"Circle")
    t1text.draw(win)

    t2=rect.getCenter()
    x2=t2.getX()
    y2=t2.getY()

    t2text=Text(Point(x2,y2),"Square")
    t2text.draw(win)

    while True:
        time.sleep(0.02)
          
        if cir.getCenter().getX()>=400 and rect.getCenter().getX()<=0:
            break
        if cir.getCenter().getX()<=400:  
            cir.move(10,0)
            t1text.move(10,0)
        if rect.getCenter().getX()>=0:
            rect.move(-10,0)
            t2text.move(-10,0)
            
    win.getMouse()
    win.close()

    
    
main()    
