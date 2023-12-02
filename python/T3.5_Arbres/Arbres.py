class Arbre:
    def __init__(self,valeur):
        """Initialisation de l'arbre racine + sous-arbre gauche et sous-arbre droit"""
        self.v=valeur
        self.gauche=None
        self.droit=None
        
    def ajout_gauche(self,val):
        """On ajoute valeur dans le sous-arbre gauche sous la forme [val,None,None]"""
        self.gauche=Arbre(val)
        
    def ajout_droit(self,val):
        """ On ajoute valeur dans le sous-arbre droit sous la forme [val,None,None]"""
        self.droit=Arbre(val)

    def affiche(self):
        """permet d'afficher un arbre"""
        if self==None:
            return None
        else :
            return [self.v,Arbre.affiche(self.gauche),Arbre.affiche(self.droit)]
        
    def taille(self):
        if self==None:
            return 0
        else :
            return 1+Arbre.taille(self.droit)+Arbre.taille(self.droit)
    
    def hauteur(self):
        if self==None:
            return 0
        elif self.gauche==None and self.droit==None:
            return 0
        else :
            return 1+max(Arbre.hauteur(self.gauche),Arbre.hauteur(self.droit))

    def get_gauche(self):
        return self.gauche

    def get_droit(self):
        return self.droit
    
    
    def get_valeur(self):
        if self==None:
            return None
        else:
            return self.v
