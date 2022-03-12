from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", font=("roboto", 24, "bold"), align="center")
        self.hideturtle()
    def update_score (self):
        self.clear()
        self.write(f"Score: {self.score}", font=("roboto", 24, "bold"), align="center")
    def increase_score(self):
        self.score += 1
        self.update_score()
        
    def game_over(self):
        self.clear()
        self.write(f"GAME OVER", font=("roboto", 24, "bold"), align="center")