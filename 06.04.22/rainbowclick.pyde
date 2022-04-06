ClickValue = 0
r = 255
g = 0
b = 0
br = 255
bg = 255
bb = 255

def setup():
    frameRate(100)
    size(800,800)
    
def draw():
    background(br,bg,bb)
    fill(r,g,b)
    rect(300,300,210,220)
    textSize(25)
    fill(0,0,0)
    text(u"Clicks:",370,200)
    text(ClickValue,390,250)
    
def mouseClicked():
    global ClickValue,r,g,b,br,bg,bb
    if mouseX > 300 and mouseX < 510 and mouseY > 300 and mouseY < 520:
        ClickValue = ClickValue + 1
        r = random(10,250)
        g = random(10,250)
        b = random(10,250)
        br = random(240,255)
        bg = random(240,255)
        bb = random(240,255)
        
    
