def echange(liste,i,j):
    liste[i],liste[j] = liste[j],liste[i]

def min_liste(liste,ind):
    elt_min = liste[ind]
    ind_min=ind
    for k in range(ind,len(liste)):
        if liste[k]<elt_min:
            elt_min=liste[k]
            ind_min=k
    return ind_min

def tri_selection(liste):
    longueur = len(liste)
    for ind in range(longueur):
        ind_min = min_liste(liste,ind)
        echange(liste,ind,ind_min)

L=[12,19,10,13,11,15,9,14]



def echange(liste,i,j):
    liste[i],liste[j] = liste[j],liste[i]

def max_liste(liste,ind):
    elt_max = liste[ind]
    ind_max=ind
    for k in range(ind,len(liste)):
        if liste[k]<elt_min:
            elt_min=liste[k]
            ind_min=k
    return ind_min

def tri_selection_inverse(liste):
    longueur = len(liste)
    for ind in range(longueur):
        ind_min = min_liste(liste,ind)
        echange(liste,ind,ind_min)

L=[12,19,10,13,11,15,9,14]

print(tri_selection(L))
print(L)
