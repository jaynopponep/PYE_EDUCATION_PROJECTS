# Project 17 & 18 Combined
import pygame

pygame.init()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Hello World!")

# Build the rectangle block properties:
rect_color = (255, 0, 0)
rect_x, rect_y = 100, 100
rect_width, rect_height = 60, 40
rect_speed = 80

light_blue = (173, 216, 230)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Keyboard events for rectangle block:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect_x -= rect_speed
            if event.key == pygame.K_RIGHT:
                rect_x += rect_speed
            if event.key == pygame.K_UP:
                rect_y -= rect_speed
            if event.key == pygame.K_DOWN:
                rect_y += rect_speed
    screen.fill(light_blue)

    # Draw rectangle here:
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))

    pygame.display.flip()

pygame.quit()