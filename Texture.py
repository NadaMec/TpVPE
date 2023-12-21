import pygame

def interpolate_points(quad, texture):
    points = {}
    L1, L2 = texture.get_size()

    for i in range(L2 + 1):
        x2 = interpolate_linear(quad[1], quad[2], i / L2)
        x3 = interpolate_linear(quad[0], quad[3], i / L2)

        for j in range(L1 + 1):
            x1 = interpolate_linear(x3, x2, j / L1)
            points[(j, i)] = x1

    return points

def interpolate(start_point, end_point, factor, operation):
    return [operation(start_point[i], end_point[i], factor) for i in range(len(start_point))]

def interpolate_linear(start_point, end_point, factor):
    return interpolate(start_point, end_point, factor, lambda x, y, t: x + t * (y - x))

def draw_texture(surface, quad, texture):
    points = interpolate_points(quad, texture)

    L1, L2 = texture.get_size()
    for i in range(L1):
        for j in range(L2):
            polygon_points = [
                (int(points[(i, j)][0]), int(points[(i, j)][1])),
                (int(points[(i, j + 1)][0]), int(points[(i, j + 1)][1])),
                (int(points[(i + 1, j + 1)][0]), int(points[(i + 1, j + 1)][1])),
                (int(points[(i + 1, j)][0]), int(points[(i + 1, j)][1]))
            ]

            pygame.draw.polygon(surface, texture.get_at((i, j)), polygon_points)
