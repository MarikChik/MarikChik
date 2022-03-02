ellipseSize = 1

def setup():
    global mode
    size(1000,500)
    mode = "Bolshitsya"
def draw():
    global ellipseSize 
    global mode
    background (5) 
    ellipse(500,250,ellipseSize,ellipseSize)
    if mode == "Bolshitsya":
        ellipseSize += 3
    if mode == "Menshitsya":
        ellipseSize -= 3

    if ellipseSize <= 50 :
        mode = "Bolshitsya"
    if ellipseSize >= 500:
        mode = "Menshitsya"
