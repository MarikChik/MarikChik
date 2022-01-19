x = 1000
y = 1600
z = 1300


def setup():
    size(600,600)
    
def draw():
    global x
    global y
    global z
    
    background(0,50,75)
    noFill()
    ellipse(300,300,x,x)
    ellipse(300,300,y,y)
    ellipse(300,300,z,z)
    x = x - 10
    y = x - 5
    z = x - 1
    
