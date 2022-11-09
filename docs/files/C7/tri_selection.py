from random import randint

def tri_selection(lst) :
    for k in range(len(lst)-1):
        indice_min = k
        for i in range(k+1, len(lst)) :
            if lst[i] < lst[indice_min]:
                indice_min = i
        lst[k], lst[indice_min] = lst[indice_min], lst[k]

ex_liste = [randint(1,100) for _ in range(50)]
tri_selection(ex_liste)
print(ex_liste)