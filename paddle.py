from turtle import Turtle

WIDTH = 800
HEIGHT = 600


class Paddle(Turtle):

    def __init__(self, xpos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("White")
        self.goto(xpos, 0)


    def move_up(self):
        new_y = self.ycor() + 20
        if new_y < (HEIGHT // 2) - 50:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if new_y > (-HEIGHT // 2) + 50:
            self.goto(self.xcor(), new_y)




