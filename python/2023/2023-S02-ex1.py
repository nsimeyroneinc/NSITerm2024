def indices_maxi(tab):
    maxi, indices_maxi = tab[0], [0]
    for i in range(1,len(tab)):
        if tab[i] > maxi:
            maxi = tab[i]
            indices_maxi = [i]
        elif tab[i] == maxi:
            indices_maxi.append(i)
    return maxi, indices_maxi
