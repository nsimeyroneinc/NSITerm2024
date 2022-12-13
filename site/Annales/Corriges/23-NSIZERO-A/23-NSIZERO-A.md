hide: - navigation  in docs.md

{% set repere_sujet = "23-NSIZERO-A" %}

{{ corrige_sujetbac(repere_sujet) }}


{{ corrige_exobac(repere_sujet,1) }}

1. Les attributs de la table `groupes` sont `idgrp`, `nom`, `style` et `nb_pers`.

2. L'attribut `nom` de la table `musiciens` ne peut pas être une clé primaire car plusieurs musiciens peuvent porter le même nom, or une clé primaire doit identifier de façon unique un enregistrement.

3. Cette requête renvoie la colonne `nom` de la table `groupes` lorsque le style du groupe est `'Latin Jazz'`. Sur l'extrait fourni, on obtient donc :

| nom |
|-----|
|`'Weather Report'`|
|`'Return to Forever'`|

4. 
```sql
UPDATE concerts
SET heure_fin = '22h30'
WHERE idconc = 36;
```

5. Pour récupérer le nom de tous les groupes qui jouent sur la scène 1 :
```sql
SELECT groupes.nom
FROM groupes 
JOIN concerts ON groupes.idgrp = concerts.idgrp
WHERE concerts.scene = 1
```

6. 
```sql
INSERT INTO groupes
VALUES 15,'Smooth Jazz Fourplay','Free Jazz',4
```

7. 
```python
def recherche_nom(musiciens):
    au_moins_4_concerts = []
    for musicien in musiciens:
        if musicien['nb_concerts']>=4:
            au_moins_4_concerts.append(musicien['nom'])
    return au_moins_4_concerts
```


{{ corrige_exobac(repere_sujet,2) }}

1. L'adresse réseau  de la configuration d'Alice est `172.16.2.0/24`, donc tous les ordinateurs de cette configuration ont une adresse IP qui commence par les 24 même premiers bits (i.e. les 3 premiers octets) : `172.16.2`. Cette configuration appartient donc à l'ordinateur d'Alice.

2. On applique la formule donnée dans l'énoncé avec un débit du réseau de $1\,000$ Mbits/s :
$\textnormal{cout} = \dfrac{10\,000}{1\,000} = 10$
Le cout du réseau WAN8 est donc 10.

3. Voici la table du routeur R6 :

| Destination | Pass. | Cout |
|-------------|-------|------|
|LAN 1        |  R5   |  21  |
|LAN 2        |  -    |  -   |
|WAN 1        |  R5   |  11  |
|WAN 2        |  R5   |  20  |
|WAN 3        |  R5   |  11  |
|WAN 4        |  R5   |  12  |
|WAN 5        |  R5   |  10  |
|WAN 6        |  -    |  -   |
|WAN 7        |  -    |  -   |
|WAN 8        |  R5   |  10  |

4. Les routeurs traversés seront : {{ route(['R6','R5','R2','R1']) }}

5. Le routeur en panne est le routeur `R5` (car la nouvelle route est alors {{route(['R6','R4','R2','R1'])}} dont le coût est bien 111.)


{{ corrige_exobac(repere_sujet,3) }}

1. Ce fonctionnement traduit le comportement d'une **file** c'est à dire que le premier élément qui entre dans la structure de données est aussi le premier à en sortir (*FIFO* pour *First In, First Out*). Dans une pile, la dernier élément entré est le premier à sortir (*LIFO* pour *Last In, First Out*)

2.  a. C'est la **taille** de l'arbre (c'est à dire le nombre total de noeuds de l'arbre)

    b. C'est la **racine** de l'arbre puisqu'il s'agit de la tâche ajoutée à l'arbre en premier

    c. C'est une **feuille** de l'arbre aucune tâche n'ayant été ajouté après celle-ci, le noeud représentant cette tâche n'a pas de fils, c'est donc une feuille.

3.  a. Les attributs de la classe `Noeud` sont `tache`, `indice`, `gauche` et `droite`.

    b. La méthode `insere` est récursive car elle s'appelle elle-même. Elle se termine car à chaque appel on descend d'un niveau dans l'arbre.

    c. On insère à gauche lorsque la valeur à insérer est inférieure à celle du noeud courant donc on complète la ligne 26 par :
    ```python
    elif self.racine.indice > nouveau_noeud.indice
    ```

    d. 
    
    * Arbre initial
    ```mermaid
        graph TD
        S12["12"] --> S6["6"]
        S12 --> S14["14"]
        S6 --> V1[" "]
        S6 --> S10["10"]
        S10 --> S8["8"]
        S10 --> V2[" "]
        S14 --> S13["13"]
        S14 --> V3[" "]
        style V1 opacity:0;
        style V2 opacity:0;
        style V3 opacity:0;
        linkStyle 2 stroke:#FFFFFF,stroke-width:0px
        linkStyle 5 stroke:#FFFFFF,stroke-width:0px
        linkStyle 7 stroke:#FFFFFF,stroke-width:0px
    ```

    * Après insertion du 11
    ```mermaid
        graph TD
        S12["12"] --> S6["6"]
        S12 --> S14["14"]
        S6 --> V1[" "]
        S6 --> S10["10"]
        S10 --> S8["8"]
        S10 --> S11["11"]
        S14 --> S13["13"]
        S14 --> V3[" "]
        style V1 opacity:0;
        style V3 opacity:0;
        linkStyle 2 stroke:#FFFFFF,stroke-width:0px
        linkStyle 7 stroke:#FFFFFF,stroke-width:0px
    ```

    * Après insertion du 5
    ```mermaid
        graph TD
        S12["12"] --> S6["6"]
        S12 --> S14["14"]
        S6 --> S5["5"]
        S6 --> S10["10"]
        S10 --> S8["8"]
        S10 --> S11["11"]
        S14 --> S13["13"]
        S14 --> V3[" "]
        style V3 opacity:0;
        linkStyle 7 stroke:#FFFFFF,stroke-width:0px
    ```

    * Après insertion du 16
    ```mermaid
        graph TD
        S12["12"] --> S6["6"]
        S12 --> S14["14"]
        S6 --> S5["5"]
        S6 --> S10["10"]
        S10 --> S8["8"]
        S10 --> S11["11"]
        S14 --> S13["13"]
        S14 --> S16["16"]
    ```

    * Après insertion du 7
    ```mermaid
        graph TD
        S12["12"] --> S6["6"]
        S12 --> S14["14"]
        S6 --> S5["5"]
        S6 --> S10["10"]
        S10 --> S8["8"]
        S10 --> S11["11"]
        S14 --> S13["13"]
        S14 --> S16["16"]
        S8 --> S7["7"]
        S8 --> V1[" "]
        style V1 opacity:0;
        linkStyle 9 stroke:#FFFFFF,stroke-width:0px
    ```
4. 
```python linenums='41'
def est_present(self,indice_recherche):
    """renvoie True si l'indice de priorité indice_recherche (int) passé en paramètre est déjà l'indice d'un noeud de l'abre, False sinon"""
    if self.racine == None:
        return False
    else:
        if self.racine.indice == indice_recherche:
            return True
        elif self.racine.indice > indice_recherche:
            return self.racine.gauche.est_present()
        else:
            return self.racine.droite.est_present()
```

5.  a. On rappelle que dans un parcours *infixe*, on parcourt le sous arbre gauche, puis la racine, puis le sous arbre droit. Dans le cas de l'arbre de la figure 1, on obtient : {{ route(["6","8","10","12","13","14"]) }}

    b. La tâche la plus prioritaire sera le premier élément rencontré lors de ce parcours.

6. 
```python linenums="1"
def tache_prioritaire(self):
    """renvoie la tache du noeud situé le plus à gauche de l'ABR supposé non vide"""
    if self.racine.gauche.est_vide():
        return self.racine.tache
    else:
        return self.racine.gauche.tache_prioritaire()
```

7.  

    * Etape 1 : tâche d'indice 14 à accomplir
    ```mermaid
        graph TD
        S14["14"]
    ```

    * Etape 2 : tâche d'indice 11 à accomplir
    ```mermaid
        graph TD
        S14["14"] --> S11["11"]
        S14 --> V1[" "]
        style V1 opacity:0;
        linkStyle 1 stroke:#FFFFFF,stroke-width:0px
    ```

    * Etape 3 : tâche d'indice 8 à accomplir
    ```mermaid
        graph TD
        S14["14"] --> S11["11"]
        S14 --> V1[" "]
        S11 --> S8["8"]
        S11 --> V2[" "]
        style V1 opacity:0;
        style V2 opacity:0;
        linkStyle 1 stroke:#FFFFFF,stroke-width:0px
        linkStyle 3 stroke:#FFFFFF,stroke-width:0px
    ```

    * Etape 4 : accomplir la tâche prioritaire (8) 
    ```mermaid
        graph TD
        S14["14"] --> S11["11"]
        S14 --> V1[" "]
        style V1 opacity:0;
        linkStyle 1 stroke:#FFFFFF,stroke-width:0px
    ```

    * Etape 5 : tâche d'indice 12 à accomplir
    ```mermaid
        graph TD
        S14["14"] --> S11["11"]
        S14 --> V1[" "]
        S11 --> V2[" "]
        S11 --> S12["12"]
        style V1 opacity:0;
        style V2 opacity:0;
        linkStyle 1 stroke:#FFFFFF,stroke-width:0px
        linkStyle 2 stroke:#FFFFFF,stroke-width:0px
    ```

    * Etape 6 : accomplir la tâche prioritaire (11) 
    ```mermaid
        graph TD
        S14["14"] --> S12["12"]
        S14 --> V1[" "]
        style V1 opacity:0;
        linkStyle 1 stroke:#FFFFFF,stroke-width:0px
    ```

    * Etape 7 : accomplir la tâche prioritaire (12) 
    ```mermaid
        graph TD
        S14["14"]
    ```

    * Etape 8 : tâche d'indice 15 à accomplir
    ```mermaid
        graph TD
        S14["14"] --> V1[" "]
        S14 --> S15["15"]
        style V1 opacity:0;
        linkStyle 0 stroke:#FFFFFF,stroke-width:0px
    ```

    * Etape 9 : tâche d'indice 19 à accomplir
    ```mermaid
        graph TD
        S14["14"] --> V1[" "]
        S14 --> S15["15"]
        S15 --> V2[" "]
        S15 --> S19["19"]
        style V1 opacity:0;
        linkStyle 0 stroke:#FFFFFF,stroke-width:0px
        style V2 opacity:0;
        linkStyle 2 stroke:#FFFFFF,stroke-width:0px
    ```

    * Etape 10 : accomplir la tâche prioritaire (14)
    ```mermaid
        graph TD
        S15["15"] --> V1[" "]
        S15 --> S19["19"]
        style V1 opacity:0;
        linkStyle 0 stroke:#FFFFFF,stroke-width:0px
    ```