def nbr_occurrences(chaine):
    occ = {}
    for caractere in chaine:
        if caractere in occ:
            occ[caractere] += 1
        else:
            occ[caractere]=1
    return occ
