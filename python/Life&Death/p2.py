import pygame
from pygame.locals import *


class Grille:
    def __init__(self, l:int, h:int):
        self.longueur = l
        self.hauteur = h
        self.cellules = [self.longueur*[1] for _ in range(self.hauteur)]
        self.puce = Puce(self.longueur//2, self.hauteur//2)
        self.go = True

    def actualisation(self):
        l, c = self.puce.ligne, self.puce.colonne

        try:
            self.puce.avance(self.cellules[l][c])
            self.cellules[l][c] = 1 - self.cellules[l][c]
            pygame.draw.rect(fenetre, [255*self.cellules[l][c]]*3, [l, c, 1, 1])
            pygame.draw.rect(fenetre, [255, 0, 0], [self.puce.ligne, self.puce.colonne, 1, 1])
        except:
            pass


class Puce:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def __init__(self, l, c):
        self.ligne = l
        self.colonne = c
        self.dir = 0

    def avance(self, cellule):
        if cellule == 1:
            self.dir = (self.dir+1) % 4
        else:
            self.dir = (self.dir-1) % 4

        self.ligne += Puce.directions[self.dir][0]
        self.colonne += Puce.directions[self.dir][1]


pygame.init()

longueur, hauteur = 640, 480
fenetre = pygame.display.set_mode((longueur, hauteur))
fenetre.fill([255, 255, 255])
pygame.display.flip()


G = Grille(longueur, hauteur)

continuer = True
while continuer:

    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            continuer = False

    G.actualisation()

    pygame.display.flip()


pygame.quit()
