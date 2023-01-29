def maxliste(tab):
    maxi = tab[0]
    for elt in tab:
        if elt > maxi:
            maxi=elt
    return maxi
