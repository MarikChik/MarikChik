angle = 0
x = 300

def setup():
    size(600,600)

def draw():
    global angle
    global x
    translate(300,300)
    rotate(radians(angle))
    background(10,50,90)
    fill(random(0,200),random(10,190),random(0,200))
    noStroke()
    ellipse(0,0,random(90,100),random(100,150))
    angle = angle + 1
    x = x + 1
