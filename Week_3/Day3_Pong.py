import pygame

pygame.init()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Paddle build:
paddle_color = (255, 255, 255)
paddle_width, paddle_height = 20, 100
left_paddle_x, left_paddle_y = 50, (height - paddle_height) // 2
right_paddle_x, right_paddle_y = width - 50 - paddle_width, (height-paddle_height) // 2
paddle_speed = 1.5
background_color = (0, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < height - paddle_height:
        left_paddle_y += paddle_speed

    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < height - paddle_height:
        right_paddle_y += paddle_speed

    screen.fill(background_color)

    pygame.draw.rect(screen, paddle_color, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))

    pygame.draw.rect(screen, paddle_color, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))

    pygame.display.flip()

pygame.quit()