class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def taille(arbre):
    if arbre == None:
        return 0
    else:
        return 1 + taille(arbre.fg) + taille(arbre.fd)

def hauteur(arbre):
    if arbre == None:
        return 0
    else:
        return 1 + max(hauteur(arbre.fg), hauteur(arbre.fd))

