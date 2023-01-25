#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
"""
Source pour le calcul:
https://geodesie.ign.fr/contenu/fichiers/Distance_longitude_latitude.pdf
"""
 
from math import sin, cos, acos, pi
 
#############################################################################
def dms2dd(d, m, s):
    """Convertit un angle "degrés minutes secondes" en "degrés décimaux"
    """
    return d + m/60 + s/3600
 
#############################################################################
def dd2dms(dd):
    """Convertit un angle "degrés décimaux" en "degrés minutes secondes"
    """
    d = int(dd)
    x = (dd-d)*60
    m = int(x)
    s = (x-m)*60
    return d, m, s
 
#############################################################################
def deg2rad(dd):
    """Convertit un angle "degrés décimaux" en "radians"
    """
    return dd/180*pi
 
#############################################################################
def rad2deg(rd):
    """Convertit un angle "radians" en "degrés décimaux"
    """
    return rd/pi*180
 
#############################################################################
def distanceGPS(latA, longA, latB, longB):
    """Retourne la distance en mètres entre les 2 points A et B connus grâce à
       leurs coordonnées GPS (en radians).
    """
    # cooordonnées GPS en radians du 1er point (ici, mairie de Tours)
    lat1 = deg2rad(latA) # Nord
    long1 = deg2rad(longA) # Est

    # cooordonnées GPS en radians du 2ème point (ici, mairie de Limoges)
    lat2 = deg2rad(latB) # Nord
    long2 = deg2rad(longB) # Est
    # Rayon de la terre en mètres (sphère IAG-GRS80)
    RT = 6378137
    # angle en radians entre les 2 points
    S = acos(sin(lat1)*sin(lat2) + cos(lat1)*cos(lat2)*cos(abs(long2-long1)))
    # distance entre les 2 points, comptée sur un arc de grand cercle
    return S*RT
 
#############################################################################

latA,longA =(45.54909280064133, 3.1339889032710375)
latB,longB = (45.55034640571267, 3.2496815789627)
dist = distanceGPS(latA, longA, latB, longB)
print(int(dist))
