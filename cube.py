import numpy as np
import pygame
from math import cos, sin

class Cube:
    def __init__(self, scale_factor, width=0, height=0):
        self.scale_factor = scale_factor
        self.width = width
        self.height = height
        self.vertices_cube = np.array([
            [-1, -1, 1],
            [1, -1, 1],
            [1, 1, 1],
            [-1, 1, 1],
            [-1, -1, -1],
            [1, -1, -1],
            [1, 1, -1],
            [-1, 1, -1]
        ])

        self.vertices_cube2 = self.vertices_cube + np.array([2, 0, 0])
        self.vertices_cube3 = self.vertices_cube2 + np.array([2, 0, 0])
        self.vertices_cube4 = self.vertices_cube + np.array([0, 0, 2])
        self.vertices_cube5 = self.vertices_cube2 + np.array([0, 0, 2])
        self.vertices_cube6 = self.vertices_cube3 + np.array([0, 0, 2])
        self.vertices_cube7 = self.vertices_cube3 + np.array([2, 0, 0])
        self.vertices_cube8 = self.vertices_cube7 + np.array([0, 0, 2])
        self.vertices_cube9 = self.vertices_cube7 + np.array([2, 0, 0])
        self.vertices_cube10 = self.vertices_cube9 + np.array([0, 0, 2])
        self.vertices_cube11 = self.vertices_cube + np.array([0, -2, 0])
        self.vertices_cube12 = self.vertices_cube4 + np.array([0, 0, 2])
        self.vertices_cube13 = self.vertices_cube5 + np.array([0, 0, 2])
        self.vertices_cube14 = self.vertices_cube6 + np.array([0, 0, 2])
        self.vertices_cube15 = self.vertices_cube8 + np.array([0, 0, 2])
        self.vertices_cube16 = self.vertices_cube10 + np.array([0, 0, 2])








        self.projection_matrix = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])
        self.projected_vertices = [np.zeros(3) for _ in range(len(self.vertices_cube))]
        self.projected_vertices2 = [np.zeros(3) for _ in range(len(self.vertices_cube2))]
        self.projected_vertices3 = [np.zeros(3) for _ in range(len(self.vertices_cube3))]
        self.projected_vertices4 = [np.zeros(3) for _ in range(len(self.vertices_cube4))]
        self.projected_vertices5 = [np.zeros(3) for _ in range(len(self.vertices_cube5))]
        self.projected_vertices6 = [np.zeros(3) for _ in range(len(self.vertices_cube6))]
        self.projected_vertices7 = [np.zeros(3) for _ in range(len(self.vertices_cube7))]
        self.projected_vertices8 = [np.zeros(3) for _ in range(len(self.vertices_cube8))]
        self.projected_vertices9 = [np.zeros(3) for _ in range(len(self.vertices_cube9))]
        self.projected_vertices10 = [np.zeros(3) for _ in range(len(self.vertices_cube10))]
        self.projected_vertices11 = [np.zeros(3) for _ in range(len(self.vertices_cube11))]
        self.projected_vertices12 = [np.zeros(3) for _ in range(len(self.vertices_cube12))]
        self.projected_vertices13 = [np.zeros(3) for _ in range(len(self.vertices_cube13))]
        self.projected_vertices14 = [np.zeros(3) for _ in range(len(self.vertices_cube14))]
        self.projected_vertices15 = [np.zeros(3) for _ in range(len(self.vertices_cube15))]
        self.projected_vertices16 = [np.zeros(3) for _ in range(len(self.vertices_cube16))]






        self.rotation_angle_x = 0.0005
        self.rotation_angle_y = 0.0005

    def update(self, camera):
        self.rotation_angle_x = camera.rotation[0]
        self.rotation_angle_y = camera.rotation[1]
        self.transform_vertices(camera.position)

    def transform_vertices(self, camera_position):
        rotation_matrix_z = np.array([
            [cos(self.rotation_angle_x), -sin(self.rotation_angle_x), 0],
            [sin(self.rotation_angle_x), cos(self.rotation_angle_x), 0],
            [0, 0, 1],
        ])
        rotation_matrix_y = np.array([
            [cos(self.rotation_angle_y), 0, sin(self.rotation_angle_y)],
            [0, 1, 0],
            [-sin(self.rotation_angle_y), 0, cos(self.rotation_angle_y)],
        ])
        rotation_matrix_x = np.array([
            [1, 0, 0],
            [0, cos(self.rotation_angle_x), -sin(self.rotation_angle_x)],
            [0, sin(self.rotation_angle_x), cos(self.rotation_angle_x)],
        ])

        for i, vertex in enumerate(self.vertices_cube):
            rotated_vertex = np.dot(rotation_matrix_z, vertex.reshape((3, 1)))
            rotated_vertex = np.dot(rotation_matrix_y, rotated_vertex)
            rotated_vertex = np.dot(rotation_matrix_x, rotated_vertex)
            projected_vertex = np.dot(self.projection_matrix, rotated_vertex)

            x = int(projected_vertex[0, 0] * self.scale_factor)
            y = int(projected_vertex[1, 0] * self.scale_factor)
            z = int(projected_vertex[2, 0] * self.scale_factor)

            # Update cube position based on camera position
            self.projected_vertices[i] = [x + camera_position[0], y + camera_position[1], z + camera_position[2]]

        for i, vertex in enumerate(self.vertices_cube2):
            rotated_vertex = np.dot(rotation_matrix_z, vertex.reshape((3, 1)))
            rotated_vertex = np.dot(rotation_matrix_y, rotated_vertex)
            rotated_vertex = np.dot(rotation_matrix_x, rotated_vertex)
            projected_vertex = np.dot(self.projection_matrix, rotated_vertex)

            x = int(projected_vertex[0, 0] * self.scale_factor)
            y = int(projected_vertex[1, 0] * self.scale_factor)
            z = int(projected_vertex[2, 0] * self.scale_factor)

            # Update cube position based on camera position
            self.projected_vertices2[i] = [x + camera_position[0], y + camera_position[1], z + camera_position[2]]

        for i, vertex in enumerate(self.vertices_cube3):
            rotated_vertex = np.dot(rotation_matrix_z, vertex.reshape((3, 1)))
            rotated_vertex = np.dot(rotation_matrix_y, rotated_vertex)
            rotated_vertex = np.dot(rotation_matrix_x, rotated_vertex)
            projected_vertex = np.dot(self.projection_matrix, rotated_vertex)

            x = int(projected_vertex[0, 0] * self.scale_factor)
            y = int(projected_vertex[1, 0] * self.scale_factor)
            z = int(projected_vertex[2, 0] * self.scale_factor)

            # Update cube position based on camera position
            self.projected_vertices3[i] = [x + camera_position[0], y + camera_position[1], z + camera_position[2]]


        for i, vertex in enumerate(self.vertices_cube4):
            rotated_vertex = np.dot(rotation_matrix_z, vertex.reshape((3, 1)))
            rotated_vertex = np.dot(rotation_matrix_y, rotated_vertex)
            rotated_vertex = np.dot(rotation_matrix_x, rotated_vertex)
            projected_vertex = np.dot(self.projection_matrix, rotated_vertex)

            x = int(projected_vertex[0, 0] * self.scale_factor)
            y = int(projected_vertex[1, 0] * self.scale_factor)
            z = int(projected_vertex[2, 0] * self.scale_factor)

            # Update cube position based on camera position
            self.projected_vertices4[i] = [x + camera_position[0], y + camera_position[1], z + camera_position[2]]

        for i, vertex in enumerate(self.vertices_cube5):
            rotated_vertex = np.dot(rotation_matrix_z, vertex.reshape((3, 1)))
            rotated_vertex = np.dot(rotation_matrix_y, rotated_vertex)
            rotated_vertex = np.dot(rotation_matrix_x, rotated_vertex)
            projected_vertex = np.dot(self.projection_matrix, rotated_vertex)

            x = int(projected_vertex[0, 0] * self.scale_factor)
            y = int(projected_vertex[1, 0] * self.scale_factor)
            z = int(projected_vertex[2, 0] * self.scale_factor)

            # Update cube position based on camera position
            self.projected_vertices5[i] = [x + camera_position[0], y + camera_position[1], z + camera_position[2]]


        for i, vertex in enumerate(self.vertices_cube6):
            rotated_vertex = np.dot(rotation_matrix_z, vertex.reshape((3, 1)))
            rotated_vertex = np.dot(rotation_matrix_y, rotated_vertex)
            rotated_vertex = np.dot(rotation_matrix_x, rotated_vertex)
            projected_vertex = np.dot(self.projection_matrix, rotated_vertex)

            x = int(projected_vertex[0, 0] * self.scale_factor)
            y = int(projected_vertex[1, 0] * self.scale_factor)
            z = int(projected_vertex[2, 0] * self.scale_factor)

            # Update cube position based on camera position
            self.projected_vertices6[i] = [x + camera_position[0], y + camera_position[1], z + camera_position[2]]

        for i, vertex in enumerate(self.vertices_cube7):
            rotated_vertex = np.dot(rotation_matrix_z, vertex.reshape((3, 1)))
            rotated_vertex = np.dot(rotation_matrix_y, rotated_vertex)
            rotated_vertex = np.dot(rotation_matrix_x, rotated_vertex)
            projected_vertex = np.dot(self.projection_matrix, rotated_vertex)

            x = int(projected_vertex[0, 0] * self.scale_factor)
            y = int(projected_vertex[1, 0] * self.scale_factor)
            z = int(projected_vertex[2, 0] * self.scale_factor)

            # Update cube position based on camera position
            self.projected_vertices7[i] = [x + camera_position[0], y + camera_position[1], z + camera_position[2]]


        for i, vertex in enumerate(self.vertices_cube8):
            rotated_vertex = np.dot(rotation_matrix_z, vertex.reshape((3, 1)))
            rotated_vertex = np.dot(rotation_matrix_y, rotated_vertex)
            rotated_vertex = np.dot(rotation_matrix_x, rotated_vertex)
            projected_vertex = np.dot(self.projection_matrix, rotated_vertex)

            x = int(projected_vertex[0, 0] * self.scale_factor)
            y = int(projected_vertex[1, 0] * self.scale_factor)
            z = int(projected_vertex[2, 0] * self.scale_factor)

            # Update cube position based on camera position
            self.projected_vertices8[i] = [x + camera_position[0], y + camera_position[1], z + camera_position[2]]

        for i, vertex in enumerate(self.vertices_cube9):
            rotated_vertex = np.dot(rotation_matrix_z, vertex.reshape((3, 1)))
            rotated_vertex = np.dot(rotation_matrix_y, rotated_vertex)
            rotated_vertex = np.dot(rotation_matrix_x, rotated_vertex)
            projected_vertex = np.dot(self.projection_matrix, rotated_vertex)

            x = int(projected_vertex[0, 0] * self.scale_factor)
            y = int(projected_vertex[1, 0] * self.scale_factor)
            z = int(projected_vertex[2, 0] * self.scale_factor)

            # Update cube position based on camera position
            self.projected_vertices9[i] = [x + camera_position[0], y + camera_position[1], z + camera_position[2]]

        for i, vertex in enumerate(self.vertices_cube10):
            rotated_vertex = np.dot(rotation_matrix_z, vertex.reshape((3, 1)))
            rotated_vertex = np.dot(rotation_matrix_y, rotated_vertex)
            rotated_vertex = np.dot(rotation_matrix_x, rotated_vertex)
            projected_vertex = np.dot(self.projection_matrix, rotated_vertex)

            x = int(projected_vertex[0, 0] * self.scale_factor)
            y = int(projected_vertex[1, 0] * self.scale_factor)
            z = int(projected_vertex[2, 0] * self.scale_factor)

            # Update cube position based on camera position
            self.projected_vertices10[i] = [x + camera_position[0], y + camera_position[1], z + camera_position[2]]

        for i, vertex in enumerate(self.vertices_cube11):
            rotated_vertex = np.dot(rotation_matrix_z, vertex.reshape((3, 1)))
            rotated_vertex = np.dot(rotation_matrix_y, rotated_vertex)
            rotated_vertex = np.dot(rotation_matrix_x, rotated_vertex)
            projected_vertex = np.dot(self.projection_matrix, rotated_vertex)

            x = int(projected_vertex[0, 0] * self.scale_factor)
            y = int(projected_vertex[1, 0] * self.scale_factor)
            z = int(projected_vertex[2, 0] * self.scale_factor)

            # Update cube position based on camera position
            self.projected_vertices11[i] = [x + camera_position[0], y + camera_position[1], z + camera_position[2]]

        for i, vertex in enumerate(self.vertices_cube12):
            rotated_vertex = np.dot(rotation_matrix_z, vertex.reshape((3, 1)))
            rotated_vertex = np.dot(rotation_matrix_y, rotated_vertex)
            rotated_vertex = np.dot(rotation_matrix_x, rotated_vertex)
            projected_vertex = np.dot(self.projection_matrix, rotated_vertex)

            x = int(projected_vertex[0, 0] * self.scale_factor)
            y = int(projected_vertex[1, 0] * self.scale_factor)
            z = int(projected_vertex[2, 0] * self.scale_factor)

            # Update cube position based on camera position
            self.projected_vertices12[i] = [x + camera_position[0], y + camera_position[1], z + camera_position[2]]

        for i, vertex in enumerate(self.vertices_cube13):
            rotated_vertex = np.dot(rotation_matrix_z, vertex.reshape((3, 1)))
            rotated_vertex = np.dot(rotation_matrix_y, rotated_vertex)
            rotated_vertex = np.dot(rotation_matrix_x, rotated_vertex)
            projected_vertex = np.dot(self.projection_matrix, rotated_vertex)

            x = int(projected_vertex[0, 0] * self.scale_factor)
            y = int(projected_vertex[1, 0] * self.scale_factor)
            z = int(projected_vertex[2, 0] * self.scale_factor)

            # Update cube position based on camera position
            self.projected_vertices13[i] = [x + camera_position[0], y + camera_position[1], z + camera_position[2]]

        for i, vertex in enumerate(self.vertices_cube14):
            rotated_vertex = np.dot(rotation_matrix_z, vertex.reshape((3, 1)))
            rotated_vertex = np.dot(rotation_matrix_y, rotated_vertex)
            rotated_vertex = np.dot(rotation_matrix_x, rotated_vertex)
            projected_vertex = np.dot(self.projection_matrix, rotated_vertex)

            x = int(projected_vertex[0, 0] * self.scale_factor)
            y = int(projected_vertex[1, 0] * self.scale_factor)
            z = int(projected_vertex[2, 0] * self.scale_factor)

            # Update cube position based on camera position
            self.projected_vertices14[i] = [x + camera_position[0], y + camera_position[1], z + camera_position[2]]

        for i, vertex in enumerate(self.vertices_cube15):
            rotated_vertex = np.dot(rotation_matrix_z, vertex.reshape((3, 1)))
            rotated_vertex = np.dot(rotation_matrix_y, rotated_vertex)
            rotated_vertex = np.dot(rotation_matrix_x, rotated_vertex)
            projected_vertex = np.dot(self.projection_matrix, rotated_vertex)

            x = int(projected_vertex[0, 0] * self.scale_factor)
            y = int(projected_vertex[1, 0] * self.scale_factor)
            z = int(projected_vertex[2, 0] * self.scale_factor)

            # Update cube position based on camera position
            self.projected_vertices15[i] = [x + camera_position[0], y + camera_position[1], z + camera_position[2]]

        for i, vertex in enumerate(self.vertices_cube16):
            rotated_vertex = np.dot(rotation_matrix_z, vertex.reshape((3, 1)))
            rotated_vertex = np.dot(rotation_matrix_y, rotated_vertex)
            rotated_vertex = np.dot(rotation_matrix_x, rotated_vertex)
            projected_vertex = np.dot(self.projection_matrix, rotated_vertex)

            x = int(projected_vertex[0, 0] * self.scale_factor)
            y = int(projected_vertex[1, 0] * self.scale_factor)
            z = int(projected_vertex[2, 0] * self.scale_factor)

            # Update cube position based on camera position
            self.projected_vertices16[i] = [x + camera_position[0], y + camera_position[1], z + camera_position[2]]


    def draw(self, screen):
        from Texture import draw_texture
        textures = {
            'front': pygame.image.load('p.png'),
            'back': pygame.image.load('p.png'),
            'top': pygame.image.load('p.png'),
            'bottom': pygame.image.load('p.png'),
            'left': pygame.image.load('p.png'),
            'right': pygame.image.load('p.png')

        }
        textures2 = {
            'front': pygame.image.load('gravel.png'),
            'back': pygame.image.load('gravel.png'),
            'top': pygame.image.load('gravel.png'),
            'bottom': pygame.image.load('gravel.png'),
            'left': pygame.image.load('gravel.png'),
            'right': pygame.image.load('gravel.png')
        }

        draw_texture(screen, [self.projected_vertices[i] for i in [0, 1, 2, 3]], textures['front'])
        draw_texture(screen, [self.projected_vertices[i] for i in [4, 5, 6, 7]], textures['back'])
        draw_texture(screen, [self.projected_vertices[i] for i in [0, 1, 5, 4]], textures['top'])
        draw_texture(screen, [self.projected_vertices[i] for i in [3, 2, 6, 7]], textures['bottom'])
        draw_texture(screen, [self.projected_vertices[i] for i in [0, 3, 7, 4]], textures['left'])
        draw_texture(screen, [self.projected_vertices[i] for i in [1, 2, 6, 5]], textures['right'])

        draw_texture(screen, [self.projected_vertices2[i] for i in [0, 1, 2, 3]], textures['front'])
        draw_texture(screen, [self.projected_vertices2[i] for i in [4, 5, 6, 7]], textures['back'])
        draw_texture(screen, [self.projected_vertices2[i] for i in [0, 1, 5, 4]], textures['top'])
        draw_texture(screen, [self.projected_vertices2[i] for i in [3, 2, 6, 7]], textures['bottom'])
        draw_texture(screen, [self.projected_vertices2[i] for i in [0, 3, 7, 4]], textures['left'])
        draw_texture(screen, [self.projected_vertices2[i] for i in [1, 2, 6, 5]], textures['right'])

        draw_texture(screen, [self.projected_vertices3[i] for i in [0, 1, 2, 3]], textures['front'])
        draw_texture(screen, [self.projected_vertices3[i] for i in [4, 5, 6, 7]], textures['back'])
        draw_texture(screen, [self.projected_vertices3[i] for i in [0, 1, 5, 4]], textures['top'])
        draw_texture(screen, [self.projected_vertices3[i] for i in [3, 2, 6, 7]], textures['bottom'])
        draw_texture(screen, [self.projected_vertices3[i] for i in [0, 3, 7, 4]], textures['left'])
        draw_texture(screen, [self.projected_vertices3[i] for i in [1, 2, 6, 5]], textures['right'])

        draw_texture(screen, [self.projected_vertices4[i] for i in [0, 1, 2, 3]], textures['front'])
        draw_texture(screen, [self.projected_vertices4[i] for i in [4, 5, 6, 7]], textures['back'])
        draw_texture(screen, [self.projected_vertices4[i] for i in [0, 1, 5, 4]], textures['top'])
        draw_texture(screen, [self.projected_vertices4[i] for i in [3, 2, 6, 7]], textures['bottom'])
        draw_texture(screen, [self.projected_vertices4[i] for i in [0, 3, 7, 4]], textures['left'])
        draw_texture(screen, [self.projected_vertices4[i] for i in [1, 2, 6, 5]], textures['right'])

        draw_texture(screen, [self.projected_vertices5[i] for i in [0, 1, 2, 3]], textures['front'])
        draw_texture(screen, [self.projected_vertices5[i] for i in [4, 5, 6, 7]], textures['back'])
        draw_texture(screen, [self.projected_vertices5[i] for i in [0, 1, 5, 4]], textures['top'])
        draw_texture(screen, [self.projected_vertices5[i] for i in [3, 2, 6, 7]], textures['bottom'])
        draw_texture(screen, [self.projected_vertices5[i] for i in [0, 3, 7, 4]], textures['left'])
        draw_texture(screen, [self.projected_vertices5[i] for i in [1, 2, 6, 5]], textures['right'])

        draw_texture(screen, [self.projected_vertices6[i] for i in [0, 1, 2, 3]], textures['front'])
        draw_texture(screen, [self.projected_vertices6[i] for i in [4, 5, 6, 7]], textures['back'])
        draw_texture(screen, [self.projected_vertices6[i] for i in [0, 1, 5, 4]], textures['top'])
        draw_texture(screen, [self.projected_vertices6[i] for i in [3, 2, 6, 7]], textures['bottom'])
        draw_texture(screen, [self.projected_vertices6[i] for i in [0, 3, 7, 4]], textures['left'])
        draw_texture(screen, [self.projected_vertices6[i] for i in [1, 2, 6, 5]], textures['right'])

        draw_texture(screen, [self.projected_vertices7[i] for i in [0, 1, 2, 3]], textures['front'])
        draw_texture(screen, [self.projected_vertices7[i] for i in [4, 5, 6, 7]], textures['back'])
        draw_texture(screen, [self.projected_vertices7[i] for i in [0, 1, 5, 4]], textures['top'])
        draw_texture(screen, [self.projected_vertices7[i] for i in [3, 2, 6, 7]], textures['bottom'])
        draw_texture(screen, [self.projected_vertices7[i] for i in [0, 3, 7, 4]], textures['left'])
        draw_texture(screen, [self.projected_vertices7[i] for i in [1, 2, 6, 5]], textures['right'])

        draw_texture(screen, [self.projected_vertices8[i] for i in [0, 1, 2, 3]], textures['front'])
        draw_texture(screen, [self.projected_vertices8[i] for i in [4, 5, 6, 7]], textures['back'])
        draw_texture(screen, [self.projected_vertices8[i] for i in [0, 1, 5, 4]], textures['top'])
        draw_texture(screen, [self.projected_vertices8[i] for i in [3, 2, 6, 7]], textures['bottom'])
        draw_texture(screen, [self.projected_vertices8[i] for i in [0, 3, 7, 4]], textures['left'])
        draw_texture(screen, [self.projected_vertices8[i] for i in [1, 2, 6, 5]], textures['right'])

        draw_texture(screen, [self.projected_vertices9[i] for i in [0, 1, 2, 3]], textures['front'])
        draw_texture(screen, [self.projected_vertices9[i] for i in [4, 5, 6, 7]], textures['back'])
        draw_texture(screen, [self.projected_vertices9[i] for i in [0, 1, 5, 4]], textures['top'])
        draw_texture(screen, [self.projected_vertices9[i] for i in [3, 2, 6, 7]], textures['bottom'])
        draw_texture(screen, [self.projected_vertices9[i] for i in [0, 3, 7, 4]], textures['left'])
        draw_texture(screen, [self.projected_vertices9[i] for i in [1, 2, 6, 5]], textures['right'])

        draw_texture(screen, [self.projected_vertices10[i] for i in [0, 1, 2, 3]], textures['front'])
        draw_texture(screen, [self.projected_vertices10[i] for i in [4, 5, 6, 7]], textures['back'])
        draw_texture(screen, [self.projected_vertices10[i] for i in [0, 1, 5, 4]], textures['top'])
        draw_texture(screen, [self.projected_vertices10[i] for i in [3, 2, 6, 7]], textures['bottom'])
        draw_texture(screen, [self.projected_vertices10[i] for i in [0, 3, 7, 4]], textures['left'])
        draw_texture(screen, [self.projected_vertices10[i] for i in [1, 2, 6, 5]], textures['right'])

        draw_texture(screen, [self.projected_vertices11[i] for i in [0, 1, 2, 3]], textures2['front'])
        draw_texture(screen, [self.projected_vertices11[i] for i in [4, 5, 6, 7]], textures2['back'])
        draw_texture(screen, [self.projected_vertices11[i] for i in [0, 1, 5, 4]], textures2['top'])
        draw_texture(screen, [self.projected_vertices11[i] for i in [3, 2, 6, 7]], textures2['bottom'])
        draw_texture(screen, [self.projected_vertices11[i] for i in [0, 3, 7, 4]], textures2['left'])
        draw_texture(screen, [self.projected_vertices11[i] for i in [1, 2, 6, 5]], textures2['right'])

        draw_texture(screen, [self.projected_vertices12[i] for i in [0, 1, 2, 3]], textures['front'])
        draw_texture(screen, [self.projected_vertices12[i] for i in [4, 5, 6, 7]], textures['back'])
        draw_texture(screen, [self.projected_vertices12[i] for i in [0, 1, 5, 4]], textures['top'])
        draw_texture(screen, [self.projected_vertices12[i] for i in [3, 2, 6, 7]], textures['bottom'])
        draw_texture(screen, [self.projected_vertices12[i] for i in [0, 3, 7, 4]], textures['left'])
        draw_texture(screen, [self.projected_vertices12[i] for i in [1, 2, 6, 5]], textures['right'])

        draw_texture(screen, [self.projected_vertices13[i] for i in [0, 1, 2, 3]], textures['front'])
        draw_texture(screen, [self.projected_vertices13[i] for i in [4, 5, 6, 7]], textures['back'])
        draw_texture(screen, [self.projected_vertices13[i] for i in [0, 1, 5, 4]], textures['top'])
        draw_texture(screen, [self.projected_vertices13[i] for i in [3, 2, 6, 7]], textures['bottom'])
        draw_texture(screen, [self.projected_vertices13[i] for i in [0, 3, 7, 4]], textures['left'])
        draw_texture(screen, [self.projected_vertices13[i] for i in [1, 2, 6, 5]], textures['right'])

        draw_texture(screen, [self.projected_vertices14[i] for i in [0, 1, 2, 3]], textures['front'])
        draw_texture(screen, [self.projected_vertices14[i] for i in [4, 5, 6, 7]], textures['back'])
        draw_texture(screen, [self.projected_vertices14[i] for i in [0, 1, 5, 4]], textures['top'])
        draw_texture(screen, [self.projected_vertices14[i] for i in [3, 2, 6, 7]], textures['bottom'])
        draw_texture(screen, [self.projected_vertices14[i] for i in [0, 3, 7, 4]], textures['left'])
        draw_texture(screen, [self.projected_vertices14[i] for i in [1, 2, 6, 5]], textures['right'])

        draw_texture(screen, [self.projected_vertices15[i] for i in [0, 1, 2, 3]], textures['front'])
        draw_texture(screen, [self.projected_vertices15[i] for i in [4, 5, 6, 7]], textures['back'])
        draw_texture(screen, [self.projected_vertices15[i] for i in [0, 1, 5, 4]], textures['top'])
        draw_texture(screen, [self.projected_vertices15[i] for i in [3, 2, 6, 7]], textures['bottom'])
        draw_texture(screen, [self.projected_vertices15[i] for i in [0, 3, 7, 4]], textures['left'])
        draw_texture(screen, [self.projected_vertices15[i] for i in [1, 2, 6, 5]], textures['right'])

        draw_texture(screen, [self.projected_vertices16[i] for i in [0, 1, 2, 3]], textures['front'])
        draw_texture(screen, [self.projected_vertices16[i] for i in [4, 5, 6, 7]], textures['back'])
        draw_texture(screen, [self.projected_vertices16[i] for i in [0, 1, 5, 4]], textures['top'])
        draw_texture(screen, [self.projected_vertices16[i] for i in [3, 2, 6, 7]], textures['bottom'])
        draw_texture(screen, [self.projected_vertices16[i] for i in [0, 3, 7, 4]], textures['left'])
        draw_texture(screen, [self.projected_vertices16[i] for i in [1, 2, 6, 5]], textures['right'])

