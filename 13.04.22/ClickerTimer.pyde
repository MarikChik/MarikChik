secs = 30
clicks = 0


def setup():
    size(1000,500)
    frameRate(60)
    
def draw():
    global secs,clicks
    background (200,255,200) 
    fill(255,10,10)
    rect(415,150,200,200)
    textSize(25)
    text("Seconds:",50,50)
    text(secs,47,75)
    text("Clicks:",850,50)
    text(clicks,879,75)
    
    fill(40,125,40)
    rect(850,400,100,50)
    fill(10,10,10)
    textSize(15)
    text("Reset",875,425)
    
    
    if clicks < 30:
        secs = secs - 0.02
        
    



def mouseClicked():
    global secs, clicks
    if mouseX > 415 and mouseX < 615 and mouseY > 150 and mouseY < 350:
        clicks = clicks + 1
    if mouseX > 850 and mouseX < 950 and mouseY > 400 and mouseY < 450:
        clicks = 0 
        secs = 30
    
