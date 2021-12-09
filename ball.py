from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("White")
        self.x_delta = 3
        self.y_delta = 3

    def move(self):
        self.setpos(self.xcor() + self.x_delta, self.ycor() + self.y_delta)

    def bounce_y(self):
        self.y_delta *= -1

    def bounce_x(self):
        self.x_delta *= -1

    def reset_position(self):
            self.goto(0, 0)
            self.x_delta *= -1
            self.y_delta *= -1
