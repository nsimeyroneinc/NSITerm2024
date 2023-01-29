from random import randint

def nbre_coups():
    n = 0 #(1)
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while len(cases_vues) < 12: #(2)
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % nbre_cases #(3)
        if case_en_cours not in cases_vues: #(4)
            cases_vues.append(case_en_cours)
        n = n + 1
    return n

