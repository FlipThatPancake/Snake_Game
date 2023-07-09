from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("data.txt") as data_file:
            self.high_score = int(data_file.read())
        self.penup()
        self.goto(0, 250)
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.current_score} High Score: {self.high_score}', move=False, align='center', font=('Arial', 16, 'normal'))

    def reset_scoreboard(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
        self.current_score = 0
        self.update_scoreboard()
        self.save_high_score()

    def save_high_score(self):
        with open("data.txt", mode='w') as data_file:
            data_file.write(str(self.high_score))