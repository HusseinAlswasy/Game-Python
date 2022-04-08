                              #python Game Hussein
#imported turtel module
import turtle

wind = turtle.Screen()                  ##You see game in wind
wind.title("Game PING PONG Hussein")            ##title
wind.bgcolor("white")                   ##color background
wind.setup(width=800,height=600)        ##width - heigh
wind.tracer(0)                          ##Dont Update

                         #madrab 1
madrab1 = turtle.Turtle()               ##to draw inimation
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid=5,stretch_len=0.5)
madrab1.penup()                         ##to be dont draw lines
madrab1.goto(-350,0)                    ##direction y x

                         #madrab 2
madrab2 = turtle.Turtle()               ##to draw inimation
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("black")
madrab2.shapesize(stretch_wid=5,stretch_len=0.5)
madrab2.penup()                         ##to be dont draw lines
madrab2.goto(350,0)

                           #ball
ball = turtle.Turtle()                ##to draw inimation
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()                          ##to be dont draw lines
ball.goto(0,0)                        ##ball start center
ball.dx =0.5                          ##fast ball in screen x
ball.dy =0.5                          ##fast ball in screen y

#score
score1 =0
score2 =0
score =turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()                    ##علشان اشوف مكان سكوور
score.goto(0 , 260)
score.write("Player 1: 0 *** Player 2: 0",align="center",font=("bold",24,"bold"))

#functions
def madrab1_up():
    y =madrab1.ycor()                   ##to control madrab1 up
    y = y + 20                          ##20 pixel in up
    madrab1.sety(y)                     ##y old in y new

def madrab1_down():
    y =madrab1.ycor()                   ##to control madrab1 down
    y = y - 20                          ##20 pixel in down
    madrab1.sety(y)                     ##y old in y new


def madrab2_up():
    y =madrab2.ycor()                   ##to control madrab1 up
    y = y + 20                          ##20 pixel in up
    madrab2.sety(y)                     ##y old in y new

def madrab2_down():
    y =madrab2.ycor()                   ##to control madrab1 down
    y = y - 20                          ##20 pixel in down
    madrab2.sety(y)                     ##y old in y new


#keyboard dirction
wind.listen()                           ##redy to listen keyboard
wind.onkeypress(madrab1_up,"w")         ##on press on w move up
wind.onkeypress(madrab1_down,"s")       ##on press on w move down

wind.onkeypress(madrab2_up,"Up")        ##on press on w move up
wind.onkeypress(madrab2_down,"Down")    ##on press on w move down


while True:
    wind.update()                       ##in all once screen i=on screen update

    ##move ball
    ball.setx(ball.xcor()+ball.dx)      ##مكان الكرة حالي ونزود علية 2.5
    ball.sety(ball.ycor()+ball.dy)      ##مكان الكرة حالي ونزود علية 2.5

    #border revers       top 300  , bottom -300   ball 20pxel
    if ball.ycor() > 290:               # up - down
        ball.sety(290)
        ball.dy *= -1                   #بدل ما بذيد فوق 2.5 انزل تحت

    if ball.ycor() <- 290:
        ball.sety(-290)
        ball.dy *= -1                   #بدل ما بذيد فوق 2.5 انزل تحت

    if ball.xcor() >390:                #rigth
        ball.goto(0,0)                  #center ball
        ball.dx *= -1                   #revers dirction
        score1 +=1
        score.clear()
        score.write("Player 1: {} *** Player 2: {}".format(score1,score2),align="center",font=("bold",24,"bold")),


    if ball.xcor() <- 390:              #left
        ball.goto(0,0)                  #center ball
        ball.dx *= -1                   #revers dirction
        score2 +=1
        score.clear()
        score.write("Player 1: {} *** Player 2: {}".format(score1,score2),align="center",font=("bold",24,"bold"))

    #tsadom  madrab in ball

    if (ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < madrab2.ycor()+40 and ball.ycor() > madrab2.ycor()-40):
        ball.setx(340)
        ball.dx *=-1

    if (ball.xcor() <-340 and ball.xcor() >-350 and ball.ycor() < madrab1.ycor() + 40 and ball.ycor() > madrab1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
