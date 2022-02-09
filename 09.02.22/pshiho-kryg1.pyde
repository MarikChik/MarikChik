angle = 0
x = 300

def setup():
    size(600,600)

def draw():
    global angle
    global x
    translate(x,300)
    rotate(radians(angle))
    fill(random(0,120))
    ellipse(0,0,random(20,100),random(40,150))
    angle = angle + 1
    x = x + 1
