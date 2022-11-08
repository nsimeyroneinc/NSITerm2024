
{% set num = 8 %}
{% set titre = "Diviser Pour Régner"%}
{% set theme = "algorithmique" %}
{% set niveau = "terminale"%} 


{{ titre_chapitre(num,titre,theme,niveau)}}


## Activités 

{{ titre_activite("Retour sur l'algorithme de dichotomie",["rappel"],0) }}

!!! Aide
    Cette activité revient sur deux algorithmes de recherche d'un élément dans une liste déjà rencontrés en classe de première.

1. Ecrire une fonction `recherche(x,l)` qui en effectuant un parcours simple de la liste, renvoie `True` ou `False` selon que l'élément `x` se trouve ou non dans la liste `l`.

2. On suppose maintenant que la **liste est triée**, l'algorithme de recherche par dichotomie vue en classe de première consiste alors à  
    :one: partager la liste en deux listes de longueurs égales (à une unité près)   
    :two: comparer  l'élément recherché avec celui situé au milieu de la liste  
    :three: en déduire dans quelle moitié poursuivre la recherche  
    On s'arrête lorsque la zone de recherche ne contient plus qu'un élément.  

    1. Faire fonctionner "à la main" cet algorithme pour rechercher `6` dans `[1,3,5,7,11,13]`.  
    2. Programmer cet algorithme en version impérative.  

    ??? aide "A compléter - Dichotomie version impérative :heart:"
        ```python linenums='1'
        def recherche_dichotomique(tab, val) :
            '''
            renvoie True ou False suivant la présence de la valeur val dans le tableau trié tab.
            '''
            i_debut = 0
            i_fin = len(tab) - 1
            while i_debut <= i_fin :
                i_centre = (... + ...) // 2     # (1)
                val_centrale = tab[...]          # (2) 
                if val_centrale == val:               # (3) 
                    return True
                if val_centrale < val:                # (4) 
                    i_debut = ....              # (5) 
                else :
                    i_fin = ...
            return False
        ```

        1. on prend l'indice central
        2. on prend la valeur centrale
        3. si la valeur centrale est la valeur cherchée...
        4. si la valeur centrale est trop petite...
        5. on ne prend pas la valeur centrale qui a déjà été testée

    Exemple d'utilisation :

    ```python
    >>> tab = [1, 5, 7, 9, 12, 13]
    >>> recherche_dichotomique(tab, 12)
    True
    >>> recherche_dichotomique(tab, 17)
    False
    ```

    À chaque tour de la boucle ```while```, la taille de la liste est divisée par 2. Ceci confère à cet algorithme une **complexité logarithmique** (bien meilleure qu'une complexité linéaire).

    !!! note "Complexité"

        Pour pouvoir majorer le nombre maximum d’itérations, si le tableau contient n valeurs, et si on a un entier $k$ tel que $n \leq 2^k$ , alors puisque qu’à chaque itération, on sélectionne une moitié de ce qui reste :  

        - au bout d’une itération, une moitié de tableau aura au plus $\dfrac{2^k}{2} = 2^{k−1}$ éléments,  
        - un quart aura au plus $2^{k−2}$    
        - et au bout de $i$ itérations, la taille de ce qui reste à étudier est de taille au plus $2^{k−i}$.  
        - En particulier, si l’on fait $k$ itérations, il reste au plus $2^{k−k} = 1$ valeur du tableau à examiner. On est sûr de s’arrêter cette fois-ci

        On a donc montré que si l’entier $k$ vérifie $n \leq 2^k$ , alors l’algorithme va effectuer au plus $n$ itérations.
        La plus petite valeur est obtenue pour $\log(n) = \log_2 k$.  
        Ainsi, la complexité de la fonction est de l’ordre du logarithme  de la longueur de la liste ($O(log_2(n))$).  
        $log_2(n)$.


3. Dichotomie récursive sans slicing

Il est possible de programmer de manière récursive la recherche dichotomique sans toucher à la liste, et donc en jouant uniquement sur les indices :

!!! note "Dichotomie version récursive sans slicing :heart:"
    ```python linenums='1'
    def dicho_rec_2(tab, val, i=0, j=None): # (1)
        if j is None:                       # (2)
            j = len(tab)-1
        if i > j :
            return False
        m = (i + j) // 2
        if tab[m] < val :
            return dicho_rec_2(tab, val, m + 1, j)
        elif tab[m] > val :
            return dicho_rec_2(tab, val, i, m - 1 )
        else :
            return True
    ```

    1. Pour pouvoir appeler simplement la fonction sans avoir à préciser les indices, on leur donne des paramètres par défaut.
    2. Il est impossible de donner ```j=len(tab)-1``` par défaut (car ```tab``` est aussi un paramètre). On passe donc par une autre valeur (ici ```None```) qu'on va ici intercepter.

    Exemple d'utilisation :

    ```python
    >>> tab = [1, 5, 7, 9, 12, 13]
    >>> dicho_rec_2(tab, 12)
    True
    >>> dicho_rec_2(tab, 17)
    False
    ```

Les algorithmes de dichotomie présentés ci-dessous ont tous en commun de diviser par deux la taille des données de travail à chaque étape. Cette méthode de résolution d'un problème est connue sous le nom de *diviser pour régner*, ou *divide and conquer* en anglais.  

Une définition pourrait être :

!!! abstract "Définition :heart:"
    Un problème peut se résoudre en employant le paradigme *diviser pour régner* lorsque :  
    - il est possible de décomposer ce problème en sous-problèmes **indépendants**.  
    - la taille de ces sous-problèmes est une **fraction** du problème initial


**Remarques :**

- Les sous-problèmes peuvent nécessiter d'être ensuite recombinés entre eux (voir plus loin le tri fusion).


{{ titre_activite("Tri fusion",[]) }}

1. Algorithmes de tri vus en première et revus cette année :  
    1. Rappeler rapidement le principe du [tri par sélection](https://nsimeyroneinc.github.io/NSITerm/Algo/T5_2_algo_tri/){target=_blank} vu en classe de première. Donner les étapes de cet algorithme pour trier la liste `[10,6,3,9,7,5]`
    2. Rappeler rapidement le principe du [tri par insertion](https://nsimeyroneinc.github.io/NSITerm/Algo/T5_2_algo_tri/){target=_blank} vu en classe de première. Donner les étapes de cet algorithme pour trier la liste `[10,6,3,9,7,5]` 
    3. Quelle est la complexité de ces deux algorithmes ?

2. L'algorithme du **tri fusion** consiste à :  <br>
    :one: partager la liste en deux moitiés (à une unité près),  
    :two: trier chacune des deux moitiés,  
    :three: les fusionner pour obtenir la liste triée.  

    On a schématisé le tri de la liste `[10,6,3,9,7,5]` suivant ce principe ci-dessous :  
    ```mermaid
        graph TD
        subgraph Partager en deux
        S["[10,6,3,9,7,5]"] --> S1["[10,6,3]"]
        S --> S2["[9,7,5]"]
        end
        subgraph Fusionner
        S1 -.Trier.-> T1["[3,6,10]"]
        S2 -.Trier.-> T2["[5,7,9]"]
        T1 --> T["[3,5,6,7,9,10]"]
        T2 --> T
        end
    ```  

    1. Le tri des deux moitiés est lui-même effectué par tri fusion, par conséquent que peut-on dire de cet algorithme ?  
    2. On a schématisé ci-dessous le fonctionnement complet de l'algorithme pour la liste `[10,6,3,9,7,5]`, recopier et compléter les cases manquantes.

    ```mermaid
        graph TD
            subgraph Partager en deux
            S["[10,6,3,9,7,5]"] --> S1["[10,6,3]"]
            S --> S2["[9,7,5]"]
            S1 --> S11["[10]"]
            S1 --> S12["[6,3]"]
            S2 --> S21["[9]"]
            S2 --> S22["[...,...]"]
            S12 --> S121["[6]"]
            S12 --> S122["[3]"]
            S22 --> S221["[...]"]
            S22 --> S222["[...]"]
        end
            subgraph Fusionner
            S121 --> T21["[...,...]"]
            S122 --> T21
            S221 --> T22["[5,7]"]
            S222 --> T22["[5,7]"]
            S11 --> T1["[...,...,...]"]
            T21 --> T1
            S21 --> T2["[...,...,...]"]
            T22 --> T2
            T1 --> T["[3,5,6,7,9,10]"]
            T2 --> T
        end

    ```  
3. Implémentation en Python  

    1. Programmer une fonction `partage(l)` qui prend en argument une liste `l` et renvoie les deux moitiés `l1` et `l2` (à une unité près) de `l`. Par exemple `partage([3,7,5])` renvoie `[3]` et `[7,5]`.

        !!! aide
            * Penser à utiliser les constructions de listes par compréhension  
            * Les *slices* de Python sont un moyen efficace d'effectuer le partage, mais leur connaissance n'est pas un attendu du programme de terminale. Les élèves intéressés pourront faire leur propre recherche sur le *Web*.  

    2. On donne ci-dessous une fonction `fusion(l1,l2)` qui prend en argument deux listes **déjà triées** `l1` et `l2` et renvoie la liste triée `l` fusion de `l1` et `l2` :  
        
        ```python linenums="1"
        def fusion(l1,l2):
            ind1=0
            ind2=0
            l = []
            while ind1<len(l1) and ind2<len(l2):
                if l1[ind1]<l2[ind2]:
                    l.append(...)
                    ind1+=1
                else:
                    l.append(...)
                    ind2+=1
            if ind1==len(l1):
                for k in range(ind2,len(l2)):
                    l.append(...)
            else:
                for k in range(ind1,len(l1)):
                    l.append(...)
            return l
        ```

        1. Recopier et compléter cette fonction.  
        2. Quel est le rôle des variables `ind1` et `ind2` ?  
        3. Ajouter un commentaire décrivant le rôle de la boucle `while`.  
        4. Ajouter un commentaire décrivant le rôle des lignes 12 à 17.  
    
    3. En utilisant les deux fonctions précédentes, écrire une fonction `tri_fusion(l)` qui implémente l'algorithme du tri fusion en Python.  


        ```python linenums="1"
        def tri_fusion(liste):
            long = len(liste)
            if long <= 1:
                return liste
            else:
                l1, l2 = partage(liste)
                l1 = tri_fusion(l1)
                l2 = tri_fusion(l2)
            return fusion(l1,l2)  

        ``` 


    !!! Important
        On montre que l'algorithme du tri fusion a une complexité en $O(n\log(n))$, c'est donc un algorithme plus efficace que le tri par insertion ou le tri par sélection qui ont tous les deux une complexité en $O(n^2)$.


## Exercices

!!! exo "Maximum des éléments d'une liste"
    On propose l'algorithme suivant pour la recherche du maximum des éléments d'une liste :<br>
    :one: Partager la liste en deux moitiés `l1` et `l2` <br>
    :two: Chercher les maximums `m1` de `l1` et `m2` de `l2` <br>
    :three: En déduire le maximum `m` de `l`.

    1. Expliquer pourquoi cet algorithme fait partie de la méthode **diviser pour régner**.
    2. Cet algorithme est-il récursif ? Justifier.
    3. Ecrire une implémentation en Python de cet algorithme.


!!! exo "Epreuve Pratique"
    === "Sujet 38 : Exercice 1"
        Écrire une fonction tri_selection qui prend en paramètre une liste tab de nombres entiers et qui renvoie le tableau trié par ordre croissant.  
        On utilisera l’algorithme suivant :  
        
        - on recherche le plus petit élément du tableau, et on l'échange avec l'élément d'indice 0 ;  
        - on recherche le second plus petit élément du tableau, et on l'échange avec l'élément d'indice 1 ;  
        - on continue de cette façon jusqu'à ce que le tableau soit entièrement trié.  
        
        Exemple :
        ```python
        >>> tri_selection([1,52,6,-9,12])
        [-9, 1, 6, 12, 52]
        ```
    === "Sujet 35 : Exercice 2"
        Écrire une fonction qui prend en paramètre un tableau d'entiers non vide et qui renvoie la  moyenne de ces entiers. La fonction est spécifiée ci-après et doit passer les assertions fournies.  

        ```python
        def moyenne (tab):
            '''
                moyenne(list) -> float
                Entrée : un tableau non vide d'entiers
                Sortie : nombre de type float
                Correspondant à la moyenne des valeurs présentes dans le
                tableau
            '''

        assert moyenne([1]) == 1
        assert moyenne([1,2,3,4,5,6,7] == 4
        assert moyenne([1,2]) == 1.5
        ```

    === "Sujet 10 : Exercice 2"
        La fonction `fusion` prend deux listes `L1`, `L2` d’entiers triées par ordre croissant et les fusionne en une liste triée `L12` qu’elle renvoie.

        Le code Python de la fonction est

        ```python linenums='1'
        def fusion(L1,L2):
            n1 = len(L1)
            n2 = len(L2)
            L12 = [0]*(n1+n2)
            i1 = 0
            i2 = 0
            i = 0
            while i1 < n1 and ... :
                if L1[i1] < L2[i2]:
                    L12[i] = ...
                    i1 = ...
                else:
                    L12[i] = L2[i2]
                    i2 = ...
                i += 1
            while i1 < n1:
                L12[i] = ...
                i1 = i1 + 1
                i = ...
            while i2 < n2:
                L12[i] = ...
                i2 = i2 + 1
                i = ...
            return L12
        ```

        Compléter le code.

        Exemple :  
        ```python
        >>> fusion([1,6,10],[0,7,8,9])
        [0, 1, 6, 7, 8, 9, 10]
        ```
    === "Sujet 27 : Exercice 1"
        On considère l'algorithme de tri de tableau suivant : à chaque étape, on parcourt depuis le début du tableau tous les éléments non rangés et on place en dernière position le plus grand élément.

        Exemple avec le tableau : ```t = [41, 55, 21, 18, 12, 6, 25]```

        - Étape 1 : on parcourt tous les éléments du tableau, on permute le plus grand élément avec le dernier.

        Le tableau devient `t = [41, 25, 21, 18, 12, 6, 55]`

        - Étape 2 : on parcourt tous les éléments **sauf le dernier**, on permute le plus grand élément trouvé avec l'avant dernier.

        Le tableau devient : ```t = [6, 25, 21, 18, 12, 41, 55]```

        Et ainsi de suite. La code de la fonction `tri_iteratif` qui implémente cet algorithme est donné ci-
        dessous.

        ```python linenums='1'
        def tri_iteratif(tab):
            for k in range(..., 0 ,-1):
                imax = ...
                for i in range(0, ...):
                    if tab[i] > ... :
                        imax = i
                if tab[max] > ... :
                    ..., tab[imax] = tab[imax], ...
            return tab
        ```

        Compléter le code qui doit donner :

        ```python
        >>> tri_iteratif([41, 55, 21, 18, 12, 6, 25])
        [6, 12, 18, 21, 25, 41, 55]
        ```

        On rappelle que l'instruction ```a, b = b, a``` échange les contenus de ```a``` et ```b```.

    === "Sujet 19 : Exercice 2"
        Soit `T` un tableau non vide d'entiers triés dans l'ordre croissant et `n` un entier.  
        La fonction `chercher`, donnée à la page suivante, doit renvoyer un indice où la valeur `n` apparaît éventuellement dans `T`, et `None` sinon.

        Les paramètres de la fonction sont :

        - `T`, le tableau dans lequel s'effectue la recherche ;  
        - `n`, l'entier à chercher dans le tableau ;  
        - `i`, l'indice de début de la partie du tableau où s'effectue la recherche ;  
        - `j`, l'indice de fin de la partie du tableau où s'effectue la recherche.  

        La fonction `chercher` est une fonction récursive basée sur le principe « diviser pour régner ».

        Le code de la fonction commence par vérifier si `0 <= i` et `j < len(T)`.  
        Si cette condition n’est pas vérifiée, elle affiche `"Erreur"` puis renvoie `None`.

        Recopier et compléter le code de la fonction `chercher` proposée ci-dessous :

        ```python linenums='1'
        def chercher(T, n, i, j):
            if i < 0 or ??? :
                print("Erreur")
                return None
            if i > j :
                return None
            m = (i + j) // ???
            if T[m] < ??? :
                return chercher(T, n, ??? , ???)
            elif ??? :
                return chercher(T, n, ??? , ??? )
            else :
                return ???
        ```

        L'exécution du code doit donner :  

        ```python
        >>> chercher([1,5,6,6,9,12],7,0,10)
        Erreur
        >>> chercher([1,5,6,6,9,12],7,0,5)
        >>> chercher([1,5,6,6,9,12],9,0,5)
        4
        >>> chercher([1,5,6,6,9,12],6,0,5)
        2
        ```


    
!!! exo "Inversions dans une liste : extrait BAC"
*Cet exercice est extrait  d'un sujet de {{sc("bac")}} de la session 2021*

Dans un tableau Python d'entiers `tab`, on dit que le couple d'indice `(i,j)` forme une inversion lorsque `i<j` et `tab[i]>tab[j]`. On donne ci-dessous quelques exemples.

* Dans le tableau `[1,5,3,7]` le couple d'indices `(1,2)` forme une inversion car `5>3`. Par contre, le couple  `(1,3)` ne forme pas d'inversion car `5<7`.<br>
Il n'y a qu'une inversion dans ce tableau
* Il y a trois inversions sans le tableau `[1,6,2,7,3]`, à savoir les couples d'indices `(1,2)`, `(1,4)` et `(3,4)`.
* On peut compter six inversions dans le tableau `[7,6,5,3]` : les couples d'indices `(0,1), (0,2), (0,3), (1,2), (1,3)` et `(2,3)`.
On se propose dans cet exercice de déterminer le nombre d'inversions dans un tableau quelconque

#### Questions préliminaires
1. Expliquer pourquoi le couple `(1,3)` est une inversion dans le tableau `[4,8,3,7]`.
2. Justifier que le couple `(2,3)` n'en est pas une.

#### Partie A : Méthode itérative
Le but de cette partie est d'ecrire une fonction itérative `nombre_inversion` qui renvoie le nombre d'inversions dans un tableau. Pour cela, on commence par écrire une fonction `fonction1` qui sera ensuite utilisé pour écrire la fonction `nombre_inversion`.

1. On donne la fonction suivante.

    ```python
        def fonction1(tab, i):
            nb_elem = len(tab)
            cpt = 0
            for j in range(i+1, nb_elem):
            if tab[j] < tab[i]:
            cpt += 1
            return cpt
    ```

    1. Indiquer ce que renvoie la `fonction1(tab,i)` dans les cas suivants :
        
        * Cas n°1 : `tab=[1,5,3,7]` et `i=0`
        * Cas n°2 : `tab=[1,5,3,7]` et `i=1`
        * Cas n°3 : `tab=[1,5,2,6,4]` et `i=1`
    
    2. Expliquer ce que permet de déterminer cette fonction.

2. En utilisant la fonction précédente, écrire une fonction `nombre_inversion(tab)` qui prend en argument un tableau et renvoie le nombre d’inversions dans ce tableau. On donne ci-dessous les résultats attendus pour certains appels.
    ```python
    >>> nombre_inversions([1,5,7])
    0
    >>> nombre_inversions([1,6,7,2,3])
    3
    >>> nombre_inversions([7,6,5,3])
    6
    ```
3. Quelle est l’ordre de grandeur de la complexité en temps de l'algorithme obtenu ? Aucune justification n'est attendue.

#### Partie B : Méthode récursive

Le but de cette partie est de concevoir une version récursive de la fonction `nombre_inverion`. On définit pour cela des fonctions auxiliaires.

1. Donner le nom d'un algorithme de tri ayant une complexité meilleure que quadratique.
Dans la suite de cet exercice, on suppose qu’on dispose d'une fonction `tri(tab)` qui prend en argument un tableau et renvoie un tableau contenant les mêmes éléments rangés dans l'ordre croissant.

2. Écrire une fonction `moitie_gauche(tab)` qui prend en argument un tableau tab et renvoie un nouveau tableau contenant la moitié gauche de tab. Si le nombre d'éléments de tab est impair, l'élément du centre se trouve dans cette partie gauche. On donne ci-dessous les résultats attendus pour certains appels.

    ```python
        >>> moitie_gauche([])
        []
        >>> moitie_gauche([4, 8, 3])
        [4,8]
        >>> moitie_gauche ([4, 8, 3, 7])
        [4,8]
    ```
Dans la suite, on suppose qu’on dispose de la fonction moitie_droite(tab) qui renvoie la moitié droite sans l’élément du milieu.

3. On suppose qu’une fonction `nb_inv_tab(tab1, tab2)` a été écrite. Cette fonction renvoie le nombre d’inversions du tableau obtenu en mettant bout à bout les tableaux `tab1` et `tab2`, à condition que `tab1` et `tab2` soient triés dans l’ordre croissant. On donne ci-dessous deux exemples d’appel de cette fonction :

    ```python
        >>> nb_inv_tab([3,7,9],[2,10])
        3
        >>> nb_inv_tab([7,9,13],[7,10,14])
        3
    ```
En utilisant la fonction `nb_inv_tab` et les questions précédentes, écrire une fonction récursive `nb_inversions_rec(tab)` qui permet de calculer le nombre d'inversions dans un tableau. Cette fonction renverra le même nombre que `nombre_inversions(tab)` de la partie A. On procédera de la façon suivante :
    
    * Séparer le tableau en deux tableaux de tailles égales (à une unité près).
    * Appeler récursivement la fonction `nb_inversions_rec` pour compter le nombre d’inversions dans chacun des deux tableaux.
    * Trier les deux tableaux (on rappelle qu'une fonction de tri est déjà définie).
    * Ajouter au nombre d'inversions précédemment comptées le nombre renvoyé par la fonction `nb_inv_tab` avec pour arguments les deux tableaux triés.


!!! exo "Quart de tour d'une image"

1. Pour faire tourner une image carré de côté $2^n$ pixels d'un quart de tour à gauche, on propose la méthode suivante :
    
    * Diviser l'image en quatre quarts Q1,Q2,Q3,Q4 <br>
     ![qquarts1](../images/C8/qquart1.png){width=200}
    * Faire tourner chacun des quarts d'un quart de tour à gauche <br>
     ![qquarts2](../images/C8/qquart2.png){width=200}
    * Permuter chaque quart afin de le placer correctement <br>
     ![qquarts3](../images/C8/qquart3.png){width=200}
    
    Expliquer pourquoi cette méthode est une illustration de la technique diviser pour régner.

2. C'est algorithme est-il du type itératif ou récursif ? Justifier.
3. Découpage de l'image en quatres quarts à l'aide du module {{sc("pil")}} de manipulation d'images
    1. On a représenté une image carré de $n$ pixels de côté avec le système de coordonnées d'une image dans le module {{ sc("pil")}}. Quelles sont les coordonnées manquantes ? <br>
    ![coordonnees](./images/C8/coordonnees.png){width=300}
    2. La méthode `crop` du module {{ sc("pil")}} permet d'extraire une portion rectangulaire d'une image en donnant les coordonnées des coins supérieur gauche et inférieur droit du rectangle. Compléter la fonction Python suivante qui prend en entrée une image et retourne les quatre quarts de cette image.

        ```python
            from PIL import Image
            def partage_quart(image):
                n = image.width
                if n > 1:
                    q1 = image.crop((0,0,n//2,n//2))
                    q2 = image.crop((...,...,...,...))
                    q3 = image.crop((...,...,...,...))
                    q4 = image.crop((...,...,...,...))
                    return q1,q2,q3,q4
        ```

    3. Tester cette fonction (on pourra utiliser [cette image carré](./images/C8/carre.jpg))

        !!! aide
            * La création d'une image dans {{ sc("pil")}} à partir d'un fichier s'effectue à l'aide de :
            ```python
                img_test = Image.open("mettre ici le nom du fichier")
            ```
            * La visualisation d'une image s'effectue à l'aide de :
            ```python
                img_test.show()
            ```

    4. Ajouter une instruction `assert` permettant de vérifier que l'image est carré (c'est à dire `image.width==image.height`)
    5. Ajouter une instruction `assert` permettant de vérifier que `n` est pair.

4. Compléter puis tester la fonction python qui implémente l'algorithme décrit à la question 1.
```python
    def quart_tour(image):
        n = image.width
        # Partage de l'image en quatre quarts
        if n>1:
            q1,q2,q3,q4 = partage_quart(image)
            # Rotation de chacun des quarts
            rq1 = quart_tour(q1)
            rq2 = quart_tour(q2)
            rq3 = quart_tour(q3)
            rq4 = quart_tour(q4)
            # Reconstruction de l'image
            resultat = Image.new('RGB',image.size)
            resultat.paste(rq2,(0,0))
            resultat.paste(...,(n//2,0))
            resultat.paste(rq1,(...,...))
            resultat.paste(...,(...,...))
            return resultat
        else:
            return image
```
