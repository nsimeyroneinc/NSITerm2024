def tri_selection(tab):
    N = len(tab)
    for k in range(N): #(1)
        imin = k
        for i in range(k , N): #(2)
            if tab[i] < tab[imin] :
                imin = i
        tab[k] , tab[imin] = tab[imin] , tab[k] #(3)
