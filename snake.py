from turtle import Turtle

starting_position = [(0,0),(-20,0),(-40,0)]

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:



    def __init__(self):
        #Aqui hacemos los segmentos de la serpiente y la creamos.
        self.segments = []
        self.create_snake()

        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)
          
    def add_segment(self, position):
        snake_segment = Turtle("circle")
        snake_segment.color("pink")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


      #Le daremos movimiento.  
    def move(self): 
        for seg_num in range(len(self.segments)-1,0,-1):

             new_x = self.segments[seg_num-1].xcor()
             new_y = self.segments[seg_num-1].ycor()
             self.segments[seg_num].goto(new_x, new_y)       
        self.head.forward(20)


    #Y aqui con las flechas moveremos la cabeza de la serpiente
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down (self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right (self):  
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left (self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)