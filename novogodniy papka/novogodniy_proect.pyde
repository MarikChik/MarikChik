
def setup():
    size(600,600)
    colorMode(HSB,360,100,100)
    frameRate(2)


def draw():
    background(500)
    push()
    noStroke() # убираем обводку
    fill(0,0,100)
    rect(1,430,700,600)
    fill(41,80,50) #зелёный цвет в HSB
    translate(300,300) # координаты середины основания треугольника
    rect(-25,110,50,30)
    fill(120,100,50) #зелёный цвет в HSB
    triangle(60,30, -60,30  , 0, -60) # можно все 60 заменить на другое число
    triangle(70,70, -70,70  , 0, -10)
    triangle(90,120, -90,120  , 0, 40)
    pop()
    for step in range(floor(random(5,60))):
            strokeWeight(random(1,20))
            stroke(random(1,1),0,1000)
            point(random(0,width),random(0,height))


