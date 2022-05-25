HPval = 100 # наиважнейшии переменные
DMGval = 15
DMGtake = 20
HPenem = 125
turn = 1 
HealWait = 0
IncrWait = 0

BGX = 10  # облака
BGY = 10
BGX1 = -300
BGY1 = 190
BGX2 = -700
BGY2 = 300


NXTURN = 0 # ожидание хода

HerX = 200 # местоположение героя

EneX = 560 # местоположение врага
EneY = 400

wait=1  # анимация врага
move=5
AnimVal = "true"
EEyeVal = 0
EEyeSize = 15
EnDmgY = 400

EyeVal = 0  # анимация героя
EyeSize = 20





def setup():
    global Amode
    size(850,600)
    Amode = "wait"
    
def draw():
    global HPval,DMGval,BGX,BGY,HPenem,BGX1,BGY1,BGX2,BGY2,Amode,NXTURN,turn,HerX,EneX,EneY, wait, move,AnimVal,EyeVal,EEyeVal,EnDmgY,EEyeSize
    
    
    push()
       
    background(64, 42, 150)  # задник
    
    fill(201, 239, 255) # луна
    ellipse(825,-10,200,200)
    fill(171, 230, 255)
    ellipse(760,4,30,30)
    ellipse(790,50,20,20)
    ellipse(830,30,40,40)

    
    BGX = BGX + 2      # облака
    fill(188,143,143)
    ellipse(BGX,BGY,330,120)
    if BGX >= 1100:
        BGX = -300
        BGY = random(30,250)
        
    BGX1 = BGX1 + 3 
    fill(188,143,143)
    ellipse(BGX1,BGY1,430,103)
    if BGX1 >= 1350:
        BGX1 = -200
        BGY1 = random(1,350)
        
    BGX2 = BGX2 + 2
    fill(188,143,143)
    ellipse(BGX2,BGY2,360,109)
    if BGX2 >= 1100:
        BGX2 = -250
        BGY2 = random(1,300)
        
        
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
        
        #  хил кноп
        
        if HealWait == 0:
            fill(144,238,144)
        else:
            fill(194,255,194)
        translate(50,0) 
        rect(55,105,40,35)
        fill(0,0,0)
        text("HEAL",58,125)
        
        #  увелич кноп
        if IncrWait == 0:
            fill(127,255,212) 
        else:
            fill(227,255,255)
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
                EneX = 550 
                EneY = 400
                EEyeVal = 0
                EEyeSize = 15
            if NXTURN <= 0:
                turn = turn + 1
                Amode == "wait"
                NXTURN = 10000
                HPval = HPval - DMGtake
                EnDmgY = 400
                
                
                
    push() # анимации врага 
    
    pop()
    
    
    
    #  ожидание конца атаки врага
    if Amode == "heal":
            NXTURN = NXTURN- 0.04
            
            
            if NXTURN <= 9:
                AnimVal = "false"
                
                
            if NXTURN <= 0:
                turn = turn + 1
                Amode == "wait"
                NXTURN = 10000
                
    if Amode == "Incr":
            NXTURN = NXTURN- 0.04
            
            
            if NXTURN <= 9:
                AnimVal = "false"
                
                
            if NXTURN <= 0:
                turn = turn + 1
                Amode == "wait"
                NXTURN = 10000
                
                
                
                
    push() # анимации врага 
        
        # урон
    if Amode == "atk" and AnimVal == "true":
        EneX = EneX - move
        EEyeVal = 255
        EEyeSize = 20
        if wait <= 0:
            wait=1
            move=move*(-1)
            
        # атак

    pop()
    
    push() # анимации перса
        
        # атака
    if Amode == "atk" and AnimVal == "true":
        HerX = 210
    else:
        HerX = 200

    
            
        # атак

    pop()
    
    
    fill(0,250,154)  #  перс
    rect(HerX,400,100,100)
    fill(EyeVal,EyeVal,EyeVal)
    rect(HerX+50,425,EyeSize,40)
    rect(HerX+75,425,EyeSize,40)
    
    
    fill(102, 66, 32)  # держалка 1
    rect(EneX-3,420,20,45)
    fill(220,20,60)  #  враг
    rect(EneX,EneY,100,100)
    fill(102, 66, 32) # держалка 2
    rect(EneX+70,420,20,45)
    fill(113, 107, 138)
    rect(EneX-5,375,110,50) # шлем
    fill(208, 196, 255)
    triangle(EneX+50,320,EneX+80,380,EneX+20,380)
    
    fill(EEyeVal,EEyeVal,EEyeVal)
    line(EneX+5,405,EneX+30,425) # глаза
    line(EneX+30,425,EneX+55,405)
    rect(EneX+10,425,EEyeSize,40)
    rect(EneX+35,425,EEyeSize,40)
    
    
    push()  # текст врага об уроне
    textSize(25)
    if AnimVal == "true"and Amode == "atk" and NXTURN >= 8 :
        fill(255, 127, 127, 200)
        text(-DMGval,535,EnDmgY)
        EnDmgY = EnDmgY - 1
    pop()
    

def mouseClicked():
    global HPval,DMGval,HPenem,turn,DMGtake,Amode,NXTURN,AnimVal,HealWait,IncrWait,DMGval
    
    # атк я 
    if mouseX > 55 and mouseX < 95 and mouseY > 105 and mouseY < 140 and turn%2 == 1:
        AnimVal = "true"
        Amode = "atk"
        NXTURN = 10
        turn = turn + 1
        HPenem = HPenem - DMGval
        if HealWait > 0:
            HealWait = HealWait - 1
        if IncrWait > 0:
            IncrWait = IncrWait - 1
        
    # хил я
    if mouseX > 105 and mouseX < 145 and mouseY > 105 and mouseY < 140 and turn%2 == 1 and HealWait == 0:
        AnimVal = "true"
        Amode = "heal"
        NXTURN = 10
        turn = turn + 1
        HealWait = 1
        if HPval < 100:
            HPval = HPval + 25
        if IncrWait > 0:
            IncrWait = IncrWait - 1
            
     # инкр я   
    if mouseX > 155 and mouseX < 195 and mouseY > 105 and mouseY < 140 and turn%2 == 1 and IncrWait == 0:
        AnimVal = "true"
        Amode = "Incr"
        NXTURN = 10
        turn = turn + 1
        if IncrWait == 0:
            IncrWait = 3
            DMGval = DMGval + 15
        if HealWait > 0:
            HealWait = HealWait - 1
