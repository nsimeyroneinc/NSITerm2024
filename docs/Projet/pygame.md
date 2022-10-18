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
            <th class="redTh"; width="80%"; style="text-align:center;border:none;font-size:25pt;">Pygame : Initiation</th>
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

### Déplacement du personnage

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

## Le jeu de tennis (à la Pong)

Pour la création du jeu de tennis, nous allons organiser notre code en plusieurs fichiers :

- un fichier tennis.py qui sera le programme principal  
- un fichier constantes.py qui contiendra les constantes utilisées par les autres fichiers (hauteur et largeur de fenêtre, couleurs), certaines fonctions...  


### Les packages utilisés

On commence par introduire les packages (bibliothèques) qui seront utilisées :

```python
import pygame
from pygame.locals import *
from constantes import *
```

### Les constantes du jeu : fichier constantes.py

On définit la hauteur et la largeur de la fenêtre ainsi que l'abscisse du mur qui sera situé à droite.

On définit également un jeu de couleurs.

```python
import pygame
from pygame.locals import *
from constantes import *


# initialisation de l'écran de jeu
pygame.init()



police = pygame.font.SysFont("Arial", 25)
fonte = pygame.font.Font(None, 30) 


# Initialise la fenêtre de jeu
largeur_ecran = 600
hauteur_ecran = 400

screen = pygame.display.set_mode((largeur_ecran,hauteur_ecran))
pygame.display.set_caption("Tennis")

# variables d'état

hauteur_raquette=50

largeur_raquette =10
dist_mur   = 20  # distance du mur au bord de la raquette


raquette_G_x = dist_mur
raquette_G_y = 50


ball_x = int(largeur_ecran / 2)
ball_y = int(hauteur_ecran / 2)
ball_speed_x = -4
ball_speed_y = -4
ball_rayon  = 10

score = 0
vie=2

COORD_X_MUR = largeur_ecran-20


# Definit des couleurs RGB
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
GREEN = [24, 161, 80]
RED   = [255, 0, 0]
BLUE  = [30 , 36 , 161]
ORANGE = [196 , 92 , 54]

#fonctions permettant de dessiner la balle et les deux raquettes
def Raquette(x, y):
   R = (x,y,largeur_raquette,hauteur_raquette)
   pygame.draw.rect(screen, WHITE, R, 0)

def Balle(x,y):
   pygame.draw.circle(screen, WHITE, (x,y),10, 0)

def Mur():
   R = (COORD_X_MUR,0,20,hauteur_ecran)
   pygame.draw.rect(screen, GREEN, R, 0)



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
     
def attente():
   while touche_clavier() == None:
      pygame.display.update()

# initialisation de l'écran de jeu
pygame.init()




def affiche_texte_centre(texte, y=-1, couleur=None):
  if couleur == None:
    couleur = ORANGE
  rendu = fonte.render(texte, True, couleur)
  rectangle = rendu.get_rect()
  if y == -1:
    rectangle.center = ((largeur_ecran) / 2 , (hauteur_ecran) / 2)
  else:
    rectangle.center = ((largeur_ecran) / 2 , y)
  screen.blit(rendu, rectangle)

def affiche_texte(texte, x, y, couleur=None):
  if couleur == None:
    couleur = WHITE
  rendu = fonte.render(texte, True, couleur)
  rectangle = rendu.get_rect()
  rectangle.center = (x, y)
  screen.blit(rendu, rectangle)

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
import pygame
from pygame.locals import *
from constantes import *




 



# Gestion du rafraichissement de l'écran
clock = pygame.time.Clock()

# Cache le pointeur de la souris
pygame.mouse.set_visible(0)




###########################################################
# écran d'accueil
###########################################################
screen.fill(BLACK)
affiche_texte_centre("Appuyez sur une touche pour commencer", 100)
affiche_texte_centre("Flèche haut pour faire monter la raquette", 140)
affiche_texte_centre("Flèche bas pour faire descendre la raquette", 170)

attente()

# Le jeu continue tant que l'utilisateur ne ferme pas la fenêtre
Termine = False

# Boucle principale de jeu
while not Termine:
   # recupère la liste des évènements du joueur
   event = pygame.event.Event(pygame.USEREVENT)
   
   # dessine le mur de droite
   
   # EVENEMENTS
   # détecte le clic sur le bouton close de la fenêtrepygame.Rect
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         Termine = True

   # récupère la liste des touches claviers appuyeées sous la forme d'une liste de booléens
   KeysPressed = pygame.key.get_pressed()

   # LOGIQUE
   # déplacement du palet gauche

   if KeysPressed[pygame.K_UP]:
       raquette_G_y -= 3

   if KeysPressed[pygame.K_DOWN]:
       raquette_G_y += 3


   if raquette_G_y < 0 :
      raquette_G_y = 0


   if raquette_G_y > hauteur_ecran - hauteur_raquette :
       raquette_G_y = hauteur_ecran - hauteur_raquette

   # Déplacement de la balle
   ball_x += ball_speed_x
   ball_y += ball_speed_y

   if ball_y < ball_rayon or ball_y > hauteur_ecran - ball_rayon :
       ball_speed_y *= -1

   # collision entre la balle et le palet de gauche
   if ball_x  <  dist_mur + largeur_raquette + ball_rayon :
       if ball_y > raquette_G_y  and  ball_y  <  raquette_G_y + hauteur_raquette :
          ball_speed_x *= -1
          score+=1
         


   # collision avec les murs gauche et droit
   if ball_x < ball_rayon :
      ball_x = int(largeur_ecran / 2)
      ball_y = int(hauteur_ecran / 2)
      vie-=1
      

   if ball_x > largeur_ecran - ball_rayon :
      ball_speed_x *= -1



   # AFFICHAGE
   # Dessine le fond
   screen.fill(BLACK)
   Mur()
   Raquette(raquette_G_x, raquette_G_y)

   Balle(ball_x,ball_y)

   #  dessine le texte dans une zone de rendu à part
   texte = "Votre score : " + str(score) + " Vie : " + str(vie)
   if score == 15 :
      texte = "Joueur GAGNANT"
      Termine=True
   if vie<=0:
      texte = 'PERDU' 
      Termine=True


   zone = police.render( texte, True, GREEN)
   # affiche la zone de rendu au dessus de fenetre de jeu
   screen.blit(zone,(280,10))



   # Bascule l'image dessinée à l'écran
   pygame.display.flip()

    # Demande à pygame de se caler sur 30 FPS
   clock.tick(30)

screen.fill( 'black')
texte = "Votre score est de {} points".format(score)
affiche_texte_centre(texte,150)
affiche_texte_centre("Appuyez sur une touche pour terminer", 200)
attente()

# Ferme la fenêtre
del(police)
pygame.quit()


```

### Le jeu Pong en lui-même

A vous.

## SNAKE en Python, le plus simplement possible

### Version 0


#### Pygame
On importe pygame avec :

```python
import pygame
from pygame.locals import *
```

Le second import sert à quitter le jeu propremement.


#### Constantes
On crée quelques constantes :

```python
HAUTEUR = 600  # hauteur de la fenetre
LARGEUR = 600  # largeur de la fenetre
BLOC = 20

# Les couleurs utilisées
NOIR = (..., ..., ...)  # fond
ROUGE = (..., ..., ...) # pomme
JAUNE = (..., ..., ...)  # tête
VERT = (..., ..., ...)  # corps
CYAN = (..., ..., ...)  # texte

FPS = 30
```

#### initialisation

On initialise le jeu :

```python


pygame.init()
horloge = pygame.time.Clock()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption('Snake')

pygame.display.update()
```

#### Boucle Infinie

Tous les jeux comportent une boucle infinie. Celle-ci ne contient pas grand chose :

* quitter le jeu,  
* remplir la fenêtre de noir  
* faire avancer l'horloge  
* mettre à jour les affichages  

#### Boucle infinie

```python
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
    fenetre.fill(NOIR)
    horloge.tick(FPS)
    pygame.display.update()
```

#### Boucle infinie

* La boucle `for event in...` permet de récupérer les événements "cliquer sur la croix" ou "appuyer sur Escape" et quitte le jeu dans ce cas.

* Ensuite on dessine la fenêtre, remplie de noir
* On fait avancer l'horloge
* On affiche tout ça

### Version 1

#### Ecrire du texte

Cette fonction nous permettra d'écrire facilement le score

```python
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, CYAN)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
```

#### Taille de la police, valeur du score

```Python
font = pygame.font.SysFont(None, 48)
```

et

```python
score = 0
```

#### Le serpent

Le serpent est une double liste

```python
snake = [[3, 3], [2, 3], [1, 3]]
```

Le premier élément est sa tête, elle est en `[3,3]` ensuite vient son
corps. Il commence donc avec une taille de 3.

#### Dessiner le serpent

Dans la boucle infinie, avant l'horloge :

```python
  for elt in snake[1:]:
      pygame.draw.rect(fenetre, VERT,
                       (elt[0] * BLOC, elt[1] * BLOC,
                        BLOC, BLOC))
  pygame.draw.rect(fenetre, JAUNE,
                   (snake[0][0] * BLOC, snake[0][1] * BLOC,
                    BLOC, BLOC))
```

Le corps est vert et la tête jaune.

#### Afficher le score

On utilise notre fonction crée plus tôt :

``` python
drawText(str(score), font, fenetre, 0.2*LARGEUR, 0.2*HAUTEUR)
```


### Version 2

#### Capturer les touches du jeu

On ne capturait que "Escape" et le clic sur la croix. On ajoute les flêches.

```python
  if key:
    if key[pygame.K_UP]:
        print("up")
    if key[pygame.K_DOWN]:
        print("down")
    if key[pygame.K_LEFT]:
        print("left")
    if key[pygame.K_RIGHT]:
        print("right")
```

#### Capturer les touches du jeu

Pour l'instant elles ne font rien d'autre qu'afficher du texte

### Version 3

#### Diminuer la vitesse de rafaîchissement

```python
FPS = 3
```


#### Déplacer le serpent

On commence par créer une direction (= la vitesse)

```python
direction = (1, 0)
```

#### Déplacer le serpent

Chaque pression d'une flêche change la direction :

```python
    key = pygame.key.get_pressed()
    if key:
        if key[pygame.K_UP]:
            direction = (..., ...)
        if key[pygame.K_DOWN]:
            direction = (..., ...)
        if key[pygame.K_LEFT]:
            direction = (..., ...)
        if key[pygame.K_RIGHT]:
            direction = (..., ...)
```

#### Déplacer le serpent

Ensuite la tête.

C'est l'ancienne tête, qui s'est déplacée :

```python
  head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
```

#### Déplacer le serpent

Le corps se déplace.

1. On ajoute la tête au début :


??? correction

    ```python
      snake.insert(0, head)
    ```

2. On perd un élément de fin :

??? correction

    ```python
      snake.pop(-1)
    ```

### Version 4

#### La mort du serpent

Il meurt :

* s'il quitte l'écran  
* si sa tête est dans son corps  


#### La mort du serpent

??? correction

    ```python
      if head in snake[1:] or head[0] < 0 or head[0] > LARGEUR / BLOC - 1 or head[1] < 0 or head[1] > HAUTEUR / BLOC - 1:
       pygame.quit()
    ```

### Version 5

#### Fluidité

Le jeu n'est pas fluide.

On va mettre à jour les éléments du jeux toutes les 1.5 secondes
et afficher 30 frames par secondes.

Il nous faut deux variables supplémentaires :

1. Une valeur pour décider quand mettre à jour  
2. Un compteur  

#### Fluidité

```python
FPS = 30
MAJ = 10

# ...

# juste avant la boucle infinie
compteur = 0
```

#### Fluidité

Dans la boucle infinie

```python
  if compteur == MAJ:
    compteur = 0
    head = [snake[0][0] + direction[0],
            snake[0][1] + direction[1]]
    # autres événements

  # On augmente le compteur
  # tout à la fin de la boucle infinie
  compteur += 1
```


#### Nourriture

On crée d'abord une nouvelle liste :

```python
pomme = [8, 3]
```

#### Nourriture

On dessine la pomme comme la tête, mais en rouge

??? correction

    ```python
    pygame.draw.rect(fenetre, ROUGE,(pomme[0] * BLOC, pomme[1] * BLOC, BLOC, BLOC))
    ```

#### Nourriture

Puis on détecte la collision avec la pomme.

En cas de collision :

1. Le score augmente  
2. Une nouvelle pomme est crée.  

La boucle `while` empêche la pomme d'apparaître sur le serpent

#### Nourriture

??? correction

    ```python
    from random import randint
      # ...

      # Dans la boucle infinie
      if snake[0] == pomme:
        score += 1
        while pomme in snake:
            pomme = [randint(0, LARGEUR / BLOC - 1),
                    randint(0, HAUTEUR / BLOC - 1)]
    ```


#### Nourriture

S'il n'y a pas de collision le serpent diminue, sinon il conserve sa taille

```python
  else:
    snake.pop(-1)
```


### Conclusion

#### Conclusion

C'est terminé...

Snake en 100 lignes (peu commentées) avec le minimum d'instructions.
On peut faire beaucoup plus court mais c'est déjà très simple

#### Conclusion

* Python permet notamment de créer des jeux,  
* Créer un jeu avec Pygame n'est pas difficile,  
* Il nous faut quelques constantes, quelques éléments de jeu (serpent, tête)  
* Une boucle infinie dans laquelle  
  1. On lit les saisies de l'utilisateur  
  2. On effectue les calculs (nouvelle tête, collisions etc.)  
  3. On met à jour les éléments graphiques  