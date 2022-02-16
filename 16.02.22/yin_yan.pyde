ellipseColor = 0
maximumColor = 255

def setup():
    size(600,600)
    fill(50,150,50)
    
def draw():
    global ellipseColor
    global maximumColor
    background(100,50,50)
    translate(300,300)
    ellipseColor = ellipseColor + 1
    fill(ellipseColor)
    ellipse(0,0,100,100)
    if ellipseColor == maximumColor:
        ellipseColor = 0
