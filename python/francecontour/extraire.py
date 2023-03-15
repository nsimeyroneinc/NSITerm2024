import json

fp = open('l-fra2021.json')
dico = json.load(fp) 

# Métropole = 1er des 33 contours disponibles
liste = dico['features'][0]['geometry']['coordinates'][0]