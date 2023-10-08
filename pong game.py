import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
BALL_SPEED = [7, 7]
PADDLE_SPEED = 10
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

player_paddle = pygame.Rect(50, HEIGHT // 2 - 50, 10, 100)
opponent_paddle = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 50, 10, 100)
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)

ball_direction = [random.choice((1, -1)), random.choice((1, -1))]

player_score = 0
opponent_score = 0

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player_paddle.top > 0:
        player_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player_paddle.bottom < HEIGHT:
        player_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and opponent_paddle.top > 0:
        opponent_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and opponent_paddle.bottom < HEIGHT:
        opponent_paddle.y += PADDLE_SPEED

    ball.x += BALL_SPEED[0] * ball_direction[0]
    ball.y += BALL_SPEED[1] * ball_direction[1]

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_direction[1] *= -1

    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_direction[0] *= -1

    if ball.left <= 0:
        opponent_score += 1
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_direction[0] *= -1

    if ball.right >= WIDTH:
        player_score += 1
        ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        ball_direction[0] *= -1

    window.fill(BLACK)

    pygame.draw.rect(window, WHITE, player_paddle)
    pygame.draw.rect(window, WHITE, opponent_paddle)
    pygame.draw.ellipse(window, WHITE, ball)

    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    window.blit(player_text, (50, 50))
    window.blit(opponent_text, (WIDTH - 70, 50))

    pygame.display.flip()

     clock.tick(60)

pygame.quit()
