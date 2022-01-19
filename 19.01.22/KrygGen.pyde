x = 1  

def setup():
    size(500,500)
    colorMode(HSB)
    
def draw():
    global x

    fill(x,x,x)
    ellipse(250,250,60,60)
    
    x = x + 1
