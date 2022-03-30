bg = 250
drawCol = 0
pixSizeMain = 5
pixSize1 = 5
pixSize2 = 10

def setup():
    size(800,800)
    background(bg)
def draw():
     global pixSizeMain
     global pixSize1
     global pixSize2
     fill(40,100,40)
     rect(650,630,100,50)
     
     fill(100,40,40)
     rect(650,570,100,50)
     
     if mousePressed:
        stroke(0,0,0)
        fill(drawCol)
        rect(mouseX, mouseY,pixSizeMain,pixSizeMain)
        
        
        
        
def mouseClicked():
    global bg,pixSizeMain,pixSize2,pixSize1
    if mouseX > 650 and mouseX < 750 and mouseY > 630 and mouseY < 680:
        if pixSizeMain==pixSize1:
            pixSizeMain=pixSize2
        else:
            pixSizeMain=pixSize1
