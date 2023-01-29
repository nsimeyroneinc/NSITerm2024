def moyenne(liste):
    somme = 0
    somme_coefficient = 0
    for note,coefficient in liste:
        somme = somme + note*coefficient
        somme_coefficient = somme_coefficient + coefficient
    if somme_coefficient != 0:
        return somme/somme_coefficient
    else:
        return None