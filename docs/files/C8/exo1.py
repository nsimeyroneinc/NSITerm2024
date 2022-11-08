def maxi(liste):
    i_centre=len(liste)
    l1=liste[i_centre:]
    l2=liste[:i_centre]
    m1=maxi(l1)
    m2=maxi(l2)
    return m1,m2

L=[12,19,10,13,11,15,9,14]

print(maxi(L))
