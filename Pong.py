import turtle

wn=turtle.Screen()
wn.title("Pong by Owen Doucet")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score1 = 0
score2 = 0

#Paddle1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1 )
paddle1.penup()
paddle1.goto(-350, 0)

#Paddle2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1 )
paddle2.penup()
paddle2.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1.5
ball.dy = 1.5

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B 0" , align="center", font=("Courier", 24, "normal"))

#Functions
def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y += -20
    paddle1.sety(y)
    
def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y += -20
    paddle2.sety(y)
    
#keybindings
wn.listen()
wn.onkeypress(paddle1_up, "w")
wn.listen()
wn.onkeypress(paddle1_down, "s")

wn.listen()
wn.onkeypress(paddle2_up, "Up")
wn.listen()
wn.onkeypress(paddle2_down, "Down")

while True:
  wn.update()

  #movetheball
  ball.setx(ball.xcor() + ball.dx)
  ball.sety(ball.ycor() + ball.dy)

    #border checking
  if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
  if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
  if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

  if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        
    #Paddle and ball collision
  if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() -50):
         ball.setx(340)
         ball.dx *= -1
        
  if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() -50):
         ball.setx(-340)
         ball.dx *= -1
