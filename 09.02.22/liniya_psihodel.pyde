angle = 0

def setup():
    size(600,600)

def draw():
    global angle
    translate(300,300)
    rotate(radians(angle))
    stroke(random(0,100))
    line(0,0,100,100)
    angle = angle + 1
