def setup():
    size(800,600)
    background(0)

def draw():
    stroke(random(0,200))
    strokeWeight(random(1,30))
    point(random(0,800), random(0,600))
