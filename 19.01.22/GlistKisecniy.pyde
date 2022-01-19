x = 1
def setup():
    size(500,500)
    frameRate(30)


def draw():
    global x
    background(30,0,50)
    fill(random(50,100))
    ellipse(x,x,random(10,40),random(10,30))
    x = x + 1
