
import turtle

wn = turtle.Screen()  


wn.title("mitt pong spel")
wn.bgcolor('white')
wn.setup(width=600, height =400)
wn.tracer(0)

poäng_a = 0
poäng_b = 0

vägg_1 = turtle.Turtle()
vägg_1.speed(0)
vägg_1.shape('square')
vägg_1.shapesize(stretch_wid=4, stretch_len=1)
vägg_1.color('black')
vägg_1.penup()
vägg_1.goto(-250, 0)

vägg_2 = turtle.Turtle()
vägg_2.speed(0)
vägg_2.shape('square')
vägg_2.shapesize(stretch_wid=4, stretch_len=1)
vägg_2.color('black')
vägg_2.penup()
vägg_2.goto(250, 0)

boll = turtle.Turtle()
boll.speed(0)
boll.shape('square')
boll.color('red')
boll.penup()
boll.goto(0, 0)
boll.dx = 0.1
boll.dy = 0.1

pen = turtle.Turtle()
pen.speed(0)
pen.color('black')
pen.penup()
pen.hideturtle()
pen.goto(0, 155)
pen.write('spelare 1: 0   spelare 2: 0', align='center', font=('Courier',14,'normal'))


def vägg_1_upp():
    y= vägg_1.ycor()
    y += 20
    vägg_1.sety(y)

def vägg_1_ner():
    y= vägg_1.ycor()
    y -= 20
    vägg_1.sety(y)


def vägg_2_upp():
    y= vägg_2.ycor()
    y += 20
    vägg_2.sety(y)

def vägg_2_ner():
    y= vägg_2.ycor()
    y -= 20
    vägg_2.sety(y)
    
wn.listen()
wn.onkeypress(vägg_1_upp, 'w')
wn.onkeypress(vägg_1_ner, 's')
wn.onkeypress(vägg_2_upp, 'i')
wn.onkeypress(vägg_2_ner, 'k')

while True:
    wn.update()

    boll.setx(boll.xcor() + boll.dx)
    boll.sety(boll.ycor() + boll.dy)

    if boll.ycor() > 190:
        boll.sety(190)
        boll.dy *= -1
    
    if boll.ycor() < -190:
        boll.sety(-190)
        boll.dy *= -1

    if boll.xcor() > 290:
        boll.goto(0, 0)
        boll.dx *= -1
        poäng_a += 1
        pen.clear()
        pen.write('spelare 1: {}   spelare 2: {}'.format(poäng_a,poäng_b), align='center', font=('Courier',14,'normal'))

    if boll.xcor() < -290:
        boll.goto(0, 0)
        boll.dx *= -1
        poäng_b += 1
        pen.clear()
        pen.write('spelare 1: {}   spelare 2: {}'.format(poäng_a,poäng_b), align='center', font=('Courier',14,'normal'))

    if (boll.xcor() > 240 and boll.xcor() < 250) and (boll.ycor() < vägg_2.ycor() + 50 and boll.ycor() > vägg_2.ycor() -50):
        boll.setx(240)
        boll.dx *= -1

    if (boll.xcor() < -240 and boll.xcor() > -250) and (boll.ycor() < vägg_1.ycor() + 50 and boll.ycor() > vägg_1.ycor() -50):
        boll.setx(-240)
        boll.dx *= -1