import math
import json

fp = open('l-fra2021.json')
dico = json.load(fp) 

# Métropole = 1er des 33 contours disponibles
liste = dico['features'][0]['geometry']['coordinates'][0]
R_TERRE = 6_378_137
CIRCONF = int(2 * math.pi * R_TERRE)
def wmts(coordonnee):
    '''
    Calcule les coordonnées WMTS (en mètres)
    d'une géolocalisation donnée (latitude et longitude en degrés)
    '''
    longitude = coordonnee[0]
    latitude = coordonnee[1]
    
    return (CIRCONF/2 + R_TERRE * math.radians(longitude),
        CIRCONF/2 - R_TERRE * math.log(math.tan(math.radians(latitude)/2 + math.pi/4)) )

# Ligne polygonale de la métropôle (11 674 sommets)
poly = [wmts(c) for c in dico['features'][0]['geometry']['coordinates'][0]]



    


from math import sqrt
import matplotlib.pyplot as plt

def distance_points(a, b):
    return sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)

def distance_point_droite(p, a, b):
    if b[0] == a[0]:
        return abs(p[0]-a[0])
    m = (b[1] - a[1]) / (b[0] - a[0])
    od = a[1] - m*a[0]
    xm = (p[0]*(b[0]-a[0])+(p[1]-od)*(b[1]-a[1])) / (b[0]-a[0] + m*(b[1]-a[1]))
    ym = m*xm + od
    return distance_points(p, (xm, ym))  

def distance(p, a, b):
    if a == b:
        return distance_points(p, a)
    else:
        return distance_point_droite(p, a, b)

def le_plus_loin(ligne):
    n = len(ligne)
    deb = ligne[0]
    fin = ligne[n-1]
    dmax = 0
    indice_max = 0
    for idx in range(1, n-1):
        p = ligne[idx]
        d = distance(p, deb, fin)
        if d > dmax:
            dmax = d
            indice_max = idx
    return (indice_max, dmax)


def extrait(tab, i, j):
    ext = []
    for k in range(i, j+1):
        ext.append(tab[k])
    return ext

def simplifie(ligne, seuil):
    n = len(ligne)
    if n <= 2:
        return ligne
    else:
        indice_max, dmax = le_plus_loin(ligne)
        if dmax <= seuil:
            return [ligne[0], ligne[n-1]]
        else:
            return simplifie(extrait(ligne, 0, indice_max), seuil) + \
                   simplifie(extrait(ligne, indice_max+1, n-1), seuil)


france = [(8.74, 14.18),(8.12, 13.96),(8.08, 13.14),(7.62, 12.8),
         (7.04, 12.5),(6.84, 12.24),(6.52, 12.04),(5.86, 12.14),
         (5.74, 12.56),(5.26, 12.58),(5.34, 12.12),(5.48, 11.64),
         (5.54, 11.28),(5.18, 11.3),(4.76, 11.26),(4.46, 11.14),
         (4.24, 11.62),(3.86, 11.58),(3.50, 11.48),(2.80, 11.3),
         (2.90, 11.0), (3.18, 10.78),(2.68, 10.68),(3.04, 10.5),
         (3.60, 10.3),(4.06, 10.02),(4.44, 9.92),(4.62, 9.62),
         (4.98, 9.32),(4.92, 8.94),(5.04, 8.52),(5.52, 8.38),
         (5.66, 7.98),(5.58, 7.64),(5.96, 7.22),(5.66, 7.26),
         (5.52, 6.46),(5.46, 5.72),(5.24, 5.04),(5.00, 4.74),
         (5.34, 4.52),(5.72, 4.20),(6.24, 3.98),(6.86, 3.86),
         (7.18, 3.80),(7.34, 4.04),(7.64, 3.82),(8.04, 3.74),
         (8.28, 3.42),(8.76, 3.46),(9.04, 3.50),(9.42, 3.52),
         (9.32, 4.08),(9.78, 4.58),(10.3, 4.86),(10.66, 4.76),
         (11.18, 4.64),(11.56, 4.48),(12.22, 4.42),(12.68, 4.54),
         (12.98, 5.08),(13.42, 5.64),(12.86, 5.84),(12.68, 6.32),
         (12.8, 6.66),(12.34, 6.86),(12.86, 7.22),(12.58, 7.68),
         (12.68, 8.00),(12.48, 8.38),(12.04, 8.52),(11.84, 8.12),
         (11.9, 8.82), (12.44, 9.46),(12.98, 9.92),(13.04, 10.5),
         (13.08, 11.22),(13.46, 11.76),(12.78, 11.86),(12.26, 11.96),
         (11.8, 12.34),(11.14, 12.34),(10.72, 12.72),(10.62, 13.16),
         (10.3, 12.78),(9.98, 12.9),(10.04, 13.34),(9.64, 13.4),
         (9.34, 13.54),(9.34, 13.92),(8.92, 13.82),(8.74, 14.18)]

def trace(ligne, seuil):
    new_ligne = simplifie(ligne, seuil)
    x = [p[0] for p in new_ligne]
    y = [p[1] for p in new_ligne]
    plt.plot(x, y, 'r-')
    plt.text(2, 14, 'seuil : ' + str(seuil))
    plt.axis('equal')
    plt.show()

trace(poly, 0)
