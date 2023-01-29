def separe(tab):
    gauche = 0
    droite = len(tab)-1 #(1)
    while gauche < droite :
        if tab[gauche] == 0 :
            gauche = gauche + 1 #(2)
        else :
            tab[gauche], tab[droite] = tab[droite], tab[gauche] #(3)
            droite = droite - 1
    return tab
