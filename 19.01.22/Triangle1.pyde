x = 1  
a = 1
def setup():
    size(500,500)
    
def draw():
    global x
    global a

    fill(x)
    noStroke()
    triangle(250,150 - a,150 - x,300 + x,350 + x,300 + a)
    
    x = x + 1
    a = a + 1
    

