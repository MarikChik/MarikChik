sizeel = 5

def setup():
    size(800,800)
    background(100,50,100)
def draw():
    global sizeel
    
    if mousePressed:
        ellipse(400,400,sizeel,sizeel)
        if sizeel < 300:
            sizeel = sizeel + 1
        else:
            background(100,50,100)
            sizeel = 0
    else:
        background(100,50,100)
        sizeel = 0
    
