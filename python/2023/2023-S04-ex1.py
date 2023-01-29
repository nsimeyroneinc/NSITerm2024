def a_doublon(liste_triee):
    for i in range(len(liste_triee)-1):
        if liste_triee[i] == liste_triee[i+1]:
            return True
    return False
    