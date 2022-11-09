hide: - navigation  in docs.md

{% set repere_sujet = "22-NSIJ2JA1" %}

{{ corrige_sujetbac(repere_sujet) }}



{{ corrige_exobac(repere_sujet,1) }}

1.  a. La première ligne du terminale `gestion@capNSI-ordinateur_central` affiche le nom de l'utilisateur et le nom du terminal séparés par le caractère `@`. Ici, le nom d'utilisateur est donc `gestion` et le nom d'ordinateur `capNSI-ordinateur_central`

    b. On utilise la commande `ls` en donnant le répertoire concerné ` ls Contrats`


2.  a. `mkdir Contrats/TURING_Alan`
    b. `chmod ug=rwx, o=r Contrats/TURING_Alan` 


3. 
```python
    def formatage(tab):
        liste_noms = []
        for (nom,prenom) in tab:
            liste_noms.append(nom + "_" + prenom)
        return liste_noms
```

4.  
```python
    def creation_dossiers(tab):
        for nom in tab:
            rep = "Contrats/" + nom
            os.mkdir(repertoire)
            os.chmod(rep,774)
```
            

{{ corrige_exobac(repere_sujet,2) }}

{{ corrige_exobac(repere_sujet,3) }}

{{ corrige_exobac(repere_sujet,4) }}

{{ corrige_exobac(repere_sujet,5) }}

1.  Les valeurs successives prises par la variable `i` seront `0,1, ...,n-1`. La première valeur provoque donc une erreur de division par 0. La dernière valeur n'est pas non plus correcte puisqu'on doit calculer la somme des inverses jusqu'à `n`. On peut corriger des deux façons suivantes :
    * A la ligne 3 : `for i range(1,n+1)` afin de démarrer à 1 et d'aller jusqu'à n
    * ou alors à la ligne 4 : `total = total + 1\(i+1)` 

2.  a. La variable `indice` atteint la valeur `len(L)` or les indices  des éléments d'une liste vont jusqu'à `len(L)-1`. Pour corriger ce problème on remplace la ligne 3 par `while indice <len(L)`

    b. L'appel `maxi([-2,-7,-3])` renvoie `0` puisque le maximum est initialisé à 0 et aucun élément plus grand que 0 n'est trouvé lorsqu'on parcourt la liste. Pour corriger ce problème, on peut initialiser le maximum avec le premier élément de la liste et donc écrire à la ligne 3 : `maximum = L[0]`

3.  On peut pas ajouter une variable de type `str` avec une variable de type `int`. La ligne 4 provoque donc une erreur car `Joueur ` est du type `str` et `i` est du type `int`. Pour corriger ce problème, il faut convertir `i` en `str` et donc écrire ligne 4 : `L.append('Joueur ' + str(i))`

4.  a. Pour calculer `suite(6)`, on fait les appels successifs à `suite(4)` puis `suite(2)` puis `suite(0)`. La condition d'arrêt renvoie `0` comme valeur de `suite(0)` on remonte alors et on calcule :
    * `suite(2) = 3+2*suite(0) = 3`
    * `suite(4) = 3+2*suite(2) = 9`
    * `suite(6) = 3+2*suite(4) = 21`

L'appel de `suite(6)` renvoie donc 21.

    b. On obtient une erreur de profondeur de récursion, en effet la condition d'arrêt n'est jamais atteinte puisque les appels successifs se feront avec les valeurs suivants de `n` : `7, 5, 3, 1, -1, -3, -5, ....`.

5. La variable `x` est de type `int` donc *non mutable* alors que `L` est de type liste donc *mutable*. Par conséquent, `L` est modifiée lorsque passé en paramètre à une fonction mais pas `x`. Le premier print affichera donc `(5, [10])` et le second `4 [10]`. En effet le premier print affiche le tuple renvoyé par la fonction `modif` et le second print la valeur non modifiée de `x` suivie de celle de `L`.




