bg = 250
drawCol = 0
pixSizeMain = 5
pixSize1 = 5
pixSize2 = 10
r = 0
g = 0
b = 0
TextValue = 1

def setup():
    size(800,800)
    background(bg)
    frameRate(250)
def draw():
     global pixSizeMain
     global pixSize1
     global pixSize2
     textSize(15)
     
     fill(176, 224, 230)
     rect(600,-1,600,1000)
     
     
     
     fill(100,150,40)
     rect(650,630,100,50)  # size
     fill(0,0,0)
     text(u"Size",685,660)

    
     fill(40,100,150)
     rect(650,570,100,50)  # clear
     fill(0,0,0)
     text(u"Clear",680,600)
     
     fill(0,0,0)
     text(u"Colors:",665,350)
     
     
     fill(200,10,10)
     rect(700,380,50,50)  # r
     
     fill(10,200,10)
     rect(700,440,50,50)  # g
     
     fill(10,10,200)
     rect(700,500,50,50)  # b
     
     fill(10,10,10)
     rect(640,390,50,70)  # blac
     
     fill(255,255,255)
     rect(640,470,50,70)  # whit
     
     
     
     if mousePressed:
       if mouseX > 1 and mouseX < 600 and mouseY > 1 and mouseY < 1000:
        stroke(r,g,b)
        fill(r,g,b)
        rect(mouseX, mouseY,pixSizeMain,pixSizeMain)
        stroke(0,0,0)
        
        
        
        
        
def mouseClicked():
    global bg,pixSizeMain,pixSize2,pixSize1,drawCol,r,g,b
    if mouseX > 650 and mouseX < 750 and mouseY > 630 and mouseY < 680:
        if pixSizeMain==pixSize1:
            pixSizeMain=pixSize2
            TextValue = 1
        else:
            pixSizeMain=pixSize1  
            
        if pixSizeMain==pixSize2:
            TextValue = 0
            

    if mouseX > 650 and mouseX < 750 and mouseY > 570 and mouseY < 620:
        background(bg)
        
        
    if mouseX > 700 and mouseX < 750 and mouseY > 380 and mouseY < 430:
        r = 255
        g = 0
        b = 0
        
    if mouseX > 700 and mouseX < 750 and mouseY > 440 and mouseY < 490:
        r = 0
        g = 255
        b = 0
        
    if mouseX > 700 and mouseX < 750 and mouseY > 500 and mouseY < 550:
        r = 0
        g = 0
        b = 255
    
    if mouseX > 640 and mouseX < 690 and mouseY > 390 and mouseY < 460:
        r = 0
        g = 0
        b = 0
        
    if mouseX > 640 and mouseX < 690 and mouseY > 470 and mouseY < 540:
        r = 255
        g = 255
        b = 255
