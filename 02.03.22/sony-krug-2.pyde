ellipse_x = 101
ellipse_y = 76
coR = 255
CoG = 0
coB = 0


def setup():
    global modeX
    global coR
    coR = 255
    global coG
    coG = 125
    global coB
    coB = 0
    global modeY
    size(1000,500)
    modeX = "right"
    modeY = "down"
def draw():
    global ellipse_x
    global ellipse_y
    global coR
    global coG
    global coB
    global modeX
    global modeY
    background (5) 
    fill (coR,coG,coB)
    ellipse(ellipse_x ,ellipse_y,200,150)
    if modeX == "right":
        ellipse_x += 2
    if modeX == "left":
        ellipse_x -= 2
    if modeY == "down":
        ellipse_y += 1
    if modeY == "up":
        ellipse_y -= 1
     

    if ellipse_x >= 900:
        modeX = "left"
        coR = (coR + 100) % 250
        coG = (coG + 200) % 250
        coB = (coB + 300) % 250       
    if ellipse_x <= 100:
        coR = (coR + 100) % 250
        coG = (coG + 200) % 250
        coB = (coB + 300) % 250   
        modeX = "right"
    if ellipse_y >= 425:
        coR = (coR + 100) % 250
        coG = (coG + 200) % 250
        coB = (coB + 300) % 250     
        modeY = "up"
    if ellipse_y <= 75:  
        coR = (coR + 100) % 250
        coG = (coG + 200) % 250
        coB = (coB + 300) % 250        
        modeY = "down"
