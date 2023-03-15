def chercher_mots(liste_mots,longueur,lettre,position):
    res=[]
    for i in range(len(liste_mots)):
        if liste_mots[i][position]==lettre and len(liste_mots[i])==longueur:
            res.append(liste_mots[i])
    return res

liste=['test','aide','tiro','six']

print(chercher_mots(chercher_mots(liste,4,'i',1),4,'e',3))