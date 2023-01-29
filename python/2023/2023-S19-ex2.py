ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    resultat = ''
    for c in message : #(1)
        if 'A' <= c and c <='Z': #(2)
            indice = (position_alphabet(c) + decalage)%26 #(3)
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat + c #(4)
    return resultat
