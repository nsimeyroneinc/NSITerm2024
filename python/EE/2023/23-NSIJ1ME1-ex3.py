class Region:
    '''Modélise une région d'un pays sur une carte.'''
    def __init__(self, nom_region):
        '''
        initialise une région
        : param nom_region (str) le nom de la région
        '''
        self.nom = nom_region
        # tableau des régions voisines, vide au départ
        self.tab_voisines = []
        # tableau des couleurs disponibles pour colorier la région
        self.tab_couleurs_disponibles = ['rouge', 'vert','bleu', 'jaune', 'orange', 'marron']
        # couleur attribuée à la région et non encore choisie au départ
        self.couleur_attribuee = None
        


    def renvoie_premiere_couleur_disponible(self): 
        ''' Renvoie la première couleur du tableau des couleurs disponibles supposé non vide. 
        : return (str) '''
        return self.tab_couleurs_disponibles[0]



    def renvoie_nb_voisines(self) :
        ''' Renvoie le nombre de régions voisines. 
        : return (int) '''
        return len(self.tab_voisines)


    def est_coloriee(self): 
        ''' Renvoie True si une couleur a été attribuée à cette région et False sinon. 
        : return (bool) '''
        if self.couleur_attribuee == None :
            return False
        else :
            return True




    def retire_couleur(self, couleur):
        ''' Retire couleur du tableau de couleurs disponibles de la région si elle est dans ce tableau.
        Ne fait rien sinon. : param couleur (str) : ne renvoie rien : effet de bord sur le tableau des
        couleurs disponibles '''
        if couleur in self.tab_couleurs_disponibles:
            self.tab_couleurs_disponibles.remove(couleur)



    def est_voisine(self, region):
        ''' Renvoie True si la region passée en paramètre est une voisine et False sinon. 
        : param region (Region) 
        : return (bool) '''
        for i in range(len(self.tab_voisines)) :
            if region == self.tab_voisines[i] :
                return True
        return False


class Pays(self,tab_regions):
    self.tab_regions
    
    
    def renvoie_tab_regions_non_coloriees(self): 
        ''' Renvoie un tableau dont les éléments sont les régions du pays sans couleur attribuée. :
        return (list) tableau d’instances de la classe Region '''
        L=[]
        for region in self.tab_regions :
            if est_coloriee(region) == False :
                L.append(region)
        return L

    def renvoie_max(self):
        nb_voisines_max = -1
        region_max = None
        for reg in self.renvoie_tab_regions_non_coloriees():
            if reg.renvoie_nb_voisines() > nb_voisines_max:
                nb_voisines_max = reg.renvoie_nb_voisines()
                region_max = reg
        return region_max

    def colorie(self):
        region_m = self.renvoie_max()
        while region_m:
            region_m.couleur_attribuee = region_m.renvoie_premiere_couleur_disponible()
            for voisine in region_m.tab_voisines:
                voisine.retire_couleur(region_m.couleur_attribuee)
            region_m = self.renvoie_max()


ge = Region ("Grand Est")
ge.colorie()