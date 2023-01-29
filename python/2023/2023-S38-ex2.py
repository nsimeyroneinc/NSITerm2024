def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire `plan` correspondant à un
    plan d'envoi de messages (ici entre les personnes A, B, C, D,
    E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et
    False sinon.
    '''
    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinaires = 1
    while destinataire != expediteur: #(1)
        destinataire = plan[destinataire] #(2)
        nb_destinaires += 1
    return nb_destinaires == len(plan) #(3)
