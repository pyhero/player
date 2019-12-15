import turtle

turtle.bgcolor('black')


def rainbow():
    pen = turtle.Pen()
    pen.pensize('1')
    sides = 7
    colors = ['red', 'pink', 'yellow', 'green', 'cyan', 'blue', 'purple']
    x = 0
    while True:
        pen.pencolor(colors[x % sides])
        pen.forward(x * 3 / sides + x)
        pen.left(360 / sides + 1)
        pen.width(x * sides / 200)

        x += 2


def loop():
    pen = turtle.Pen()
    pen.color('green')
    pen.pensize('2')

    while True:
        pen.shape('turtle')
        pen.circle(100, 360)
        pen.left(30)


def pyramid():
    pen = turtle.Pen()
    pen.color('green')
    pen.pensize(2)

    x = 1
    while True:
        pen.left(90)
        pen.fd(x * 2)

        x += 2


# rainbow()
# loop()
pyramid()