def setup():
    size(600,400)
    frameRate(5)
    
def draw():
    for x in range(0,floor(random(10,200))):
        stroke(random(230,255),random(230,255),random(100,250))
        strokeWeight(random(1,3))
        point(random(0,601),random(0,401))

