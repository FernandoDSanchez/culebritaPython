from turtle import Turtle
#construir cuerpo serpiente  

STARTING_POSITION = [(0,0),(0,0),(0,0)] 
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    
    #Constructor
    def __init__(self):
        #almaceno los segmentos de la serpientes
        self.segments = []
        # Metodo que crea la serpiente
        self.create_snake()
        # Atributo cabeza
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in STARTING_POSITION: 
            self.snake_segment = Turtle("square") 
            self.snake_segment.color("white") 
            self.snake_segment.penup() 
            self.snake_segment.goto(position) 
            self.segments.append(self.snake_segment) 
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(20)
        
    def add(self):
        self.create_snake()
        print(self.segments)
        self.move()
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)   
            
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
        

#creacion del tablero del juego 




#almaceno los segmentos de la serpiente 





#animación serpiente  
 

