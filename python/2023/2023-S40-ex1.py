def nombre_de_mots(phrase):
    nbr_espaces = 0
    for caractere in phrase:
        if caractere == " ":
            nbr_espaces += 1
    if phrase[-1] == "!" or phrase[-1]=="?":
        nbr_mots = nbr_espaces
    else:
        nbr_mots = nbr_espaces + 1
    return nbr_mots
