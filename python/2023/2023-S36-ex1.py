def couples_consecutifs(tab):
    consecutifs = []
    for i in range(len(tab)-1):
        if tab[i+1]==tab[i]+1:
            consecutifs.append((tab[i],tab[i+1]))
    return consecutifs


