cent = 200
X = -120
Y = 30
X1 = -200
Y1 = 130

def setup():
    size(600,400)
    frameRate(10)
    
def draw():
    global cent,X,Y,X1,Y1
    background(127,255,212)
    
    push()
    X = X + 6
    fill(255,222,173)
    ellipse(X,Y,200,50)
    if X >= 700:
        X = -120
        Y = random(30,250)
        
    X1 = X1 + 4
    fill(255,222,173)
    ellipse(X1,Y1,150,60)
    if X1 >= 750:
        X1 = -200
        Y1= random(50,260)
    pop()
    
    
    fill(60,179,113)
    ellipse(300,400,900,100)
    fill(46,139,87)
    rect(280,200,25,1000)
    ellipse(320,320,50,30)
    
    push()
    
    fill(255,239,213)
    translate(300,200)
    rotate(radians(cent))
    for step in range(12):
        ellipse(50,50,50,50)
        rotate(radians(30))
   
    pop()
   
    fill(255,165,0)
    ellipse(300,200,100,100)

    
    cent = cent + 1
