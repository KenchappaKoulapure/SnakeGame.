from turtle import Turtle 

STARTING_POSITIONS = [[(0,0) , (-20,0) , (-40,0)]]
MOVE_DISTEANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        
       segment_1 = Turtle("square")
       segment_1.color("white")
       segment_1.penup()
       segment_1.goto(0,0)

       segment_2 = Turtle("square")
       segment_2.color("white")
       segment_2.penup()
       segment_2.goto(-20,0)   

       segment_3 = Turtle("square")
       segment_3.color("white")
       segment_3.penup()
       segment_3.goto(-40,0)

       self.segments.append(segment_1)
       self.segments.append(segment_2)
       self.segments.append(segment_3)

    def move(self):
         for seg_num in range(len(self.segments) -1 , 0 , -1):
            new_x = self.segments[seg_num - 1].xcor()

            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)

         self.head.forward(MOVE_DISTEANCE)

    
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


          
