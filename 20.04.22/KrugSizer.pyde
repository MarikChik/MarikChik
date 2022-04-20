ellSize = 50
r = 20
g = 90
b = 200
scrSpeed = 1

def setup():
    size(700,600)

    
def draw():
    global ellSize,r, g, b,scrSpeed
    background(255)
    ellipse(350,300,ellSize,ellSize)
    fill(r,g,b)
    if keyPressed:
        if key == '+' or key == '=':
            if ellSize <= 500:
                ellSize = ellSize + scrSpeed
            else:
                r = random(20,200)
                g = random(20,200)
                b = random(20,200)
                ellSize = 50
        if key == '-' or key == '_':
            if ellSize >= 1:
                ellSize = ellSize - scrSpeed
            else:
                r = random(20,200)
                g = random(20,200)
                b = random(20,200)
                ellSize = 50
                
