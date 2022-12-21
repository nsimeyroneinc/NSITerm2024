class Noeud:
    def __init__(self, gauche, valeur, droite):
        self.gauche = gauche
        self.valeur = valeur
        self.droite = droite


    def affiche(self):
        """permet d'afficher un arbre"""
        if self==None:
            return None
        else :
            return [self.valeur,Noeud.affiche(self.gauche),Noeud.affiche(self.droite)]
    
    def est_vide(self):
        if self.valeur is None:
            return True
        else:
            return False  


def inserer(v, abr):
    if abr is None:
        return Noeud(None, v, None)
    if v > abr.valeur:
        return Noeud(abr.gauche, abr.valeur, inserer(v, abr.droite))
    elif v < abr.valeur:
        return Noeud(inserer(v, abr.gauche), abr.valeur, abr.droite)
    else:
        return abr

def nb_sup(v, abr):
    if abr is None:
        return 0
    elif abr.valeur >= v:
        return 1+nb_sup(v, abr.gauche)+nb_sup(v, abr.droite)
    else:
        return nb_sup(v, abr.gauche)+nb_sup(v, abr.droite)


abr = Noeud(Noeud(None, 13, None), 15, Noeud(None, 21, None))

abr=inserer(11,abr)
abr=inserer(14,abr)
abr=inserer(18,abr)
abr=inserer(20,abr)
abr=inserer(27,abr)


print(abr.affiche())

def nb_sup2(v, abr):
    if abr is None:
        return 0
    else:
        if abr.valeur > v:
            return 1+nb_sup2(v, abr.gauche)+nb_sup2(v, abr.droite)
        elif abr.valeur==v:
            return 1+nb_sup2(v,abr.droite)
        else:
            return nb_sup2(v, abr.droite)

def nb_sup3(v, abr):
    T=0
    if abr is None:
        return 0
    elif abr.valeur > v:
        T+=1
        nb_sup3(v, abr.gauche)
        nb_sup3(v, abr.droite)
    else:
        return nb_sup3(v, abr.droite)

print(nb_sup(16,abr))
print(nb_sup2(16,abr))
print(nb_sup3(16,abr))