UpDown = 250
LeftRight = 300
r = 30
g = 250
b = 20


def setup():
    size(700,600)

    
def draw():
    global UpDown,LeftRight,r,g,b
    background(255)
    fill(r,g,b)
    rect(LeftRight,UpDown,100,100)
    if keyPressed:
        if key == 'ц' or key == 'Ц' or key == 'w' or key == 'W':
            if UpDown >= 10:
                UpDown = UpDown - 2
            else:
                 UpDown = 250
                 r = random(20,200)
                 g = random(20,200)
                 b = random(20,200)
        if key == 'ы' or key == 'Ы' or key == 's' or key == 'S':
            if UpDown <= 500:
                UpDown = UpDown + 2
            else:
                 UpDown = 250
                 r = random(20,200)
                 g = random(20,200)
                 b = random(20,200)
        if key == 'a' or key == 'A' or key == 'ф' or key == 'Ф':
            if LeftRight >= 10:
                LeftRight = LeftRight - 2
            else:
                 LeftRight = 250
                 r = random(20,200)
                 g = random(20,200)
                 b = random(20,200)
        if key == 'D' or key == 'd' or key == 'В' or key == 'в':
            if LeftRight <= 600:
                LeftRight = LeftRight + 2
            else:
                 LeftRight = 300
                 r = random(20,200)
                 g = random(20,200)
                 b = random(20,200)
        
