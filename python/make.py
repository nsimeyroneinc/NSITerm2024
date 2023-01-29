print("Création automatique des fichiers de corrections")
annee = input("Année ? ")
nb = input("Nombre de sujets dans la base ?")
for num in range(1,int(nb)+1):
    nom1 = f"{annee}-S{str(num).zfill(2)}-ex1.py"
    nom2 = f"{annee}-S{str(num).zfill(2)}-ex2.py"
    with open(nom1,"w") as f1:
        f1.write("def ")
    with open(nom2,"w") as f2:
        f2.write("def ")
