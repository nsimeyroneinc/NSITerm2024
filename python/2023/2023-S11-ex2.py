def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i] #(1)
        # la variable j sert à déterminer où placer la valeur à ranger
        j = i #(2)
        # tant qu'on a pas trouvé la place de l'élément à insérer
        # on décale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j-1]: #(3)
            tab[j] = tab[j-1]
            j = j - 1
        tab[j] = valeur_insertion
