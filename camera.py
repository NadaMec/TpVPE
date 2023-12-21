import pygame
from math import cos, sin

class Camera:
    def __init__(self, scale_factor=60):
        self.position = [300, 300, 0]
        self.rotation = [0, 0, 0]
        self.move_speed = 5
        self.rotation_speed = 0.01
        self.distance_to_cube = 50
        self.scale_factor = scale_factor

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.move_Up()
        if keys[pygame.K_DOWN]:
            self.move_Down()
        if keys[pygame.K_LEFT]:
            self.move_left()
        if keys[pygame.K_RIGHT]:
            self.move_right()

        if keys[pygame.K_z]:
            self.move_closer()
        if keys[pygame.K_x]:
            self.move_away()

        mouse_dx, mouse_dy = pygame.mouse.get_rel()
        self.rotate(mouse_dx, mouse_dy)

    def move_Up(self):
        self.position[0] += self.move_speed * sin(self.rotation[0])
        self.position[1] -= self.move_speed * cos(self.rotation[0])

    def move_Down(self):
        self.position[0] -= self.move_speed * sin(self.rotation[0])
        self.position[1] += self.move_speed * cos(self.rotation[0])

    def move_left(self):
        self.position[0] -= self.move_speed * cos(self.rotation[0])
        self.position[1] -= self.move_speed * sin(self.rotation[0])

    def move_right(self):
        self.position[0] += self.move_speed * cos(self.rotation[0])
        self.position[1] += self.move_speed * sin(self.rotation[0])

    def move_closer(self):
        self.scale_factor += 1

    def move_away(self):
        self.scale_factor -= 1


    def increase_scale_factor(self):
        self.scale_factor += 1

    def decrease_scale_factor(self):
        self.scale_factor -= 1

    def rotate(self, mouse_dx, mouse_dy):
        self.rotation[0] += mouse_dx * self.rotation_speed
        self.rotation[1] += mouse_dy * self.rotation_speed

        self.rotation[1] = max(-1.5, min(1.5, self.rotation[1]))
