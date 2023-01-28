def rangement_valeurs(notes_eval):
    new_tab=[]
    for i in range(11):
        nb=0
        for note in notes_eval:
            if note==i:
                nb+=1
        new_tab.append(nb)
    return new_tab

def notes_triees(liste_effectif):
    tab=[]
    nb=0
    for v in liste_effectif:
        for i in range(v):
            tab.append(nb)
        nb+=1
    return tab
        


