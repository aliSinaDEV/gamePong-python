from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, cordinate):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=100/20, stretch_len=20/20)
        self.color("white")
        self.goto(x= cordinate[0], y=cordinate[1])

    def go_up(self):
        new_y = self.ycor() + 20
        x = self.xcor()
        self.penup()
        self.goto(x=x, y=new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        x = self.xcor()
        self.penup()
        self.goto(x=x, y=new_y)