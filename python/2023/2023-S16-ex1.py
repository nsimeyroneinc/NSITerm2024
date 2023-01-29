def recherche_indices_classement(elt,tab):
    inferieur = []
    egal = []
    superieur = []
    for i in range(len(tab)):
        if tab[i]<elt:
            inferieur.append(i)
        elif tab[i]==elt:
            egal.append(i)
        else:
            superieur.append(i)
    return inferieur, egal, superieur

