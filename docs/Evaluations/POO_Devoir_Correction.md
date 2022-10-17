---
title : Thème 1 - Structure de données
subtitle: P.O.O
subsubtitle: Terminale NSI
author : M.Meyroneinc-Condy
numbersections: true
fontsize: 10pt
geometry:
- top=20mm
- left=20mm
- right=20mm
- heightrounded    
--- 

P.O.O : Devoir n°2
===

<table  class="redTable">
        <tr >
            <th  class="redTh";width="100%"; style="text-align:center;border:none;font-size:15pt;">Thème 1 - Structure de données</th>
        </tr>
</table>
<br>

<table  class="redTable">
        <tr >
            <th width="20%"; style="background-color: #3B444B;color:white;text-align:center;border:none;font-size:40pt;">
            Eval.
            </th>
            <th  class="redTh";width="80%"; style="text-align:center;border:none;font-size:25pt;">P.O.O</th>
        </tr>
</table>
<br>



## D'après 2021, Centres étrangers, J1, Ex. 1

Dans cet exercice, on étudie une méthode de chiffrement de chaines de caractères
alphabétiques. Pour des raisons historiques, cette méthode de chiffrement
est appelée « code de César ». On considère que les messages ne contiennent
que les lettres capitales de l’alphabet "ABCDEFGHIJKLMNOPQRSTUVWXYZ" et la
méthode de chiffrement utilise un nombre entier fixé appelé la clé de
chiffrement.

**1.** Soit la classe `CodeCesar` définie ci-dessous :

```python
class CodeCesar:
    def __init__(self, cle):
        self.cle = cle

    def decale(self, lettre):
        indice_1 = indice_capitale(lettre)
        indice_2 = indice_1 + self.cle
        if indice_2 >= 26:
            indice_2 = indice_2 - 26
        if indice_2 < 0:
            indice_2 = indice_2 + 26
        nouvelle_lettre = lettre_capitale(indice_2)
        return nouvelle_lettre
```
On dispose aussi des fonctions `indice_capitale(indice)` et
`lettre_capitale(lettre)` qui renvoient la lettre majuscule correspondant à
un indice donné et l'indice (la position d'une lettre) dans l'alphabet latin
usuel.

!!! info "Passer d'un indice à une lettre"
    Les fonctions `indice_lettre(indice)` et `lettre_indice (lettre)` peuvent
    être définies par

    ```python
    def indice_capitale(indice: int) -> str:
        assert 0 <= indice < 26, "L'indice doit être entre 0 et 25"
        return chr(ord('A') + indice)

    def lettre_capitale(lettre: str) -> int:
        assert lettre in [chr(i + ord('A')) for i in range(26)], "La lettre doit être dans l'alphabet latin capital"
        return ord(lettre) - ord('A')
    ```

**Représenter** le résultat d’exécution du code Python suivant :

```pycon
>>> code = CodeCesar(3)
>>> code.decale('A')
...
>>> code.decale('X')
...
```

??? done "Réponse"
    La première instruction permet d'initialiser un objet `CodeCesar`
    correspondant à un décalage de 3 caractères. Ainsi `A`, en position 0
    devient la lettre en position 3, c'est à dire `D`. Pour le `X`, si on
    applique le même décalage, on obtiendrai la lettre en position 23+3 =
    26, ce qui ferait échouer la fonction `lettre_indice()`. On soustrait donc 26
    pour trouver `A`.
    
    ```pycon
    >>> code = CodeCesar(3)
    >>> code.decale('A')
    D
    >>> code.decale('X')
    A
    ```

**2.** La méthode de chiffrement du « code de César » consiste à décaler les
lettres du message dans l’alphabet d'un nombre de rangs fixé par la clé.
Par exemple, avec la clé 3, toutes les lettres sont décalées de 3 rangs
vers la droite : le A devient le D, le B devient le E, etc.

**Ajouter** une méthode `chiffre(self, texte)` dans la classe `CodeCesar`
définie à la question précédente, qui reçoit en paramètre une chaîne de
caractères (le message à chiffrer) et qui renvoie une chaîne de
caractères (le message chiffré).

Cette méthode `chiffre(self, texte)` doit chiffrer la chaîne `texte` avec la
clé de l'objet de la classe `CodeCesar` qui a été instanciée.

Exemple :
```pycon
>>> code = CodeCesar(3)
>>> code.chiffre("NSI")
'QVL'
```

??? done "Réponse"
    ```python
    def chiffre(self, texte):
        chaine = ""
        for caractere in texte:
            chaine = chaine + self.decale(caractere)
        return chaine
    ```

**3.** **Écrire** une fonction qui :
* prend en argument la clef de chiffrement et le message à chiffrer ;
* instancie un objet de la classe `CodeCesar` ;
* renvoie le texte chiffré.

??? done "Réponse"
    ```python
    def chiffre_texte(clef, texte):
        return CodeCesar(clef).chiffre(texte)
    ```

**4.** On ajoute la méthode `transforme(texte)` à la classe `CodeCesar` :

```python
def transforme(self, texte):
    self.cle = -self.cle
    message = self.cryptage(texte)
    self.cle = -self.cle
    return message
```
On exécute la ligne suivante dans une console `CodeCesar(10).transforme("PSX")`

**Que va-t-il s'afficher** ? **Expliquer** votre réponse.


??? done "Réponse"
    Le message `'FIN'` va s'afficher sur la console.
    
    La méthode proposée permet de déchiffrer le message en appliquant la
    transformation opposée.
