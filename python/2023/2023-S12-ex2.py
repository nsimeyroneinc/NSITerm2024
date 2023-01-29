def empaqueter(liste_masses, c):
    n = len(liste_masses)
    nb_boites = 0
    boites = [0]*n
    for masse in liste_masses : #(1)
        i=0
        while i <= nb_boites and boites[i] + masse > c: #(2) 
                i = i + 1
        if i == nb_boites + 1: #(3) 
                nb_boites = nb_boites + 1
        boites[i] = boites[i] + masse
    return nb_boites + 1 #(4)
