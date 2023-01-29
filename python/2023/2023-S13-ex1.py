def recherche(a,tab):
    nb_occurence = 0
    for elt in tab:
        if elt==a:
            nb_occurence +=1
    return nb_occurence