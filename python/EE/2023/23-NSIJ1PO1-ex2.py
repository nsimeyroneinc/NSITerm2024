class Processus:
    def __init__(self,pid,duree):
        self.pid=pid
        self.duree=duree
        self.reste_a_faire=duree
        self.etat="Prêt"
        
    def execute_un_cycle(self):
        self.reste_a_faire-=1
        
    def change_etat(self,nouvel_etat):
        self.etat=nouvel_etat
        
    def est_termine(self):
        if self.reste_a_faire==0:
            return True
        else:
            return False
        
def tourniquet(liste_attente, quantum):
    ordre_execution = []
    while liste_attente != []:
        # On extrait le premier processus
        processus = liste_attente.pop(0)
        processus.change_etat("En cours d'exécution")
        compteur_tourniquet = 0
        print('1')
        while processus.reste_a_faire > 0 and compteur_tourniquet < quantum :
            print(ordre_execution)
            ordre_execution.append(processus.pid)
            processus.execute_un_cycle()
            print('info',processus.pid,processus.reste_a_faire)
            compteur_tourniquet = compteur_tourniquet + 1
        if processus.reste_a_faire != 0:
            processus.change_etat("Suspendu")
            liste_attente.append(processus)
        else:
            processus.change_etat("Terminé")
    return ordre_execution


liste_attente=[Processus(11,4),Processus(20,2),Processus(32,3)]

print(liste_attente)        

print(tourniquet(liste_attente,1))
    