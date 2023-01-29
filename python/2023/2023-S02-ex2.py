def positif(pile):
    pile_1 = list(pile) #(1)
    pile_2 = [] #(2)
    while pile_1 != []:
        x = pile_1.pop() #(3)
        if x >= 0:
            pile_2.append(x) #(4)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x) #(5)
    return pile_1
