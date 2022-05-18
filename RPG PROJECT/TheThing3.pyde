HPval = 100 # наиважнейшии переменные
DMGval = 15
DMGtake = 20
HPenem = 125
turn = 1 

BGX = 10  # облака
BGY = 10
BGX1 = -300
BGY1 = 190
BGX2 = -700
BGY2 = 300

NXTURN = 0 # ожидание хода

EneX = 600 # местоположение врага
EneY = 400

wait=1  # анимация врага
move=5
AnimVal = "true"
EyeVal = 0
EnDmgY = 400




def setup():
    global Amode
    size(850,600)
    Amode = "wait"
    
def draw():
    global HPval,DMGval,BGX,BGY,HPenem,BGX1,BGY1,BGX2,BGY2,Amode,NXTURN,turn,EneX,EneY, wait, move,AnimVal,EyeVal,EnDmgY
    
    
    push()
       
    background(64, 42, 150)  # задник
    
    BGX = BGX + 2  # облака
    fill(188,143,143)
    ellipse(BGX,BGY,310,80)
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
    ellipse(BGX2,BGY2,330,83)
    if BGX2 >= 1000:
        BGX2 = -150
        BGY2 = random(1,400)
        
    fill(80,30,130)
    rect(1,350,100,300) # части??
    rect(200,350,300,300)
    rect(600,350,700,300)
    line(30,420,80,420)  # узор частей
    line(200,450,250,450)
    line(440,390,490,390)
    line(689,440,739,440)
    line(750,400,800,400)
    fill(95,32,158)
    rect(1,475,1000,1000) # пол
    fill(89, 16, 43)
    rect(1,510,1000,1000)
    fill(101, 102, 21)
    rect(1,550,1000,1000)
    fill(89, 16, 43)
    rect(1,570,1000,1000)
    
    
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
        
        
        
        
        fill(219,112,147) # атк кноп
        rect(55,105,40,35)
        fill(0,0,0)
        text("ATK",60,125)
        
        fill(144,238,144)  #  хил кноп
        translate(50,0) 
        rect(55,105,40,35)
        fill(0,0,0)
        text("HEAL",58,125)
        
        fill(127,255,212) #  увелич кноп
        translate(50,0)  
        rect(55,105,40,35)
        fill(0,0,0)
        text("INCR",58,125)
        
        fill(128,128,150)  # блк кноп
        translate(50,0) 
        rect(55,105,40,35)
        fill(0,0,0)
        text("BLCK",58,125)
    
    pop()
    
    
    push()
    
    if turn%2 == 0:
   
        fill(255,228,225,200) # меню враг
        translate(20,0)
        rect(525,25,250,100)
        fill(0,0,0)
        textSize(15)
        text("HP:",550,50)
        text(HPenem,580,50)
        text("DMG:",550,75)
        text(DMGtake,590,75)
        text("TURN IN:",550,100)
        text(NXTURN,620,100)
        
    pop()
    
    
    
    #  ожидание конца атаки врага
    if Amode == "atk":
            NXTURN = NXTURN- 0.04
            wait=wait-0.4
            
            if NXTURN <= 9:
                AnimVal = "false"
                EneX = 600 
                EneY = 400
                EyeVal = 0
            if NXTURN <= 0:
                turn = turn + 1
                Amode == "wait"
                NXTURN = 10000
                HPval = HPval - DMGtake
                EnDmgY = 400
                
                
                
    push() # анимации врага 
        
        # атака
    if Amode == "atk" and AnimVal == "true":
        EneX = EneX - move
        EyeVal = 255
        if wait <= 0:
            wait=1
            move=move*(-1)
    
    pop()
    
    
    push()  # текст врага об уроне
    textSize(25)
    if AnimVal == "true" and NXTURN >= 8 :
        fill(150, 25, 25)
        text(-DMGval,630,EnDmgY)
        EnDmgY = EnDmgY - 1
    pop()
    
    
    
    fill(0,250,154)  #  перс
    rect(200,400,100,100)
    
    fill(220,20,60)  #  враг
    rect(EneX,EneY,100,100)
    
    fill(EyeVal,EyeVal,EyeVal)
    line(605,405,630,425)
    line(630,425,655,405)
    rect(610,425,15,40)
    rect(635,425,15,40)


def mouseClicked():
    global HPval,DMGval,HPenem,turn,DMGtake,Amode,NXTURN,AnimVal
    
    # атк я 
    if mouseX > 55 and mouseX < 95 and mouseY > 105 and mouseY < 140:
        AnimVal = "true"
        Amode = "atk"
        NXTURN = 10
        turn = turn + 1
        HPenem = HPenem - DMGval
