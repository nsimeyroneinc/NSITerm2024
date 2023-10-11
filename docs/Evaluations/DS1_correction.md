# Devoir n°1 : SQL sur table

## Enoncé 

{{telecharger("Devoir n°1 : SQL","../pdf/eval/DS1.pdf")}}

## Correction 

### Exercice n°1


1.  a. La requête va renvoyer : 

    | age | taille | poids |  
    |:---:|:---:|:---:|  
    |6|1.70|100|  

    b. 
    ```sql
    SELECT nom,age
    FROM animal
    WHERE nom_espece='bonodo'
    ```

2.  a. La clé primaire est nom_espece car elle est unique.  
    num_enclos est une clé étrangère pour faire le lien avec la table enclos.

    b.  

3.  a. 
    ```sql
    UPDATE espece
    SET classe'mammifère'
    WHERE nom_espece='ornithorynque'
    ```

    b. 
    ```sql
    INSERT INTO animal VALUES (179,'Serge',1,0.80,30,'lama')
    ```

4.  a. 
    ```sql
    SELECT animal.nom,animal.nom_espece
    FROM animal
    JOIN espece ON espece.nom_espece = animal.nom_espece
    JOIN enclos ON enclos.num_enclos = espece.num_enclos
    WHERE enclos.struct = 'vivarium' and espece.alimentation='carnivore'
    ```

    b.  
    ```sql
    SELECT COUNT(*)
    FROM animal
    JOIN espece ON espece.nom_espece = animal.nom_espece
    WHERE espece.classe='oiseaux'
    ```


### Exercice n°2


1. 
    a. La table contient déjà une entrée dont l'attribut id_equipe vaut 11. Comme il s'agit de la clé primaire cela provoque une erreur. C’est
la contrainte d’unicité

    b. L'attribut telephone est une chaine de caractère limité à 20. On ne pouvait pas choisir des entiers car les numeros de téléphone commençant par 0 il disparaitrait ainsi les espaces entre chaque paire de chiﬀres.

    c.  

    | . | . | . |
    |:---: | :---: | :---:|
    |Lyon | 451 cours d'Emile Zola,69100 Villeurbanne |04 05 06 07 08|
    
    d. La requête le nombre d'entrée dans la table `equipe`   
    Cette requête renvoie 12. Elle renvoie le nombre d’entités dans la relation Equipe.

    e. 
    ```sql
    SELECT nom
    FROM Equipe
    ORDER BY noms;
    ```

    f. 
    ```sql
    UPDATE Equipe
    SET nom='Tarbes'
    WHERE id_equipe=4;
    ```

2.  a. L'attribut `id_equipe` a été déclaré clé étrangère de la relation `Joueuse` pour référence à la clé primaire `id_equipe` de la table `Equipe`.  

    b. On ne peut pas supprimer directement l’équipe dans la relation Equipe car certaines entités de la relation Joueuse font référence à cette équipe : c’est la contrainte de référence.

    c. 
    ```sql
    SELECT Joueuse.nom, Joueuse.prenom
    FROM Joueuse
    JOIN Equipe ON Equipe.id_equipe=Joueuse.id_equipe
    WHERE Equipe.nom='Angers'
    ORDER BY Joueuse.nom;
    ```

3.  a. On peut proposer le schéma relationnel suivant : 
    {{relation("Match","id_match : INT", "date : DATE", "#id_equipe_domicile : INT", "#id_equipe_deplacement : INT","score_domicile : INT","score_deplacement : INT") }}
    
    \#id_equipe_domicile et #id_equipe_deplacement sont des clés étrangères qui font référence à la relation Equipe. 

    b.
    ```sql
    INSERT INTO Match VALUES (10, "23/10/2021", 3, 6, 73, 78) ;
    ```

4. a. On peut proposer le schéma relationnel suivant :
    {{ relation("Statistiques","id_stats : INT", "#id_joueuse : INT", "#id_match : INT","points : INT","passes_decisives : INT") }}

    b.
    ```sql
    SELECT Equipe.nom, Joueuse.nom, Joueuse.prenom, Statistiques.points, Statistiques.rebonds, Statistiques.passes_decisives
    FROM Statistiques
    JOIN Joueuse ON Joueuse.id_joueuse = Statistiques.id_joueuse
    JOIN Equipe ON Joueuse.id_equipe = Equipe.id_equipe
    WHERE Statistiques.id_match = 53 ;
    ```