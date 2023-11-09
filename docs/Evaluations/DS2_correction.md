
# Devoir n°2 : POO sur table

## Enoncé 

{{telecharger("Devoir n°2 : SQL","../pdf/eval/DS2.pdf")}}

## Correction 

**Partie 1**  


1.  
    - `nom` : attribut  
    - `tab_voisines` : attribut  
    - `tab_couleurs_disponibles` : attribut


2. `nom_region` est de type `str` : chaîne de caractère.

3.  `ge = Region ("Grand Est")`

4.  
    ```python
    def renvoie_premiere_couleur_disponible(self): 
        return self.tab_couleurs_disponibles[0]
    ```

5.  
    ```python
    def renvoie_nb_voisines(self) :
        return len(self.tab_voisines)
    ```

6.  
    ```python
    def est_coloriee(self): 
        if self.couleur_attribuee == None :
            return False
        else :
            return True
    ```

7.  
    ```python
    def retire_couleur(self, couleur):
        if couleur in self.tab_couleurs_disponibles:
            self.tab_couleurs_disponibles.remove(couleur)
    ```

8.  
    ```python
    def est_voisine(self, region):
        for i in range(len(self.tab_voisines)) :
            if region == self.tab_voisines[i] :
                return True
        return False
    ```


**Partie 2**  

9.  
    ```python
    def renvoie_tab_regions_non_coloriees(self): 
        L=[]
        for region in self.tab_regions :
            if est_coloriee(region) == False :
                L.append(region)
        return L
    ```

10. a. La méthode renvoie `None` dans le cas ou tout est colorié.

    b. La région renvoyée est la région qui a le plus de voisines parmi celles qui ne sont pas coloriées.


11.  
    ```python
    def colorie(self):
        region_m = self.renvoie_max()
        while region_m:
            region_m.couleur_attribuee = region_m.renvoie_premiere_couleur_disponible()
            for voisine in region_m.tab_voisines:
                voisine.retire_couleur(region_m.couleur_attribuee)
            region_m = self.renvoie_max()
    ```