---
title : Projet
subtitle: Pygame
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

Projet
===

<br>
<table  class="redTable">
        <tr >
            <th width="20%"; style="background-color: #3B444B;color:white;text-align:center;border:none;font-size:40pt;">
            Projet
            </th>
            <th class="redTh"; width="80%"; style="text-align:center;border:none;font-size:25pt;">PPygame</th>
        </tr>
</table>

![](data/logopygame.png)

{{ initexo(0)}}

## Preambule
Pygame est un package de Python facilitant la création de jeux basés une interface graphique. Vous pouvez :

- l'installer sur votre distribution Python, par ```pip3 install pygame```.  
- le tester directement via https://repl.it/, en choisissant ```pygame``` dans la liste des langages proposés.

```python
import pygame, sys
from pygame.locals import *

pygame.init()

#ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
ecran = pygame.display.set_mode((640, 480))
ecran.fill([10,186,181])

continuer = True

while continuer:
    for event in pygame.event.get():
          if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                continuer = False

    pygame.display.flip()

pygame.quit()
```


**Commentaires**

- Durant tout le code, notre scène de travail sera l'objet ```ecran```, dans lequel nous viendrons coller de nouveaux éléments.   

**Éléments structurants d'un code ```pygame``` :**

- ```pygame.init()```  effectue une initialisation globale de tous les modules ```pygame``` importés. À mettre au début du code.  
- ```while continue :``` comme très souvent dans les jeux, la structure essentielle est une boucle infinie dont on ne sortira que par un appui sur la flèche bas où continue passe en `False`.



## Apparition d'un personnage

### Téléchargement de l'image

Nous allons travailler avec le sprite ci-dessous, nommé ```perso.png```. 


![image](data/Paragoomba.png){: .center width=100px}


[Téléchargez-le](https://mario.wiki.gallery/images/thumb/8/8e/ParagoombaNSMBU.png/1200px-ParagoombaNSMBU.png) pour le mettre dans le même dossier que votre code ```pygame```.  A redéfinir avec une bonne dimension.

Vous pouvez trouver sur internet un grand nombre de sprites libres de droits, au format ```png``` (donc gérant la transparence), dans de multiples positions (ce qui permet de simuler des mouvements fluides). Ici nous travaillerons avec un sprite unique.

### Importation de l'image dans la fenêtre

```python
perso = pygame.image.load("Paragoomba.png").convert_alpha()
```
La fonction ```convert_alpha()``` est appelée pour que soit correctement traité le canal de transparence (canal _alpha_) de notre image.

### Affichage de l'image

À ce stade, ```perso``` est un objet ```pygame``` de type ```Surface``` .

Afin de facilement pouvoir le déplacer, nous allons stocker la position de cet objet dans une variable ```position_perso```,  qui sera de type ```rect```. 

```python
position_perso = perso.get_rect()
```
Pour afficher cette image, nous allons venir le superposer aux éléments graphiques déjà dessinés (en l'occurence : rien) avec l'instruction ```blit()``` :

```python
fenetre.blit(perso, position_perso)
```

**▸ récapitulatif du code**

```python
import pygame, sys
from pygame.locals import *

pygame.init()

#ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
ecran = pygame.display.set_mode((640, 480))
ecran.fill([10,186,181])

continuer = True

perso = pygame.image.load("Paragoomba1.png").convert_alpha()
position_perso = perso.get_rect()



while continuer:
    ecran.blit(perso, position_perso)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                continuer = False

    pygame.display.flip()

pygame.quit()
```


## Gestion des évènements  

En informatique, un événement peut être une entrée clavier (soit l’appui soit le relâchement d’une touche), le déplacement de votre souris, un clic (encore une fois, appui ou relâchement, qui seront traités comme deux événements distincts). Un bouton de votre joystick peut aussi engendrer un événement, et même la fermeture de votre fenêtre est considéré comme un événement !

Pour Pygame, un événement est représenté par un type et divers autres attributs que nous allons détailler dans ce chapitre.

De plus, il faut savoir que chaque événement créé est envoyé sur une file (ou queue), en attendant d’être traité. Quand un événement entre dans cette queue, il est placé à la fin de celle-ci. Vous l’aurez donc compris, le premier événement transmis à Pygame sera traité en premier ! Cette notion est très importante, puisque nous allons nous en servir sous peu !

Ce type de queue est dit FIFO.  

### Comment les capturer ?

On utilise le module event de Pygame.

Voici ce que nous dit la documentation à propos de ce module :

??? check "Afficher/Masquer la documentation"
    
    - pygame.event  
    - pygame module for interacting with events and queues  
    - pygame.event.pump — internally process pygame event handlers  
    - pygame.event.get — get events from the queue  
    - pygame.event.poll — get a single event from the queue  
    - pygame.event.wait — wait for a single event from the queue  
    - pygame.event.peek — test if event types are waiting on the queue  
    - pygame.event.clear — remove all events from the queue  
    - pygame.event.event_name — get the string name from and event id  
    - pygame.event.set_blocked — control which events are allowed on the queue  
    - pygame.event.set_allowed — control which events are allowed on the queue  
    - pygame.event.get_blocked — test if a type of event is blocked from the queue  
    - pygame.event.set_grab — control the sharing of input devices with other applications  
    - pygame.event.get_grab — test if the program is sharing input devices  
    - pygame.event.post — place a new event on the queue  
    - pygame.event.Event — create a new event object  
    - pygame.event.EventType — pygame object for representing SDL events

    - [event](http://www.pygame.org/docs/ref/event.html)

Et comme on peut le voir, le module event ne permet pas que d’intercepter des événements. Il nous permet aussi de créer des événements. Et même d’en bloquer !


- Lorsqu'un programme ```pygame``` est lancé, la variable interne ```pygame.event.get()``` reçoit en continu les évènements des périphériques gérés par le système d'exploitation.  
- Nous allons nous intéresser aux évènements de type ```KEYDOWN``` (touche de clavier appuyée) ou de type ```MOUSEBUTTONDOWN``` (boutons de souris appuyé).

### Évènements clavier

#### Exemple de code
La structure de code pour détecter l'appui sur une touche de clavier est, dans le cas de la détection de la touche «Flèche droite» :

```python
for event in pygame.event.get():   
  if event.type == KEYDOWN:
    if event.key == K_RIGHT:
      print("flèche droite appuyée")
```
La touche (en anglais _key_) «Flèche Droite» est appelée ```K_RIGHT``` par ```pygame```. 

Le nom de toutes les touches peut être retrouvé à l'adresse [pygame ref](https://www.pygame.org/docs/ref/key.html.)

**Remarque :** c'est grâce à la ligne initiale  
```python
from pygame.locals import *
```
que la variable ```K_RIGHT``` (et toutes les autres) est reconnue.

#### Problème de la rémanence

Quand une touche de clavier est appuyée, elle le reste un certain temps. Parfois volontairement (sur un intervalle long) quand l'utilisateur décide de la laisser appuyée, mais aussi involontairement (sur un intervalle très court), lors d'un appui «classique».  
Il existe donc toujours un intervalle de temps pendant lequel la touche reste appuyée. Que doit faire notre programme pendant ce temps ? Deux options sont possibles :

- **option 1 :** considérer que la touche appuyée correspond à un seul et unique évènement, quelle que soit la durée de l'appui sur la touche.
- **option 2 :** considérer qu'au bout d'un certain délai, la touche encore appuyée doit déclencher un nouvel évènement.

Par défaut,```pygame``` est réglé sur l'option 1. Néanmoins, il est classique pour les jeux vidéos de vouloir que «laisser la touche appuyée» continue à faire avancer le personnage. Nous allons donc faire en sorte que toutes les 50 millisecondes, un nouvel appui soit détecté si la touche est restée enfoncée. Cela se fera par l'expression :

```python
pygame.key.set_repeat(50)
```


### Évènements souris

#### Exemple de code

La structure de code pour détecter l'appui sur un bouton de la souris est, dans le cas de la détection du bouton de gauche (le bouton 1)  :


```python
for event in pygame.event.get():    
  if event.type == MOUSEBUTTONDOWN and event.button == 1 :
      print("clic gauche détecté")
```

#### Récupération des coordonnées de la souris

Le tuple ```(abscisse, ordonnée)``` des coordonnées de la souris sera récupéré avec l'instruction ```pygame.mouse.get_pos()```.

## Déplacement du personnage

Le déplacement d'un personnage se fera toujours par modification de ses coordonnées (et visuellement, par effacement de la dernière position).  
Ce déplacement pourra être :  
- absolu : on donne de nouvelles coordonnées au personnage.  
- relatif : on indique de combien le personnage doit se décaler par rapport à sa position initiale.  

### Déplacement absolu

Pour afficher le personnage à la position ```(100,200)```, on écrira :  
```python
position_perso.topleft = (100,200)
```

où ```position_perso``` est l'objet de type ```rect```  contenant les coordonnées.

!!! exo
    Coder un script pour déplacer Paragoomba à la souris (Paragoomba doit toujours suivre la souris) (`MOUSEMOTION`)

??? correction

    ```python
    import pygame, sys
    from pygame.locals import *
    from random import randint

    pygame.init()

    #ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    ecran = pygame.display.set_mode((640, 480))
    ecran.fill([10,186,181])

    continuer = True

    perso = pygame.image.load("Paragoomba1.png").convert_alpha()
    position_perso = perso.get_rect()
    position_perso.topleft = (100,200)

    while continuer:
        pygame.draw.rect(ecran, (10,186,181), (0, 0, 640, 480))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                position_perso = event.pos
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    continuer = False
        ecran.blit(perso, position_perso)
        pygame.display.flip()
    
    pygame.quit()
    ```


!!! exo
    Coder un script pour dessiner un rectangle sur l’écran au relâchement d’un bouton de la souris.

??? correction

    ```python
    import pygame, sys
    from pygame.locals import *
    from random import randint

    pygame.init()

    #ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    ecran = pygame.display.set_mode((640, 480))
    ecran.fill([10,186,181])

    continuer = True

    perso = pygame.image.load("Paragoomba1.png").convert_alpha()
    position_perso = perso.get_rect()
    position_perso.topleft = (100,200)

    largeur = 10
    hauteur = 10
    couleur = (200, 80, 20)

    while continuer:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                pygame.draw.rect(ecran, couleur, (x, y, largeur, hauteur))
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    continuer = False
        ecran.blit(perso, position_perso)
        pygame.display.flip()
    ```

## Un Premier Jeu - Pong

Pong est l'un des premiers jeux vidéo d'arcade commercialisé en 1972. Il s'inspire du tennis de table. Devant l'engouement généré par le jeu, Pong est porté sur une console de salon à partir de 1975.  

Le package PyGame permet de réaliser avec Python des jeux en quelques heures. Nous allons donc créer un jeu de pong rudimentaire en utilisant des classes pour gérer la balle et la raquette

Voici ce à quoi ressemblera l'interface du jeu que nous allons créer :

![tennis](data/tennis.png)  

Nous allons mettre en oeuvre le concept objet en définissant une classe Balle et une classe Raquette pour le jeu de Pong.


### Ouverture d'une fenêtre graphique

Voici le code à saisir pour créer une fenêtre graphique dans laquelle nous dessinerons :

```python
import pygame
from pygame.locals import *
 
HAUTEUR_FENETRE = 480
LARGEUR_FENETRE = 640
 
fenetre = pygame.display.set_mode( (LARGEUR_FENETRE, HAUTEUR_FENETRE) )
pygame.display.set_caption("Titre de la fenêtre")
pygame.font.init()
fonte = pygame.font.Font(None, 30)
```

La fenêtre s'affiche mais disparait aussitôt. il faut créer une boucle pour la garder ouverte et rafraichir l'affichage dans la fenêtre :

```python
import pygame
from pygame.locals import *
 
HAUTEUR_FENETRE = 480
LARGEUR_FENETRE = 640
 
fenetre = pygame.display.set_mode( (LARGEUR_FENETRE, HAUTEUR_FENETRE) )
pygame.display.set_caption("Titre de la fenêtre")
pygame.font.init()
fonte = pygame.font.Font(None, 30)
 
while True:
  pygame.display.update()
```

L'écran reste noir et rien ne s'affiche. Dans la boucle while il faut réaliser une série d'actions : afficher des images, du texte, etc.

```python
import pygame
from pygame.locals import *
 
HAUTEUR_FENETRE = 480
LARGEUR_FENETRE = 640
 
fenetre = pygame.display.set_mode( (LARGEUR_FENETRE, HAUTEUR_FENETRE) )
pygame.display.set_caption("Titre de la fenêtre")
pygame.font.init()
fonte = pygame.font.Font(None, 30)
 
x = LARGEUR_FENETRE // 2
y = HAUTEUR_FENETRE // 2
rayon = 10
while True:
  # dessine la balle
  pygame.draw.circle(fenetre, (255,255,255), (x, y), rayon)
  pygame.display.update()
 
  # attente du clic souris sur x pour fermer la fenêtre
  # ou Alt+F4 sous Linux
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
```

Enfin il est nécessaire de déplacer les éléments dans la fenêtre :

```python
import pygame
from pygame.locals import *
 
# initialisation de l'écran de jeu
pygame.init()

HAUTEUR_FENETRE = 480
LARGEUR_FENETRE = 640
 
fenetre = pygame.display.set_mode( (LARGEUR_FENETRE, HAUTEUR_FENETRE) )
pygame.display.set_caption("Titre de la fenêtre")
pygame.font.init()
fonte = pygame.font.Font(None, 30)
 
# données de la balle
x = LARGEUR_FENETRE // 2
y = HAUTEUR_FENETRE // 2
rayon = 10

# vecteur de déplacement
vx = 1
vy = 1

while True:
  # temporise
  pygame.time.delay(15)
 
  # dessine le fond de l'écran en noir
  fenetre.fill( (0,0,0) )
 
  # dessine la balle
  pygame.draw.circle(fenetre, (255,255,255), (x, y), rayon)
 
  # nouvelle position
  x = x + vx
  y = y + vy
 
  if x >= LARGEUR_FENETRE or x <= 0:
    vx = -vx
 
  if y >= HAUTEUR_FENETRE or y <= 0:
    vy = -vy 
 
  pygame.display.update()

del(police)
pygame.quit()
```

!!! exo
    Améliorer la gestion du rebond car la balle sort de l'écran.

Gestion des événements
Afin de gérer les évènements (appui sur une touche, clic souris, etc), il faut énumérer chacun des événements reçus et vérifier celui qui nous intéresse.

Sur l'exemple suivant on test l'appui sur la touche 'A', un clic souris ou le fait de quitter la fenêtre en cliquant sur l'icone correspondante en haut de la fenêtre.

```python
import pygame
import sys
from pygame.locals import *
 
HAUTEUR_FENETRE = 480
LARGEUR_FENETRE = 640
 
fenetre = pygame.display.set_mode( (LARGEUR_FENETRE, HAUTEUR_FENETRE) )
pygame.display.set_caption("Titre de la fenêtre")
pygame.font.init()
fonte = pygame.font.Font(None, 30)
 
# données de la balle
x = LARGEUR_FENETRE // 2
y = HAUTEUR_FENETRE // 2
rayon = 10
# vecteur de déplacement
vx = 1
vy = 1
while True:
  # temporise
  pygame.time.delay(15)
 
  # dessine le fond de l'écran en noir
  fenetre.fill( (0,0,0) )
 
  # dessine la balle
  pygame.draw.circle(fenetre, (255,255,255), (x, y), rayon)
 
  # nouvelle position
  x = x + vx
  y = y + vy
 
  if x >= LARGEUR_FENETRE or x <= 0:
    vx = -vx
 
  if y >= HAUTEUR_FENETRE or y <= 0:
    vy = -vy 
 
  for event in pygame.event.get():
    if event.type == KEYDOWN:
      if event.key == pygame.K_a:
        vx = -vx
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    if event.type == MOUSEBUTTONDOWN:
      vy = -vy
   
  pygame.display.update()
```

### Le jeu de tennis (à la Pong)

Pour la création du jeu de tennis, nous allons organiser notre code en plusieurs fichiers :

- un fichier tennis.py qui sera le programme principal  
- un fichier constantes.py qui contiendra les constantes utilisées par les autres fichiers (hauteur et largeur de fenêtre, couleurs)  
- un fichier balle.py qui implantera une classe Balle qui représentera une balle qui rebondit sur les murs et la raquette  
- un fichier raquette.py qui représente une Raquette qui se déplace verticalement et dont le but et de taper dans la balle  

#### Les packages utilisés

On commence par introduire les packages (bibliothèques) qui seront utilisées :

```python
# paquet pygame pour gestion des graphismes et des sons
import pygame
# constantes de pygame pour le clavier
from pygame.locals import *
# paquet system pour quitter le jeu
import sys
# paquet random pour générer une position aléatoire de la balle au début
import random
```

### Les constantes du jeu : fichier constantes.py
On définit la hauteur et la largeur de la fenêtre ainsi que l'abscisse du mur qui sera situé à droite.

On définit également un jeu de couleurs qui utilisent des nuances proches de celles du tournoi du grand chelem de Roland Garros.

```python
# dimensions de la fenêtre
LARGEUR_FENETRE = 640
HAUTEUR_FENETRE = 480
 
# abscisse pour le mur
COORD_X_MUR = LARGEUR_FENETRE-20
 
# couleurs
BLANC_ROLAND_GARROS = 0
NOIR = 1
ORANGE_ROLAND_GARROS = 2
VERT_ROLAND_GARROS = 3
 
couleurs = [ (217,223,226), (0,0,0), (0xc8, 0x62, 0x2f), (0x22, 0x3f, 0x34) ]
```

#### La classe Balle balle.py

La balle se déplace dans l'aire de jeu et rebondit sur les bords haut, bas et droit de la fenêtre. Par contre sur la gauche elle doit rebondir sur la raquette pour que le jeu continue.

On crée une classe Balle que l'on instanciera par la suite. La classe est une structure de donnée et on pourra créer autant de balles que nécessaire par la suite mais dans le jeu qui nous intéresse il n'y a qu'une seule balle.

Pour la balle, on doit définir les méthodes suivantes :

- un constructeur `__init__`  
- dessine pour dessiner la balle dans la fenêtre courante  
- déplace pour déplacer la balle dans la fenêtre courante  
- rebond_x pour les rebonds sur l'axe des x (mur, raquette)  
- rebond_y pour les rebonds sur l'axe des y (bords fenetre)  
- perdue pour vérifier si la balle est toujours dans la zone de jeu  

On notera l'utilisation du mot-clé self qui permet de faire référence aux variables et méthodes de la classe.

```python
import random
import pygame
from constantes import *
 
"""
  classe Balle
 
  une balle est définie par les attributs (champs) suivants :
  - sa position x, y dans la fenêtre en pixels
  - son rayon en pixel
  - son vecteur de déplacement (dx, dy) en pixels
  - une référence à la fenêtre du jeu pour pouvoir dessiner la balle
 
"""
class Balle(object):
 
  """
    initialisation de la balle
  """
  def __init__(self, fenetre):
    self.x = 100
    self.y = random.randint(20, HAUTEUR_FENETRE-20)
    self.rayon = 10
    self.dx = 1
    self.dy = 1
    self.fenetre = fenetre
 
  """
    dessine la balle sous forme d'un cercle dans la fenêtre graphique
    avec une couleur blanche
  """
  def dessine(self):
    pygame.draw.circle(self.fenetre, couleurs[BLANC_ROLAND_GARROS], \
      (self.x, self.y), self.rayon)
 
  """
    déplace la balle en gérant les rebonds
  """
  def deplace(self):
    self.x += self.dx
    self.y += self.dy
    # rebond sur le mur à droite
    # TODO
    # rebond sur les bords haut et bas
    # TODO
     
  """
    rebond sur l'axe des x
  """
  def rebond_x(self):
    self.dx = -self.dx
 
  """
    rebond sur l'axe des y
  """
  def rebond_y(self):
    self.dy = -self.dy
       
  """
    indique si la balle est en dehors de l'aire de jeu
  """
  def perdue(self):
    return self.x < 0

```

#### La classe Raquette raquette.py

La raquette se déplace verticalement sur le bord gauche. On créera une instance de la raquette.

Pour la raquette, on doit définir les méthodes suivantes :

- un constructeur __init__  
- dessine pour dessiner la raquette dans la fenêtre courante  
- déplace pour déplacer la raquette dans la fenêtre courante  
- vers_le_haut pour modifier le déplacement de la raquette vers le haut  
- vers_le_bas pour modifier le déplacement de la raquette vers le bas  
- contact(balle) pour vérifier si la balle touche la raquette

```python
import random
import pygame
from constantes import *
 
"""
  classe raquette
 
  une raquette est définie par les attributs (champs) suivants :
  - sa position x, y dans la fenêtre en pixels, sachant que x est fixé
  - sa largeur et sa hauteur en pixels
  - son vecteur de déplacement en dy en pixels
  - une référence à la fenêtre du jeu pour pouvoir dessiner la balle
"""
class Raquette(object):
 
  """
    initialisation de la raquette
  """
  def __init__(self, fenetre):
    self.hauteur = 80
    self.largeur = 20
    self.x = 20
    self.y = (HAUTEUR_FENETRE - self.hauteur) // 2
    self.dy = 2
    self.fenetre = fenetre
   
  """
    dessine la raquette dans la fenêtre graphique 
    en blanc sous forme d'un rectangle
  """
  def dessine(self):
    pygame.draw.rect(self.fenetre, couleurs[BLANC_ROLAND_GARROS], \
      (self.x, self.y, self.largeur, self.hauteur), 0)
 
  """
    déplace la raquette suivant le vecteur de déplacement en inversant la direction
    si on arrive en haut ou en bas de la fenêtre
  """
  def deplace(self):
    self.y += self.dy
    # si la raquette est en haut on change la direction du déplacement
    # TODO
    # si la raquette est en bas on change la direction du déplacement
    # TODO
 
  """
    modifie le vecteur de déplacement pour que la raquette aille vers le haut
  """
  def vers_le_haut(self):
    self.dy = -1
 
  """
    modifie le vecteur de déplacement pour que la raquette aille vers le bas
  """
  def vers_le_bas(self):
    self.dy = +1
 
  """
    vérifie s'il y a contact entre la raquette et la balle
  """
  def contact(self, balle):
    # TODO
```

#### Le jeu
On crée la fenêtre de jeu, on utilise la fonte courante et on charge les sons qui seront utilisé pour le jeu :

- la musique d'ambiance music.mp3  
- et le bruit de verre brisé glass_break.wav qui indique la fin du jeu  

Le jeu se compose de trois parties :

- l'écran d'accueil qui indique quelles sont les touches pour jouer  
- le jeu de tennis  
- la fin de partie qui affiche le score obtenu par le joueur  


```python
###########################################################
# librairies
###########################################################
import pygame
from pygame.locals import *
import sys
import random
from constantes import *
import balle
import raquette
 
###########################################################
# fonctions utiles
###########################################################
 
"""
  afficher un texte au centre de l'écran
 
  si la coordonnée y est égale à -1, on place le texte
  au milieu de la fenetred'affichage
 
  on peut également spécifier la couleur qui est l'orange
  par défaut
 
"""
def affiche_texte_centre(texte, y=-1, couleur=None):
  if couleur == None:
    couleur = couleurs[ ORANGE_ROLAND_GARROS ]
  rendu = fonte.render(texte, True, couleur)
  rectangle = rendu.get_rect()
  if y == -1:
    rectangle.center = ((LARGEUR_FENETRE) / 2 , (HAUTEUR_FENETRE) / 2)
  else:
    rectangle.center = ((LARGEUR_FENETRE) / 2 , y)
  fenetre.blit(rendu, rectangle)
 
 
"""
  afficher un texte au centre de l'écran en précisant
  les coordonnées x et y
 
  on peut également spécifier la couleur qui est l'orange
  par défaut
 
"""
def affiche_texte(texte, x, y, couleur=None):
  if couleur == None:
    couleur = couleurs[ ORANGE_ROLAND_GARROS ]
  rendu = fonte.render(texte, True, couleur)
  rectangle = rendu.get_rect()
  rectangle.center = (x, y)
  fenetre.blit(rendu, rectangle)
 
"""
  quitter le programme
 
  on arrête la musique d'ambiance et on libère les resources
  utilisées par pygame
 
"""
def quitter():
  pygame.mixer.music.stop()
  pygame.quit()
  sys.exit()
 
"""
  attend qu'on tape une touche au clavier
 
  on parcourt les événements (clavier, souris) mais en ne
  traitant que l'appui sur une touche (KEYDOWN)
"""
def touche_clavier():
  for event in pygame.event.get():
    if event.type == KEYDOWN:
      # Ctrl-C pour quitter le jeu
      if event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
        quitter()
      # retourner la touche pressée 
      return event.key
    # sinon, ne rien retourner (valeur nulle)
    return None    
       
"""
  on attend que l'utilisateur tape une touche du clavier avant
  d'aller plus loin. A chaque itération on redessine la fenêtre
"""      
def attente():
  while touche_clavier() == None:
    pygame.display.update()
     
 
 
###########################################################
# initialisation du jeu
###########################################################
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
pygame.display.set_caption("Tennis")
pygame.font.init()
fonte = pygame.font.Font(None, 30) 
crash_sound = pygame.mixer.Sound("glass_break.wav")
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()
 
###########################################################
# définition des variables du jeu
###########################################################
 
balle = balle.Balle(fenetre)
 
raquette = raquette.Raquette(fenetre)
 
# nombre de rebonds sur la raquette
score = 0
 
# variable booléenne à vrai si on est en pause
pause = False
 
 
###########################################################
# écran d'accueil
###########################################################
fenetre.fill(couleurs[NOIR])
affiche_texte_centre("Appuyez sur une touche pour commencer", 100)
affiche_texte_centre("Flèche haut pour faire monter la raquette", 140)
affiche_texte_centre("Flèche bas pour faire descendre la raquette", 170)
affiche_texte_centre("p pour pause", 200)
affiche_texte_centre("Ctrl-C pour quitter", 230)
attente()
     
###########################################################
# écran de jeu : boucle principale
###########################################################
while True:
  # temporisation : arrêt de l'exécution du programme pendant 5 ms
  pygame.time.delay(5)
 
  # -------------------------------
  # dessine les différents éléments
  # - fond d'écran
  # - mur de droite
  # - balle
  # - raquette
  # - score
  # -------------------------------
 
  # dessine le fond en orange
  fenetre.fill( couleurs[ ORANGE_ROLAND_GARROS ] )
  # dessine le mur de droite
  pygame.draw.rect(fenetre, couleurs[ VERT_ROLAND_GARROS ], (COORD_X_MUR, 0, 20, HAUTEUR_FENETRE), 0)
 
  balle.dessine()
 
  raquette.dessine()
 
  # affichage du score
  texte = "Score = {}".format(score)
  affiche_texte_centre(texte, 20, couleurs[VERT_ROLAND_GARROS])
 
  pygame.display.update()
 
  # -------------------------------
  # gestion des événements clavier
  # - flèche vers le haut
  # - flèche vers le bas
  # - 'p' pour pause
  # -------------------------------
 
  clavier = touche_clavier()
  if clavier == K_UP:
    raquette.vers_le_haut()
  if clavier == K_DOWN:
    raquette.vers_le_bas() 
  if clavier == K_p:
    pause = not pause
 
  # si on a appuyé sur 'p' et qu'on met le jeu en pause
  # il ne faut pas aller plus loin c'est à dire qu'il ne
  # faut pas déplacer ni la raquette, ni la balle
  if pause:
    continue
 
  # ------------------------------
  # déplacement de la raquette et de la balle
  # vérification de fin de jeu
  # ------------------------------
   
  raquette.deplace()
   
  balle.deplace()
 
  # si balle en dehors de l'aire de jeu, on quitte la boucle
  # de jeu
  # TODO
 
  # si la balle touche la raquette, on réalise le rebond
  # TODO   
 
################################
# écran de fin de partie
################################
 
fenetre.fill( couleurs[NOIR] )
texte = "Votre score est de {} points".format(score)
affiche_texte_centre(texte)
affiche_texte_centre("Appuyez sur une touche pour terminer", 200)
pygame.mixer.Sound.play(crash_sound)
pygame.mixer.music.stop()
attente()
 
quitter()
```

### Multi Pong


!!! exo 
    A titre d'exercice vous pouvez modifier le jeu de manière à lancer plusieurs balles au début du jeu. Il suffit de créer une liste de balles et de travailler avec cette liste plutôt qu'avec une seule balle.

!!! exo     
    On peut également faire en sorte qu'à mesure que le temps passe :

    - les balles se déplacent plus vite  
    -  la hauteur de la raquette diminue  
    