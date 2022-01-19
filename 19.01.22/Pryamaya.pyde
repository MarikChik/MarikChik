x = 1

def setup():
    size(500,500)
    
def draw():
    global x
    translate(249,249)
    fill(random(0,100))
    strokeWeight(1)
    stroke(random(0,100))
    ellipse(x,x,1,1)
    x = x + 1
    
