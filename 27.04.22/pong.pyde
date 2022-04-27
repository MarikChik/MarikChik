ellX = 300
ellY = 50
rectX = 250
r = 30
Tr = 200
Tg = 40
Tb = 30
g = 255
b = 100
scorVal = 0
rankVal = 0
fallSpd = 2
moveSpd = 5
rankName = "ok."


def setup():
    size(600,500)
    rectMode(CENTER)
    global modeX
    global modeY
    modeX = "right"
    modeY = "down"
def draw():
    global ellX,ellY,r,g,b,modeX,modeY,rectX,scorVal,Tr,Tb,Tg,fallSpd,moveSpd,rankVal,rankName
    background(10,10,50)
    fill(r,g,b)
    ellipse(ellX,ellY,50,50)
    fill(50,50,255)
    rect(rectX,450,80,20)
    textSize(15)
    text(rankName,10,60)
    fill(Tr,Tg,Tb)
    text("SCORE:" , 10,30)
    text(scorVal,70,30)
    
    if modeX == "right":
        ellX += fallSpd
    if modeX == "left":
        ellX -= fallSpd
    if modeY == "down":
        ellY += fallSpd
    if modeY == "up":
        ellY -= fallSpd
        
    if ellX >= 575:
        modeX = "left"
    if ellX <= 20:
        modeX = "right"
    if ellY <= 18:      
        modeY = "down"
    if ellY >= 415 and ellY <= 465 and (ellX >= (rectX - 40) and ellX <= (rectX + 40)):
        modeY = "up"
        fallSpd = fallSpd + 0.10
        moveSpd = moveSpd + 0.05
        scorVal = scorVal + 10
        rankVal = rankVal + 1
        Tr = random(150,250)
        Tg =  random (60,250)
        Tb = random(100,220)
        
    if ellY >= 600:
        r = random(30,240)
        g = random(30,240)
        b = random(30,240)
        ellY = 40
        ellX = random(150,450)
        scorVal = 0
        fallSpd = 2
        moveSpd = 5
        rankVal = 0
        rankName = "ok."
    
        
    if rankVal >= 5 and rankVal <= 10:
        rankName = "Good!"
        
    if rankVal >= 10 and rankVal <= 15:
        rankName = "Awesome!"
        
    if rankVal >= 15 and rankVal <= 20:
        rankName = "Golly!"
        
    if rankVal >= 20 and rankVal <= 25:
        rankName = "Keep it up!"
    
    if rankVal >= 25 and rankVal <= 30:
        rankName = "Unbelivable!"
    
    if rankVal >= 30 and rankVal <= 40:
        rankName = "IMPOSSIBLE!"
        
        


    if keyPressed:
        if key == 'a' or key == 'A' or key == 'ф' or key == 'Ф':
            if rectX >= 40:
                rectX = rectX - 5
            else:
                rectX = rectX
        if key == 'd' or key == 'D' or key == 'в' or key == 'В':
            if rectX <= 560:
                rectX = rectX + 5
            else:
                rectX = rectX
            
        
