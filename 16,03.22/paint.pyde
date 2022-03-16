def setup():
    size(800,800)
    background(255,255,255)
def draw(): 
    if mousePressed:
        stroke(0,0,0)
        fill(0,0,0)
        rect(mouseX, mouseY, 10, 10 )
