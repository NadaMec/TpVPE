import pygame
import numpy as np
from math import cos, sin

Window_couleur = ('#C4EFF9')
Largeur, Hauteur = 1000, 670

pygame.display.set_caption("3D Cube")
screen = pygame.display.set_mode((Largeur, Hauteur))

# Paramètres du cube
facteur_echelle = 100
position_cube = np.array([Largeur / 2, Hauteur / 2, 0])  # Position initiale du cube (x, y, z)
rotation_angulaire = 0

# Définition des sommets du cube en 3D
sommets = np.array([
    [-1, -1, 1],
    [1, -1, 1],
    [1, 1, 1],
    [-1, 1, 1],
    [-1, -1, -1],
    [1, -1, -1],
    [1, 1, -1],
    [-1, 1, -1]
])



# Définition des sommets du deuxième cube en 3D
sommets_cube2 = sommets+ np.array([2, 0, 0])

# Définition des sommets du troisième cube en 3D
sommets_cube3 = sommets_cube2 + np.array([2, 0, 0])

# Définition des sommets du quatrième cube en 3D
sommets_cube4 = sommets_cube3 + np.array([2, 0, 0])

# Matrice de projection
projection_matrice = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

# Initialisation des sommets projetés
sommets_projetes = [np.zeros(3) for _ in range(len(sommets))]

sommets_projetes_cube2 = [np.zeros(3) for _ in range(len(sommets_cube2))]

sommets_projetes_cube3 = [np.zeros(3) for _ in range(len(sommets_cube3))]

sommets_projetes_cube4 = [np.zeros(3) for _ in range(len(sommets_cube4))]

# Chargement des textures du cube
textures = {
    'devant': pygame.image.load('p.png'),
    'dos': pygame.image.load('p.png'),
    'gauche': pygame.image.load('p.png'),
    'droite': pygame.image.load('p.png'),
    'haut': pygame.image.load('p.png'),
    'bas': pygame.image.load('p.png')
}

# Fonction pour interpoler des points le long d'un quadrilatère
def interpolation_points(quad, texture):
    points = {}
    L1, L2 = texture.get_size()

    for i in range(L2 + 1):
        x2 = interpolation_lin(quad[1], quad[2], i / L2)
        x3 = interpolation_lin(quad[0], quad[3], i / L2)

        for j in range(L1 + 1):
            x1 = interpolation_lin(x3, x2, j / L1)
            points[(j, i)] = x1

    return points

# Fonction pour dessiner une texture sur une surface
def dessiner_texture(surface, quad, texture):
    points = interpolation_points(quad, texture)

    L1, L2 = texture.get_size()
    for i in range(L1):
        for j in range(L2):
            polygon_points = [
                points[(i, j)],
                points[(i, j + 1)],
                points[(i + 1, j + 1)],
                points[(i + 1, j)]
            ]

            pygame.draw.polygon(surface, texture.get_at((i, j)), polygon_points)

# Fonction générique pour interpoler entre deux valeurs
def interpoler(point_depart, point_arrivee, facteur, operation):
    return operation(point_depart, point_arrivee, facteur)

# Fonction d'interpolation linéaire pour un point
def interpolation_lineaire(point_depart, point_arrivee, facteur):
    return interpoler(point_depart, point_arrivee, facteur, lambda x, y, t: x + t * (y - x))

# Fonction d'interpolation linéaire pour une liste de points
def interpolation_lin(point_depart, point_arrivee, facteur):
    return [interpoler(point_depart[i], point_arrivee[i], facteur, lambda x, y, t: x + t * (y - x)) for i in range(2)]

# Fonction pour dessiner une ligne entre deux sommets
def dessiner_ligne(i, j, sommets):
    pygame.draw.line(
        screen, (255, 255, 255), (sommets[i][0], sommets[i][1]), (sommets[j][0], sommets[j][1]))

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

    # Récupération de la position de la souris
    mouse_x, mouse_y = pygame.mouse.get_pos()
    position_cube = np.array([mouse_x, mouse_y, 0])

    # Matrices de rotation autour des axes x, y, z
    rotation_matrice_z = np.array([
        [cos(rotation_angulaire), -sin(rotation_angulaire), 0],
        [sin(rotation_angulaire), cos(rotation_angulaire), 0],
        [0, 0, 1],
    ])

    rotation_matrice_y = np.array([
        [cos(rotation_angulaire), 0, sin(rotation_angulaire)],
        [0, 1, 0],
        [-sin(rotation_angulaire), 0, cos(rotation_angulaire)],
    ])

    rotation_matrice_x = np.array([
        [1, 0, 0],
        [0, cos(rotation_angulaire), -sin(rotation_angulaire)],
        [0, sin(rotation_angulaire), cos(rotation_angulaire)],
    ])
    rotation_angulaire += 0.01

    screen.fill(Window_couleur)

    # Transformation des sommets du premier cube en 3D
    for i, sommet in enumerate(sommets):
        sommet_roté = np.dot(rotation_matrice_z, sommet.reshape((3, 1)))
        sommet_roté = np.dot(rotation_matrice_y, sommet_roté)
        sommet_roté = np.dot(rotation_matrice_x, sommet_roté)
        sommet_projeté = np.dot(projection_matrice, sommet_roté)

        x = int(sommet_projeté[0, 0] * facteur_echelle) + int(mouse_x)
        y = int(sommet_projeté[1, 0] * facteur_echelle) + int(mouse_y)
        z = int(sommet_projeté[2, 0] * facteur_echelle)

        sommets_projetes[i] = [x, y, z]

    # Transformation des sommets du deuxième cube en 3D
    for i, sommet in enumerate(sommets_cube2):
        sommet_roté = np.dot(rotation_matrice_z, sommet.reshape((3, 1)))
        sommet_roté = np.dot(rotation_matrice_y, sommet_roté)
        sommet_roté = np.dot(rotation_matrice_x, sommet_roté)
        sommet_projeté = np.dot(projection_matrice, sommet_roté)

        x = int(sommet_projeté[0, 0] * facteur_echelle) + int(mouse_x)
        y = int(sommet_projeté[1, 0] * facteur_echelle) + int(mouse_y)
        z = int(sommet_projeté[2, 0] * facteur_echelle)

        sommets_projetes_cube2[i] = [x, y, z]

        # Transformation des sommets du troisieme cube en 3D
    for i, sommet in enumerate(sommets_cube3):
        sommet_roté = np.dot(rotation_matrice_z, sommet.reshape((3, 1)))
        sommet_roté = np.dot(rotation_matrice_y, sommet_roté)
        sommet_roté = np.dot(rotation_matrice_x, sommet_roté)
        sommet_projeté = np.dot(projection_matrice, sommet_roté)

        x = int(sommet_projeté[0, 0] * facteur_echelle) + int(mouse_x)
        y = int(sommet_projeté[1, 0] * facteur_echelle) + int(mouse_y)
        z = int(sommet_projeté[2, 0] * facteur_echelle)

        sommets_projetes_cube3[i] = [x, y, z]

        # Transformation des sommets du quatrieme cube en 3D
    for i, sommet in enumerate(sommets_cube4):
        sommet_roté = np.dot(rotation_matrice_z, sommet.reshape((3, 1)))
        sommet_roté = np.dot(rotation_matrice_y, sommet_roté)
        sommet_roté = np.dot(rotation_matrice_x, sommet_roté)
        sommet_projeté = np.dot(projection_matrice, sommet_roté)

        x = int(sommet_projeté[0, 0] * facteur_echelle) + int(mouse_x)
        y = int(sommet_projeté[1, 0] * facteur_echelle) + int(mouse_y)
        z = int(sommet_projeté[2, 0] * facteur_echelle)

        sommets_projetes_cube4[i] = [x, y, z]

    # Dessiner les faces des cubes avec les textures
    dessiner_texture(screen, [sommets_projetes[i] for i in [0, 1, 2, 3]], textures['devant'])
    dessiner_texture(screen, [sommets_projetes[i] for i in [4, 5, 6, 7]], textures['dos'])
    dessiner_texture(screen, [sommets_projetes[i] for i in [0, 1, 5, 4]], textures['gauche'])
    dessiner_texture(screen, [sommets_projetes[i] for i in [3, 2, 6, 7]], textures['droite'])
    dessiner_texture(screen, [sommets_projetes[i] for i in [0, 3, 7, 4]], textures['haut'])
    dessiner_texture(screen, [sommets_projetes[i] for i in [1, 2, 6, 5]], textures['bas'])

    dessiner_texture(screen, [sommets_projetes_cube2[i] for i in [0, 1, 2, 3]], textures['devant'])
    dessiner_texture(screen, [sommets_projetes_cube2[i] for i in [4, 5, 6, 7]], textures['dos'])
    dessiner_texture(screen, [sommets_projetes_cube2[i] for i in [0, 1, 5, 4]], textures['gauche'])
    dessiner_texture(screen, [sommets_projetes_cube2[i] for i in [3, 2, 6, 7]], textures['droite'])
    dessiner_texture(screen, [sommets_projetes_cube2[i] for i in [0, 3, 7, 4]], textures['haut'])
    dessiner_texture(screen, [sommets_projetes_cube2[i] for i in [1, 2, 6, 5]], textures['bas'])

    dessiner_texture(screen, [sommets_projetes_cube3[i] for i in [0, 1, 2, 3]], textures['devant'])
    dessiner_texture(screen, [sommets_projetes_cube3[i] for i in [4, 5, 6, 7]], textures['dos'])
    dessiner_texture(screen, [sommets_projetes_cube3[i] for i in [0, 1, 5, 4]], textures['gauche'])
    dessiner_texture(screen, [sommets_projetes_cube3[i] for i in [3, 2, 6, 7]], textures['droite'])
    dessiner_texture(screen, [sommets_projetes_cube3[i] for i in [0, 3, 7, 4]], textures['haut'])
    dessiner_texture(screen, [sommets_projetes_cube3[i] for i in [1, 2, 6, 5]], textures['bas'])

    dessiner_texture(screen, [sommets_projetes_cube4[i] for i in [0, 1, 2, 3]], textures['devant'])
    dessiner_texture(screen, [sommets_projetes_cube4[i] for i in [4, 5, 6, 7]], textures['dos'])
    dessiner_texture(screen, [sommets_projetes_cube4[i] for i in [0, 1, 5, 4]], textures['gauche'])
    dessiner_texture(screen, [sommets_projetes_cube4[i] for i in [3, 2, 6, 7]], textures['droite'])
    dessiner_texture(screen, [sommets_projetes_cube4[i] for i in [0, 3, 7, 4]], textures['haut'])
    dessiner_texture(screen, [sommets_projetes_cube4[i] for i in [1, 2, 6, 5]], textures['bas'])

    # Dessiner les arêtes des cubes
    for p in range(4):
        dessiner_ligne(p, (p + 1) % 4, sommets_projetes)
        dessiner_ligne(p + 4, (p + 1) % 4 + 4, sommets_projetes)
        dessiner_ligne(p, p + 4, sommets_projetes)

        dessiner_ligne(p, (p + 1) % 4, sommets_projetes_cube2)
        dessiner_ligne(p + 4, (p + 1) % 4 + 4, sommets_projetes_cube2)
        dessiner_ligne(p, p + 4, sommets_projetes_cube2)

        dessiner_ligne(p, (p + 1) % 4, sommets_projetes_cube3)
        dessiner_ligne(p + 4, (p + 1) % 4 + 4, sommets_projetes_cube3)
        dessiner_ligne(p, p + 4, sommets_projetes_cube3)

        dessiner_ligne(p, (p + 1) % 4, sommets_projetes_cube4)
        dessiner_ligne(p + 4, (p + 1) % 4 + 4, sommets_projetes_cube4)
        dessiner_ligne(p, p + 4, sommets_projetes_cube4)

    pygame.display.update()