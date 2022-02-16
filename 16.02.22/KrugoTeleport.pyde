x = 50

def setup():
    size(600,600)
    fill(10,10,10)
    
def draw():
    global x
    background(50,50,100)
    ellipse(x,x,100,100)
    x = x + 5
    if x == 550:
      fill (random(0,200),random(0,200),random(0,150))
      x = x - 500
    
