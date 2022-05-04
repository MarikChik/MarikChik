X = 5
X2 = 35

def setup():
    size(600,400)
    frameRate(10)
    
def draw():
    global X,X2
    background(255,255,255)
    for step in range(11):
        fill(random(10,250),random(10,250),random(10,250))
        rect(X,5,X2,35)
        translate(0,35)
    X = X + 5
    if X == 550:
       noLoop()
