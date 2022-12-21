
class ArbreBinaire:
    def __init__(self, etiquette):
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def affiche(self):
        """permet d'afficher un arbre"""
        if self==None:
            return None
        else :
            return [self.etiquette,ArbreBinaire.affiche(self.gauche),ArbreBinaire.affiche(self.droit)]
    
    def est_vide(self):
        if self.etiquette is None:
            return True
        else:
            return False  


def est_vide(arbre: ArbreBinaire) -> bool:
    """renvoie True si arbre est vide, False sinon"""
    if arbre is None:
        return True
    else:
        return False  

def racine(arbre: ArbreBinaire) -> str:
    """renvoie l'étiquette du nœud racine de arbre"""
    return arbre.etiquette

def gauche(arbre: ArbreBinaire) -> ArbreBinaire:
    """renvoie le sous-arbre à gauche de arbre"""
    return arbre.gauche

def droite(arbre: ArbreBinaire) -> ArbreBinaire:
    """renvoie le sous-arbre à droite de arbre"""
    return arbre.droit

def hauteur(arbre):
    if est_vide(arbre) :
        return 0
    else:
        hauteur_a_gauche = hauteur(gauche(arbre))
        hauteur_a_droite = hauteur(droite(arbre))
        return 1 + max(hauteur_a_gauche, hauteur_a_droite)


a = ArbreBinaire("AnneB")
a.gauche = ArbreBinaire("Pedro")
a.droit = ArbreBinaire("Sophia")
a.droit.gauche = ArbreBinaire("Malik2")
a.droit.droit = ArbreBinaire("AstridM")
a.gauche.gauche = ArbreBinaire("FredB")
a.droit.droit.gauche = ArbreBinaire("KevinH")
a.droit.droit.droit = ArbreBinaire("Nico")
a.droit.gauche.gauche = ArbreBinaire("Marc")

def membres(arbre, liste_membres):
    if not est_vide(arbre):
        liste_membres.append(racine(arbre))
        membres(gauche(arbre), liste_membres)
        membres(droite(arbre), liste_membres)



print(a.affiche())
print(racine(a))
#print(est_vide(a.droit.gauche.gauche.droit))
print("La hauteur est :", hauteur(a))

listes_membres=[]
membres(a,listes_membres)

print('Les membres sont : ', listes_membres)


def profil(arbre):
    if est_vide(gauche(arbre)) and est_vide(droite(arbre)):
        return 'bronze'
    elif est_vide(gauche(arbre)) or est_vide(droite(arbre)):
        return 'argent'
    else:
        return 'or'



print('profils : ', profil(a))

def membres_profils(arbre, liste_membres_profils):
    if not est_vide(arbre):
        liste_membres_profils.append((racine(arbre), profil(arbre)))
        membres_profils(gauche(arbre), liste_membres_profils)
        membres_profils(droite(arbre), liste_membres_profils)


listes_membres=[]
membres_profils(a,listes_membres)

print('Les membres sont : ', listes_membres)

tarifs = {'or': 20, 'argent': 30, 'bronze': 40}

def cotisations(arbre):
    if est_vide(arbre):
        return 0
    else:
        a_gauche = cotisations(gauche(arbre))
        a_droite = cotisations(droite(arbre))
        return tarifs[profil(a)] + a_gauche + a_droite



print("cotisation : ",cotisations(a))