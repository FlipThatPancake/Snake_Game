from Screen import Background
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
import time

screen = Background()
snake = Snake(screen)
food = Food()
score = Scoreboard()
snake.start_listening()

game_is_on = True

while game_is_on:
    screen.screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.snake_head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.current_score += 1
        score.update_scoreboard()

    # Detect collision with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        score.reset_scoreboard()
        snake.reset_func()
        print('wall')


    # Detect if head collides with tail
    for segment in snake.the_snake[1:]:
        if snake.snake_head.distance(segment) < 10:
            score.reset_scoreboard()
            snake.reset_func()



screen.screen.exitonclick()