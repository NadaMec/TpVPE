import pygame
from cube import Cube
from camera import Camera

Window_color = ('#C4EFF9')
Width, Height = 1000, 670

pygame.display.set_caption("3D Cube")
screen = pygame.display.set_mode((Width, Height))

scale_factor = 60

cube = Cube(scale_factor)
camera = Camera(scale_factor)

clock = pygame.time.Clock()

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

    # Update camera based on user input
    camera.update()

    screen.fill(Window_color)

    # Update cube state with camera information
    cube.update(camera)

    cube.draw(screen)

    pygame.display.update()
