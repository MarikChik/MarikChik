ellipse_x = 100

def setup():
    global mode
    size(1000,500)
    mode = "right"
def draw():
    global ellipse_x
    global mode
    background (5) 
    ellipse(ellipse_x ,250 ,200,150)
    if mode == "right":
        ellipse_x += 3
    if mode == "left":
        ellipse_x -= 3

    if ellipse_x >= 900:
        mode = "left"
    if ellipse_x <= 100:
        mode = "right"
