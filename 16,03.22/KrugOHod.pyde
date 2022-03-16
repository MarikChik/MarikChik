x = 400
y = 400

def setup():
    size(800,800)
def draw():
    background(255,255,255)
    global x
    global y
    fill(0,255,0)
    ellipse(x,y,50,50)
    if mousePressed:
        x = mouseX
        y = mouseY
        
