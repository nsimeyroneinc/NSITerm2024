def pantheon(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = [] #(1)
    for i in range(len(eleves)): #(2)
        if notes[i] == note_maxi:
            meilleurs_eleves.append(eleves[i]) #(3)
        elif notes[i] > note_maxi: 
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]] #(4)
    return (note_maxi, meilleurs_eleves)
