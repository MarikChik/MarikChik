colorful_r = 0
colorful_g = 0
colorful_b = 0



def setup():
    global mode
    global colorful_r
    colorful_r = 0
    global colorful_g
    colorful_g = 0
    global colorful_b
    colorful_b = 0
    size(1000,500)
    mode = "Red"
def draw():
    global colorful_r
    global colorful_g
    global colorful_b
    global mode
    background (75) 
    line(1,155,1000,155)
    fill (colorful_r,colorful_g,colorful_b)
    ellipse(250,155,30,30)
    ellipse(400,165,30,30)
    ellipse(650,155,30,30)
    ellipse(850,165,30,30)
    if mode == "Red":
        colorful_g = 0
        colorful_b = 0
        colorful_r += 3
    if mode == "Green":
        colorful_r = 0
        colorful_b = 0
        colorful_g += 3
    if mode == "Blue":
        colorful_r = 0
        colorful_g = 0
        colorful_b += 3
        
    
    colorful_r = colorful_r + 0
    colorful_g = colorful_g + 0
    colorful_b = colorful_b + 0
    if colorful_r >= 255:
          mode = "Green"
    if colorful_g >= 255:
          mode = "Blue"
    if colorful_b >= 255:
          mode = "Red"
