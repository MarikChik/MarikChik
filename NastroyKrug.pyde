ellipseSize = 1
spd = 3
r = 0
g = 0
b = 0

def setup():
    global mode
    size(1000,500)
    mode = "Bolshitsya"
def draw():
    global ellipseSize 
    global mode
    global spd
    global r
    global g
    global b
    background (255,255,255) 
    fill(r,g,b)
    ellipse(500,250,ellipseSize,ellipseSize)
    
    fill(0,0,0)
    rect(880,360,50,50)  # Blk
    fill(255,255,255)
    text(u"BLK",894,390)
    
    fill(0,0,random(200,255))
    rect(940,360,50,50)  # Rnd
    fill(255,255,255)
    text(u"RND",953,390)
    
    fill(255,255,255)
    rect(885,425,100,50)  # speed
    fill(0,0,0)
    text(u"Speed:",900,455)
    
    fill(0,0,0)
    text(spd,940,455)
    
    if mode == "Bolshitsya":
        ellipseSize += spd
    if mode == "Menshitsya":
        ellipseSize -= spd

    if ellipseSize <= 50 :
        mode = "Bolshitsya"
    if ellipseSize >= 500:
        mode = "Menshitsya"
        
        
        
def mouseClicked():
    global spd, r,g,b
    if mouseX > 885 and mouseX < 985 and mouseY > 425 and mouseY < 475:
        spd = spd + 3
        if spd > 15:
            spd = 3
            
    if mouseX > 940 and mouseX < 990 and mouseY > 360 and mouseY < 410:
        r = random(20,200)
        g = random(20,200)
        b = random(20,200)
        
    if mouseX > 880 and mouseX < 930 and mouseY > 360 and mouseY < 410:
        r = 0
        g = 0
        b = 0
