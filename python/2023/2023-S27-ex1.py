def recherche_min(tab):
    indice_mini,mini = 0, tab[0]
    for indice in range(1,len(tab)):
        if tab[indice]<mini:
            indice_mini,mini = indice,tab[indice]
    return indice_mini