notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]

def rangement_valeurs(notes):
    effectifs = [0]*11
    for note in notes:
        effectifs[note] += 1
    return effectifs

def notes_triees(effectifs_notes):
    note_triees = []
    for note in range(11):
        for i in range(effectifs_notes[note]):
            note_triees.append(note)
    return note_triees
