def max_et_indice(tab):
    maxi = tab[0]
    indice = 0
    for i in range(len(tab)):
        if tab[i] > maxi:
            maxi = tab[i]
            indice = i
    return maxi, indice
