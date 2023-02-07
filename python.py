from turtle import Turtle

SEG_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Python:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for pos in SEG_POS:
            self.insert(pos)

    def insert(self, position):
        seg = Turtle("square")
        seg.penup()
        seg.color("white")
        seg.goto(position)
        self.segment.append(seg)

    def extend(self):
        self.insert(self.segment[-1].position())

    def move(self):
        for new_seg in range(len(self.segment) - 1, 0, -1):
            x_pos = self.segment[new_seg - 1].xcor()
            y_pos = self.segment[new_seg - 1].ycor()
            self.segment[new_seg].goto(x_pos, y_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

