import pygame
import random as rd

## Classes

class Cellule():
    def __init__(self, t, l, c, e):
        self.s = t
        self.ligne = l
        self.colonne = c
        self.x = self.s * c
        self.y = self.s * l
        self.etat = e
        self.etat_suivant = 0
        self.nb_voisins = 0

    def actualise_suivant(self):
        if (self.etat == 0 and self.nb_voisins==3) or (self.etat == 1 and self.nb_voisins in {2, 3}):
            self.etat_suivant = 1
        else:
            self.etat_suivant = 0

    def actualise_cellule(self):
        self.etat = self.etat_suivant

    def affiche_cellule(self, ecran):
        if self.etat:
            pygame.draw.rect(ecran, (0, 0, 0), (self.x, self.y, self.s, self.s))
        else:
            pygame.draw.rect(ecran, (255, 255, 255), (self.x, self.y, self.s, self.s))


class Grille():
    def __init__(self, l, h, t, e):
        self.longueur = l
        self.hauteur = h
        self.taille_cellule = t
        self.ecran = e
        self.cellules = [[Cellule(self.taille_cellule, r, c, rd.randint(0, 1)) for c in range(self.longueur)] for r in range(self.hauteur)]

    def actualisation(self):
        for r in range(self.hauteur):
            for c in range(self.longueur):
                self.cellules[r][c].nb_voisins = self.compte_voisins(r, c)
                self.cellules[r][c].actualise_suivant()
        for r in range(self.hauteur):
            for c in range(self.longueur):
                self.cellules[r][c].actualise_cellule()
                self.cellules[r][c].affiche_cellule(self.ecran)

    def compte_voisins(self, r, c):
        n = 0
        for d in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            try:
                n += self.cellules[r + d[0]][c + d[1]].etat
            except:
                pass
        return n

## initialisation
pygame.init()


## Constantes
longueur_grille, hauteur_grille = 640, 480
taille_cellule = 10
taille = (longueur_grille, hauteur_grille)

## Écran
fenetre = pygame.display.set_mode(taille)
pygame.display.set_caption("Jeu de la vie de John Conway")

## Grille
G = Grille(longueur_grille // taille_cellule , hauteur_grille // taille_cellule, taille_cellule, fenetre)

## Boucle des événements
continuer = False
while not continuer:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            continuer = True

    G.actualisation()
    pygame.display.flip()
    pygame.time.delay(200)

## Fermeture de la fenêtre
pygame.quit()
