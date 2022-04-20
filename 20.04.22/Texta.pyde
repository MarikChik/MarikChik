txtVal=u""
txtVal = key

def setup():
    size(700,600)
    frameRate(10)
    
def draw():
    global txtVal
    fill(20,30,20)
    if keyPressed == True:
        txtVal = txtVal + key
        textSize(25)
        fill(random(10,200),random(10,200),random(10,200)) 
        background(255)
        text(txtVal,10,300)
    if key == BACKSPACE:
        background(255)
