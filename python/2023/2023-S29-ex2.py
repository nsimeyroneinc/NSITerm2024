def ajoute(indice, element, liste):
    nbre_elts = len(liste)
    L = [0 for i in range(nbre_elts + 1)]
    if indice < len(liste): #(1)
        for i in range(indice):
            L[i] = liste[i] #(2)
        L[indice] = element
        for i in range(indice + 1, nbre_elts + 1):
            L[i] = liste[i-1] #(3)
    else:
        for i in range(nbre_elts): #(4)
            L[i] = liste[i]
        L[nbre_elts] = element
    return L


