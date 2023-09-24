{% set num = 2 %}
{% set titre = "Memento SQL"%}
{% set theme = "db" %}
{% set niveau = "terminale"%}

{{ titre_chapitre(num,titre,theme,niveau)}}

# Memento `SQL`

Ce document n'a pas la vocation d'être exhaustif. On pourra se référer à [ce site](https://sql.sh) afin de le compléter et avoir plus de détails.

Dans certains *dialectes* `SQL`, les points-virgules en fin de ligne sont indispensables même s'il n'y a qu'une seule instruction. Bien que n'utilisions ici que des instructions uniques, on écrit tout de même les points-virgules en fin de ligne.

## Liens directs :

* [Création d'une base de données](memento_sql.md#creation-dune-base-de-donnees)
  
* [Création de tables](memento_sql.md#creation-de-tables)

* [Afficher toute une table](memento_sql.md#afficher-toute-une-table)
  
* [Effacer une base, une table](memento_sql.md#effacer-une-base-une-table)

* [Insertion de valeurs](memento_sql.md#insertion-de-valeurs)

* [Suppression de valeurs](memento_sql.md#suppression-de-valeurs)

* [Mise à jour de valeurs](memento_sql.md#mise-a-jour-de-valeurs)

* [Sélections](memento_sql.md#selections)


## Création d'une base de données

* La base n'existe pas :

    ```sql
    CREATE DATABASE ma_base;
    ```

* Au cas où la base existe et que l'on ne souhaite pas l'écraser :

    ```sql
    CREATE DATABASE IF NOT EXISTS ma_base;
    ```

## Création de tables

* Cas de base :

    ```sql
    CREATE TABLE ma_table (
        attribut_1 INTEGER PRIMARY KEY AUTOINCREMENT,
        attribut_2 TEXT,
        attribut_3 VARCHAR(50)
    );
    ```

    Là encore on peut ajouter l'argument `IF NOT EXISTS`.

* Clé primaire multiple :

    ```sql
    CREATE TABLE ma_table (
        attribut_1 INTEGER,
        attribut_2 TEXT,
        attribut_3 VARCHAR(50),
        PRIMARY KEY (attribut_1, attribut_2)
    );
    ```

* Clé étrangère :

    ```sql
    CREATE TABLE ma_table (
        attribut_1 INTEGER PRIMARY KEY AUTOINCREMENT,
        attribut_2 TEXT,
        attribut_3 VARCHAR(50),
        FOREIGN KEY (attribut_1) REFERENCES autre_table (attribut_de_reference)
    );
    ```

## Afficher toute une table

* On effectue une requête :

    ```sql
    SELECT *
    FROM ma_table;
    ```

## Effacer une base, une table

* Une base :
  
    ```sql
    DROP DATABASE ma_base;
    ```

* Une table :

    ```sql
    DROP TABLE ma_table;
    ```

## Insertion de valeurs

* On renseigne touts les attributs dans l'ordre de leur création :

    ```sql
    INSERT INTO ma_table
    VALUES (valeur_1, valeur_2, valeur_3);
    ```

* On ne renseigne que les attributs cités dans l'ordre souhaité :

    ```sql
    INSERT INTO ma_table (attribut_3, attribut_1)
    VALUES (valeur_3, valeur_1);
    ```

* Insertion de plusieurs lignes :

    ```sql
    INSERT INTO ma_table (attribut_3, attribut_1)
    VALUES 
    (valeur_3_1, valeur_1_1),
    (valeur_3_2, valeur_1_2),
    (valeur_3_3, valeur_1_3);
    ```

## Suppression de valeurs

* On supprime des entrées, des lignes, en précisant une condition (ici les entrées dont l'`attribut_1` vaut `8`) :

    ```sql
    DELETE FROM ma_table
    WHERE attribut_1 = 8;
    ```

## Mise à jour de valeurs

* Modification de la valeur pour **toutes** les lignes d'une table :

    ```sql
    UPDATE ma_table
    SET attribut_1 = valeur_1;
    ```

* Modification de la valeur en posant une condition :

    ```sql
    UPDATE ma_table
    SET attribut_1 = valeur_1
    WHERE condition;
    ```

## Sélections

### Cas de base

* Tous les attributs :

    ```sql
    SELECT *
    FROM ma_table;
    ```

* Seulement certains attributs :

    ```sql
    SELECT attribut_1, attribut_3
    FROM ma_table;
    ```

* Avec une condition :

    ```sql
    SELECT attribut_1, attribut_3
    FROM ma_table
    WHERE attribut_2 = valeur_2;
    ```

    On peut utiliser les opérateurs `=` (attention, un seul symbole contrairement au `==` de Python), `<>` (plusieurs systèmes de gestion de BDD acceptent aussi `!=`), `>`, `<`, `>=`, `<=`, `AND`, `OR`.

* Les chaînes de caractères :

    L'usage veut que l'on délimite les chaînes de caractères par des guillemets simples : `'chaine'`. Les guillemets
    doubles sont réservés aux noms de tables, d'attributs : `"attribut_1" = 'chaine'`. Dans les faits, **cela ne change pas grand chose** !

    En cas de stricte égalité :

    ```sql
    SELECT attribut_1, attribut_3
    FROM ma_table
    WHERE attribut_2 = 'chat'
    ```

    Si l'on cherche les chaînes débutant par `'chat'` (`chat`, `chatte`, `chaton`...):
    
    ```sql
    SELECT attribut_1, attribut_3
    FROM ma_table
    WHERE attribut_2 LIKE 'chat%'
    ```
    
    Si l'on cherche les chaînes se terminant par `'chat'` (`achat`, `le chat`...):
    
    ```sql
    SELECT attribut_1, attribut_3
    FROM ma_table
    WHERE attribut_2 LIKE '%chat'
    ```

### Fonctions d'agrégation

* Compter les lignes vérifiant une condition :

    ```sql
    SELECT COUNT(*)
    FROM ma_table
    WHERE condition;
    ```

* Regrouper toutes les lignes selon la valeur d'un attribut :

    ```sql
    SELECT COUNT(*)
    FROM ma_table
    WHERE condition
    GROUP BY attribut_1;
    ```

* La maximum d'un attribut :

    ```sql
    SELECT MAX(attribut_1)
    FROM ma_table
    WHERE condition;
    ```

    Il existe aussi la fonction `MIN`.

* La somme d'un attribut :

    ```sql
    SELECT SUM(attribut_1)
    FROM ma_table
    WHERE condition;
    ```

* La moyenne d'un attribut :

    ```sql
    SELECT AVG(attribut_1)
    FROM ma_table
    WHERE condition;
    ```

* Trier les données :

    ```sql
    SELECT attribut_1
    FROM ma_table
    WHERE condition
    ORDER BY attribut_2 ASC;
    ```

    `ASC` pour `ASCENDING` et l'ordre croissant. Utiliser `DESC` pour l'ordre décroissant.

* N'afficher que les 10 premiers résultats :

    ```sql
    SELECT attribut_1
    FROM ma_table
    WHERE condition
    LIMIT 10;
    ```

### Jointures

* Mettre en correspondance plusieurs tables grâce aux clés étrangères :

    ```sql
    SELECT table_1.attribut_1, table_2.attribut_3
    FROM table_1
    JOIN table_2 ON table_1.attribut_1 = table_2.attribut_de_reference
    JOIN table_3 ON table_2.attribut_2 = table_3.attribut_de_reference;
    ```

    On précise à quelles tables appartiennent les attributs afin de lever les ambiguïtés si deux tables ont des attributs portant le même nom.