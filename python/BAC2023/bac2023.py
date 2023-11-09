class Region:
    '''Modélise une région d'un pays sur une carte.'''
    def __init__(self, nom_region):
        '''
        initialise une région 
        IN : param nom_region (str) le nom de la région
        '''
        self.nom = nom_region # tableau des régions voisines, vide au départ
        self.tab_voisines = [] # tableau des couleurs disponibles pour colorier la région
        self.tab_couleurs_disponibles = ['rouge', 'vert','bleu', 'jaune', 'orange', 'marron'] # couleur attribuée à la région et non encore choisie au départ
        self.couleur_attribuee = None

    def renvoie_premiere_couleur_disponible(self):
        '''
        Renvoie la première couleur du tableau des couleurs disponibles supposé non vide.
        OUT : return (str)
        '''
        return  self.tab_couleurs_disponibles[0]

    def renvoie_nb_voisines(self) :
        '''
        Renvoie le nombre de régions voisines.
        OUT : return (int)
        '''
        return len(self.tab_voisines)

    def est_coloriee(self):
        '''
        Renvoie True si une couleur a été attribuée à cette région et False sinon.
        OUT :  return (bool)
        '''
        return self.couleur_attribuee != None
    
    def retire_couleur(self, couleur):
        '''
        Retire couleur du tableau de couleurs disponibles de la région si elle est dans ce tableau. Ne fait rien sinon.
        IN : param couleur (str)
        OUT : ne renvoie rien, effet de bord sur le tableau des couleursdisponibles
        '''
        if couleur in self.tab_couleurs_disponibles :
            self.tab_couleurs_disponibles.remove(couleur)

    def est_voisine(self, region):
        '''
        Renvoie True si la region passée en paramètre est une voisine et False sinon.
        IN : param region (Region)
        OUT : return (bool)
        '''
        # for reg in self.tab_voisines :
        #     if reg == region :
        #         return True
        # return False
    
        i = 0
        while self.tab_voisines[i] != region and i < len(self.tab_voisines) :
            i = i + 1
        return i != len(self.tab_voisines)

class Pays:
    '''Modélise un pays sur une carte composé de plusieurs regions.'''
    def __init__(self):
        self.tab_regions = []
        
    def renvoie_tab_regions_non_coloriees(self):
        '''
        Renvoie un tableau dont les éléments sont les régions du pays sans couleur attribuée.
        OUT : return (list) tableau d’instances de la classe
        Region
        '''
        result = []
        for reg in self.tab_regions :
            if not reg.est_coloriee() : #reg.couleur_attribuee != None
                result.append(reg)
        return result

    def renvoie_max(self):
        nb_voisines_max = -1
        region_max = None
        for reg in self.renvoie_tab_regions_non_coloriees():
            if reg.renvoie_nb_voisines() > nb_voisines_max:
                nb_voisines_max = reg.renvoie_nb_voisines()
                region_max = reg
        return region_max
    
    def colorie(self):
        reg = self.renvoie_max()
        while reg != None :
            reg.couleur_attribuee = reg.renvoie_premiere_couleur_disponible()
            for voisine in reg.tab_voisines :
                voisine.retire_couleur(reg.couleur_attribuee)
            reg = self.renvoie_max()
            
france = Pays()
ara = Region("Auvergne-Rhône-Alpes")
bfc = Region("Bourgogne-Franche-Comté")
b = Region("Bretagne")
cv = Region("Centre-Val de Loire")
c = Region("Corse")
ge = Region("Grand Est")
h = Region("Hauts-de-France")
i = Region("Île-de-France")
n = Region("Normandie")
na = Region("Nouvelle-Aquitaine")
o = Region("Occitanie")
pl = Region("Pays de la Loire")
pa = Region("Provence-Alpes-Côte d'Azur")

ara.tab_voisines = [bfc, cv, na, o, pa]
bfc.tab_voisines = [ge,i,cv,ara]
b.tab_voisines = [n,pl]
cv.tab_voisines = [n,pl,na,ara,bfc,i]
c.tab_voisines = []
ge.tab_voisines = [h,i,bfc]
h.tab_voisines = [n,i,ge]
i.tab_voisines = [h,n,cv,bfc,ge]
n.tab_voisines = [b,pl,cv,i,h]
na.tab_voisines = [pl,cv,ara,o]
o.tab_voisines = [na,ara,pa]
pl.tab_voisines = [b,n,cv,na]
pa.tab_voisines = [ara,o]

france.tab_regions = [ara,bfc,b,cv,c,ge,h,i,n,na,o,pl,pa]

print(pa.est_voisine(i))

