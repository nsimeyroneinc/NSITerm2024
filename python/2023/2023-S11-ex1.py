def convertir(tab):
    poids =  len(tab)-1
    valeur = 0
    for elt in tab:
        valeur += 2**poids * elt
        poids -=1
    return valeur
