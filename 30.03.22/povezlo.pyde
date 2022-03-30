bg = 250
textVal = 0
text1 = u"повезло-повезло"
text2 = u"не повезло-повезло"
def setup():
    size(700,700)
def draw():
    global bg 
    global textVal 
    background(bg)
    fill(50,50,50)
    rect(250,300,200,100)
    
    textSize(20)
    textAlign(CENTER,CENTER)
    if textVal % 2 == 1:
        fill(75,150,76)
        text(text2,350,350)
    else:
        fill(150,75,76)
        text(text1,350,350)
    
    
    
def mouseClicked():
    global bg
    global textVal
    if mouseX < 450 and mouseX > 250 and mouseY < 400 and mouseY > 300:
        bg = random(0,250)
        textVal = textVal + 1
