HPval = 100
DMGval = 15
DMGtake = 15
HPenem = 125
turn = 1 
BGX = 10
BGY = 10
BGX1 = -300
BGY1 = 190
BGX2 = -700
BGY2 = 300
NXTURN = 0



def setup():
    size(800,600)
    
def draw():
    global HPval,DMGval,BGX,BGY,HPenem,BGX1,BGY1,BGX2,BGY2
    
    
    push()
       
    background(75,0,130)  # задник
    fill(128,0,128)
    rect(1,480,1000,1000)
    
    BGX = BGX + 2  
    fill(188,143,143)
    ellipse(BGX,BGY,300,80)
    if BGX >= 1000:
        BGX = -120
        BGY = random(30,250)
        
    BGX1 = BGX1 + 3 
    fill(188,143,143)
    ellipse(BGX1,BGY1,320,83)
    if BGX1 >= 1000:
        BGX1 = -150
        BGY1 = random(1,350)
        
    BGX2 = BGX2 + random(1,3) 
    fill(188,143,143)
    ellipse(BGX2,BGY2,320,83)
    if BGX2 >= 1000:
        BGX2 = -150
        BGY2 = random(1,400)
    
    pop()
    
    push()
    
    if turn%2 == 1:
        fill(224,255,255,200) # меню перс
        rect(25,25,250,100)
        fill(0,0,0)
        textSize(15)
        text("HP:",50,50)
        text(HPval,80,50)
        text("DMG:",50,75)
        text(DMGval,90,75)
        
    
        
        fill(224,235,235,130) # меню дейст
        rect(40,100,220,50)
        fill(0,0,0)
        
        
        
        
        fill(219,112,147) # атк
        rect(55,105,40,35)
        fill(0,0,0)
        text("ATK",60,125)
        
        fill(144,238,144)  #  хил
        translate(50,0) 
        rect(55,105,40,35)
        fill(0,0,0)
        text("HEAL",58,125)
        
        fill(127,255,212) #  хил
        translate(50,0)  
        rect(55,105,40,35)
        fill(0,0,0)
        text("INCR",58,125)
        
        fill(128,128,150)  # блк
        translate(50,0) 
        rect(55,105,40,35)
        fill(0,0,0)
        text("BLCK",58,125)
    
    pop()
    
    
    push()
    
    if turn%2 == 0:
   
        fill(255,228,225,200) # меню враг
        rect(525,25,250,100)
        fill(0,0,0)
        textSize(15)
        text("HP:",550,50)
        text(HPenem,580,50)
        text("DMG:",550,75)
        text(DMGtake,590,75)
        text("TURN IN:",550,100)
    
    pop()
    
    
    fill(0,250,154)  #  перс
    rect(100,400,100,100)
    
    fill(220,20,60)  #  враг
    rect(600,400,100,100)
    
def mouseClicked():
    global HPval,DMGval,HPenem,turn,DMGtake  
    
    # атк я (ИЗМЕНИТ НА УРОН ВРАГУ)
    if mouseX > 55 and mouseX < 95 and mouseY > 105 and mouseY < 140:
        turn = turn + 1
