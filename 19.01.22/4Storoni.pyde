x = 1
n = 1
b = 1
c = 1

def setup():
    size(600,600)
    
def draw():
    global x
    global n
    global b
    global c

    translate(299,299)
    fill(random(30,80))
    background(40,10,60)
    ellipse(x,x,40,40)
    ellipse(n,n,40,40)
    ellipse(b,c,40,40)
    ellipse(c,b,40,40)
    x = x + 1
    n = n - 1
    b = b + 1
    c = c - 1
    
