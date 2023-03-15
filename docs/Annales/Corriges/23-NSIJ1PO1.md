hide: - navigation  in docs.md

{% set repere_sujet = "23-NSIJ1PO1" %}

{{ corrige_sujetbac(repere_sujet) }}


{{ corrige_exobac(repere_sujet,1) }}

1. 
    a. La table contient déjà une entrée dont l'attribut id_equipe vaut 11. Comme il s'agit de la clé primaire cela provoque une erreur.

    b. L'attribut telephone est une chaine de caractère limité à 20. On ne pouvait pas choisir des entiers car les numeros de téléphone commençant par 0 il disparaitrait.

    c. 
    ```sql
    Lyon 451 cours d'Emile Zola,69100 Villeurbanne 04 05 06 07 08
    ```

    d. La requête le nombre d'entrée dans la table `equipe`  
    ```sql
    12
    ```

    e. 
    ```sql
    SELECT nom
    FROM Equipe
    ORDER BY noms
    ```

    f. 
    ```sql
    UPDATE Equipe
    SET nom=Tarbes
    WHERE id_equipe=4
    ```

2.  a. L'attribut `id_equipe` a été déclaré clé étrangère pour faire la liaison avec la table Equipe et sa clé primaire `id_equipe`.
    b. On ne peut pas supprimer directement cette équipe dans la table `Equipe` car elle poséde une clé primaire reliée à une clé étrangère.  
    c. 
    ```sql
    SELECT Joueuse.nom, Joueuse.prenom
    FROM Joueuse
    JOIN Equipe ON Equipe.id_equipe=Joueuse.id_equipe
    WHERE Equipe.nom='Angers'
    ORDER BY Joueuse.nom
    ```


{{ corrige_exobac(repere_sujet,2) }}

1.  a. 11 - 20 - 32 - 11 - 20 - 32 - 11 - 32 - 11 
    b. 11 - 11 - 20 - 20 - 32 - 32 - 11 - 11 - 32 

2.  a.
    ```python
    liste_attente=[Processus(11,4),Processus(20,2),Processus(32,3)]
    ```

    b. 
    ```python
    def execute_un_cycle(self):
        self.reste_a_faire-=1
        
    def change_etat(self,nouvel_etat):
        self.etat=nouvel_etat
        
    def est_termine(self):
        if self.reste_a_faire==0:
            return True
        else:
            return False
    ```

    c. 
    ```python        
    def tourniquet(liste_attente, quantum):
        ordre_execution = []
        while liste_attente != []:
            # On extrait le premier processus
            processus = liste_attente.pop(0)
            processus.change_etat("En cours d'exécution")
            compteur_tourniquet = 0
            while processus.reste_a_faire > 0 and compteur_tourniquet < quantum :
                ordre_execution.append(processus.pid)
                processus.execute_un_cycle()
                compteur_tourniquet = compteur_tourniquet + 1
            if processus.reste_a_faire != 0:
                processus.change_etat("Suspendu")
                liste_attente.append(processus)
            else:
                processus.change_etat("Terminé")
        return ordre_execution
    ```

 

    

{{ corrige_exobac(repere_sujet,3) }}

1.  a. `from math import sqrt` permet d'import la fonction racine carrée de la bibliothèque math  
    b. `0.1 + 0.2 == 0.3` return `False` car l'ordinateur travaille en binaire et le developpement en binaire de 0.1 est infini, il y a donc une troncature ce qui provoque ce résultat.  
    c. `point_A` est un tupple qui n'est pas mutable d'où l'erreur.

2.  a. 
    ```python linenums='1' hl_lines='6'
    from math import sqrt
    class Segment:
        def __init__(self,point1,point2):
            self.p1=point1
            self.p2=point2
            self.longueur= sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)
    ```

    b.  
    ```python
    def liste_segments(liste_points):
        n = len(liste_points)
        segments = []
        for i in range(n):
            for j in range(i+1, n):
                # On construit le segment à partir des points i et j.
                seq = Segment(liste_points[i],liste_points[j])
                segments.append(seg) # On l'ajoute à la liste
        return segments    
    ```

    c. Pour liste de points de longueur n, on aura $(n-1) + (n-2) + ... + 1$ segments 

    d. La complexité est donc de l'ordre de $O(n^2)$. En effet on a : $(n-1) + (n-2) + ... + 1= (n-1) \times \dfrac{n-1+1}{2}$

3.  a. 
    ```python
    def plus_court_segment(liste_segments):
        if len(liste_segments)==1:
            return liste_segments[0]
        else:
            c1=plus_court_segment(moitie_gauche(liste_segments))
            c2=plus_court_segment(moitie_droite(liste_segments))
        if c1.longueur>c2.longueur:
            return c2
        else:
            return c1
    ```

4.  a. 
    ```python
    point_A=(3,4)
    point_B=(2,3)
    point_C=(-3,-1)

    nuage_points=[point_A,point_B,point_C]
    ```

    b. 
    ```python
    rep=plus_court_segment(liste_segments(liste_points))

    print((rep.p1[0],rep.p1[1]),(rep.p2[0],rep.p2[1]))
    ```
