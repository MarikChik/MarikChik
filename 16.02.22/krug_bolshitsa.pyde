ellipseSize = 0
startEllipseSize = 500

def setup():
    size(600,600)
    fill(50,150,50)
    
def draw():
    global ellipseSize
    background(100,50,50)
    translate(300,300)
    ellipse(0,0,ellipseSize,ellipseSize)
    ellipseSize = ellipseSize + 20
    if ellipseSize == startEllipseSize:
      fill (random(0,100),random(0,200),random(0,200))
      ellipseSize = 0
    
