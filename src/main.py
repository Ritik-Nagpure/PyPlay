import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Game Window Size
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake & Food Size
snake_size = 10
snake_speed = 15

# Clock
clock = pygame.time.Clock()


# Snake Game Function
def game_loop():
    game_over = False
    game_close = False

    x, y = WIDTH // 2, HEIGHT // 2
    x_change, y_change = 0, 0

    snake_body = []
    length = 1

    # Food position
    food_x = round(random.randrange(0, WIDTH - snake_size) / 10) * 10
    food_y = round(random.randrange(0, HEIGHT - snake_size) / 10) * 10

    while not game_over:
        while game_close:
            win.fill(BLACK)
            font = pygame.font.SysFont("comicsans", 35)
            msg = font.render("Game Over! \n Press Q-Quit or R-Retry", True, RED)
            win.blit(msg, [WIDTH / 6, HEIGHT / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_size
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_size
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_size
                    x_change = 0

        # Check for boundaries
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_change
        y += y_change

        win.fill(WHITE)
        pygame.draw.rect(win, RED, [food_x, food_y, snake_size, snake_size])

        snake_body.append([x, y])
        if len(snake_body) > length:
            del snake_body[0]

        for block in snake_body[:-1]:
            if block == [x, y]:
                game_close = True

        for segment in snake_body:
            pygame.draw.rect(win, GREEN, [segment[0], segment[1], snake_size, snake_size])

        pygame.display.update()

        # Check if Snake Eats Food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - snake_size) / 10) * 10
            food_y = round(random.randrange(0, HEIGHT - snake_size) / 10) * 10
            length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


# Run the Game
game_loop()

