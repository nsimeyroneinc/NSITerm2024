import os
from cgitb import small
import csv

def define_env(env):
    "Hook function"
    
    env.variables['transversal']=["histoire","projet","typesconstruits","python"]
    env.variables['projet'] = {"icone":":fontawesome-solid-lightbulb:","style":"projet"}
    env.variables['devoir'] = {"icone":":fontawesome-solid-pen-to-square:","style":"devoir"}
    env.variables['BAC'] = {"icone":":fontawesome-solid-pen-to-square:","style":"BAC"}
    env.variables['typesconstruits'] = {"icone":":fontawesome-solid-cubes:","style":"typesconstruits"}
    env.variables['python'] = {"icone":":fontawesome-brands-python:","style":"python"}
    env.variables['themes']={
        "histoire":"Histoire de l'informatique",
        "projet":"Projet",
        "devoir":"Devoir",
        "BAC":"BAC",
        "sd":"Structures de données",
        "db":"Bases de données",
        "os":"Architectures matérielles, systèmes d'exploitation et réseaux",
        "algorithmique":"Algorithmique",
        "python":"Langages et programmation",
        "typesconstruits":"Types construits",
        "typesbase":"Types de base",
        "donneestable":"Données en table",
        "web":"Le web"
    }
    env.variables['icones'] = {
        "histoire":':fontawesome-solid-building-columns:{title="'+env.variables['themes']['histoire']+'"}',
        "projet":':fontawesome-solid-lightbulb:{title="'+env.variables['themes']['projet']+'"}',
        "devoir":':fontawesome-solid-pen-to-square:{title="'+env.variables['themes']['devoir']+'"}',
        "BAC":':fontawesome-solid-pen-to-square:{title="'+env.variables['themes']['BAC']+'"}',
        "sd":':fontawesome-solid-diagram-project:{title="'+env.variables['themes']['sd']+'"}',
        "db":':fontawesome-solid-database:{title="'+env.variables['themes']['db']+'"}',
        "os":':fontawesome-solid-microchip:{title="'+env.variables['themes']['os']+'"}',
        "algorithmique":':fontawesome-solid-gears:{title="'+env.variables['themes']['algorithmique']+'"}',
        "python":':fontawesome-brands-python:{title="'+env.variables['themes']['python']+'"}',
        "typesconstruits" : ':fontawesome-solid-cubes:{title="'+env.variables['themes']['typesconstruits']+'"}',
        "typesbase" : ':fontawesome-solid-cube:{title="'+env.variables['themes']['typesbase']+'"}',
        "donneestable" : ':fontawesome-solid-table-columns:{title="'+env.variables['themes']['donneestable']+'"}',
        "web" : ':material-web:{title="'+env.variables['themes']['web']+'"}'

    }
    env.variables['icones_exo']={
        "dur": ":fontawesome-solid-bomb:{title='Exercice difficile'}",
        "rappel": ":fontawesome-solid-clock-rotate-left:{title='Retour sur des notions antérieures'}",
        "recherche": ":fontawesome-solid-search:{title='Exercice de recherche'}",
        "capacite": ":fontawesome-solid-puzzle-piece:{title='Exercice testant une capacité du chapitre'}",
        "python": ":fontawesome-brands-python:{title='Exercice en lien avec la programmation en Python'}",
        "bac": ":fontawesome-solid-graduation-cap:{title='Exercice extrait du Bac'}",
        "maths": ":fontawesome-solid-infinity:{title='Exercice en lien avec les mathématiques'}"
    }
    env.variables['icones_act']={
        "rappel": ":material-history:{title='Retour sur des notions antérieures'}",
        "recherche": ":fontawesome-solid-search:{title='Activité de recherche'}",
        "oral": ":fontawesome-solid-comments:{title='Activité oral'}",
        "papier": ":material-file-edit-outline:{title='Activité à réaliser sur feuille'}",
        "vscode": ":material-microsoft-visual-studio-code:{title='Activité utilisant VS Code'}",
        "video": ":fontawesome-solid-film:{title='Activité utilisant un support vidéo'}",
        "notebook": ":fontawesome-solid-book:{title='Activité utilisant un jupyter notebook'}",
        "python": ":fontawesome-brands-python:{title='Activité en lien avec la programmation en Python'}",
        "maths": ":fontawesome-solid-infinity:{title='Activité en lien avec les mathématiques'}"
    }

    env.variables['devant_exo']=':black_small_square:'
    env.variables['devant_act']=':black_small_square:'
    env.variables['num_exo']=1
    env.variables['num_act']=1

    env.variables['progression_terminale']={
        1 : ["db","Le Modéle relationnel",1,"BasesDonnees/Modele_Relationnel.md"],
        2 : ["python","Langage SQL",2,"BasesDonnees/Cours_TP_SQL.md"],
        3 : ["python","Récursivité",1,"Programmation/T1_1_Recursivite.md"],
        4 : ["sd","Programmation Orientée Objet",2,"StructureDonnees/T1_1_Programmation_Orientee_Objet.md"],
        5 : ["os","Listes et Piles",2,"StructureDonnees/T2_1_Listes_Piles_et_Files.md"],
        6 : ["os","Protocole de routage",1,"Archi_Materielle/T3_1_Routage.md"],
        7 : ["algorithmique","Algorithmes de tri",1,"Algo/T5_2_algo_tri.md"],
        8 : ["algorithmique","Diviser pour régner",1,"Algo/T5_3_Diviser_pour_regner.md"],
        9 : ["sd","Les Dictionnaires - Révision",1,"StructureDonnees/T4_1_Dictionnaires.md"],
        10 : ["sd","Les arbres",2,"StructureDonnees/T3_1_arbre.md"],
        11: ["algorithmique","Algorithmes sur les arbres",2,"Algo/TP5_5_Implementation_arbres.md"],
        12: ["algorithmique","arbres binaires de recherche",1,"StructureDonnees/T3_3_arbre_recherche.md"],
        13 : ["os","Gestion Processus",1,"Archi_Materielle/T3_2_gestion_processus.md"],
        #7 : ["python","Notions de programmation orienté objet",2,"poo.md"],
        #8 : ["sd","Structures de données linéaires",2,"sl.md"],
        #9 : ["os","Système sur puce",1,"puces.md"],
        #10 : ["sd","Arbres",2,"arbres.md"],
        #11 : ["db","Schéma relationnel d'une base de données",2,"sgbd.md"],
        #12: ["algorithmique","Algorithmes sur les arbres",2,"algoarbre.md"],
        #13: ["sd","Graphes",2,"graphes.md"],
        #14: ["os","Protocoles de routage",2,"routage.md"],
        15: ["algorithmique","k-plus proches voisins",1,"Algo/TP6_1_kppv.md"],
        #15: ["algorithmique","Recherche textuelle",2,"texte.md"],
        #16: ["python","Calculabilité, décidabilité",2,"calculabilite.md"],
        #17: ["os","Sécurisation des communications",2,"cryptographie.md"],
        #18:["python","Récursivité",2,"Programmation/T1_1_Recursivite.md"],
        19 : ["sd","Les dictionnaires",1,"StructureDonnees/T4_2_dictionnaires.md"],
        20: ["os","Cryptographie",1,"Projet/cryptographie2.md"],
        21: ["os","Système à puces",1,"Archi_Materielle/T3_5_systeme_sur_puce.md"],
        22: ["sd","Les Graphes",2,"Graphe/TD_Graphe.md"],
        23: ["sd","Les Graphes - Parcours",2,"Graphe/TD_Graphe_Parcours.md"],
        24: ["sd","Les Graphes - Exercices",2,"Graphe/TD_Graphe_Exercices.md"]
    }

    env.variables['devoir_terminale']={
        1 : ["devoir","Langage SQL","","Evaluations/BDD_Devoir_Corrige.md"],
        #2 : ["devoir","Pile-File et Protocole de Routage",'16/11/2023',"Evaluations/DS_Pile_File_Routage.md"],
        3 : ["devoir","Pile-File et Protocole de Routage",'16/11/2023',"Evaluations/DS_Pile_File_Routage.md"],
        4 : ["devoir","Les tris - Diviser pour régner","02/12/2023","Evaluations/DS_Diviser_pour_regner_tris.md"],
        5 : ["devoir","Les arbres binaires","16/12/2023","Evaluations/DS_Arbres.md"],
        6 : ["devoir","Gestion Processus","19/01/2023","Evaluations/DS0110.md"]
        #6 : ["os","Protocole de routage",1,"Archi_Materielle/T3_1_Routage.md"],
        #7 : ["algorithmique","Algorithmes de tri",1,"Algo/T5_2_algo_tri.md"],
        #8 : ["algorithmique","Diviser pour régner",1,"T5_2_Diviser_pour_regner.md"]
        #6 : ["os","Protocole de Routage",1,""],
        #7 : ["python","Notions de programmation orienté objet",2,"poo.md"],
        #8 : ["sd","Structures de données linéaires",2,"sl.md"],
        #9 : ["os","Système sur puce",1,"puces.md"],
        #10 : ["sd","Arbres",2,"arbres.md"],
        #11 : ["db","Schéma relationnel d'une base de données",2,"sgbd.md"],
        #12: ["algorithmique","Algorithmes sur les arbres",2,"algoarbre.md"],
        #13: ["sd","Graphes",2,"graphes.md"],
        #14: ["os","Protocoles de routage",2,"routage.md"],
        #15: ["algorithmique","Recherche textuelle",2,"texte.md"],
        #16: ["python","Calculabilité, décidabilité",2,"calculabilite.md"],
        #17: ["os","Sécurisation des communications",2,"cryptographie.md"],
        #18:["python","Récursivité",2,"Programmation/T1_1_Recursivite.md"],
        #19 : ["algorithmique","Diviser pour régner",1,"diviser.md"]
    }

    env.variables['BAC_terminale']={
        #1 : ["devoir","Langage SQL","","Evaluations/BDD_Devoir_Corrige.md"],
        #2 : ["devoir","Pile-File et Protocole de Routage",'16/11/2023',"Evaluations/DS_Pile_File_Routage.md"],
        3 : ["db","Langage SQL","SQL","BasesDonnees/SQL_BAC_correction.md"],
        #3 : ["python","Récursivité",1,"Programmation/T1_1_Recursivite.md"],
        4 : ["sd","Programmation Orientée Objet","P.O.O","StructureDonnees/POO_BAC_correction.md"],
        5 : ["sd","Piles et Files","Struc. Données","StructureDonnees/T2_2_Pile_File_BAC_Correction.md"],
        6 : ["os","Protocole de routage","Réseaux","Archi_Materielle/T3_1_Routage_BAC_Correction.md"],
        #7 : ["algorithmique","Algorithmes de tri",1,"Algo/T5_2_algo_tri.md"],
        #8 : ["algorithmique","Diviser pour régner",1,"T5_2_Diviser_pour_regner.md"]
        #6 : ["os","Protocole de Routage",1,""],
        #7 : ["python","Notions de programmation orienté objet",2,"poo.md"],
        8 : ["algorithmique","Diviser pour régner","Algo","Algo/T5_4_Diviser_pour_regner_BAC.md"],
        10 : ["sd","Les arbres - Partie 1","Struc. Données","StructureDonnees/T3_2_arbre_BAC.md"],
        11 : ["algorithmique","Algorihtmes Arbres Binaires","Implémentation arbres binaires","Algo/T5_6_algo_arbre_BAC.md"],
        12 : ["algorithmique","Arbres Binaires de Recherche","ABR","StructureDonnees/T3_4_arbre_recherche_BAC.md"],
        #12: ["algorithmique","Algorithmes sur les arbres",2,"algoarbre.md"],
        13: ["os","Gestion Processus","Processus","Archi_Materielle/T3_3_gestion_processus_BAC.md"],
        14: ["sd","Piles et Files","Struc. Données","BAC/pile_file/compilation_pile_file.md"],
        15: ["algorithmique","k-plus proches voisins",1,"Algo/TP6_1_kppv.md"],
        16: ["python","Récursivité",'Programmation',"BAC/recursivite/compile_recursivite.md"],
        17: ["python","Programmation - Tableaux","Python","BAC/programmation/compilation_programmation.md"],
        18: ["db","SQL","SQL","BAC/SQL/compile_sql.md"]
        #19 : ["algorithmique","Diviser pour régner",1,"diviser.md"]
    }

    @env.macro
    def capytale(id):
        lien = "[![logo capytale](./images/capytale.png){.imgcentre width=150px border=2px}]"
        lien +=f"(https://capytale2.ac-paris.fr/web/c/{id})"
        lien += "{target=_blank}"
        return lien

    @env.macro
    def icone(theme):
        return env.variables.icones[theme]

    @env.macro
    def affiche_progression(niveau):
        ret='''
| |Titre        | Durée |
|-|-------------|-------|
        '''
        if niveau=="premiere":
            var_progression = env.variables.progression_premiere
        else:
            var_progression = env.variables.progression_terminale
        for k in var_progression:
           ret+=chapitre(k,env.variables['progression_'+niveau][k][0],env.variables['progression_'+niveau][k][1],env.variables['progression_'+niveau][k][2],env.variables['progression_'+niveau][k][3])
        return ret
    
    @env.macro
    def genere_nav():
        ret='''```\n'''
        for k in env.variables.progression:
            da = env.variables['progression'][k]
            ret+=f'  - "C{k}-{da[1]}" : {da[3]}\n'
        return ret+'```\n'
#---------------- <exo perso>-------------------- 
    with open("qcm.csv","r",encoding="utf-8") as f:
        questions = list(csv.DictReader(f,delimiter=","))
    env.variables['qcm']=questions

    @env.macro
    def affiche_question(num,index):
        lenonce = env.variables.qcm[num]["enonce"]
        # Traitement si enoncé sur plusieurs lignes
        nl = lenonce.find('\n')
        if nl>0:
            lenonce=lenonce.replace("\n",'"\n',1)
            lenonce=lenonce.replace("\n",'\n    ')
        else:
            lenonce+='"'
        # Traitement si image
        limg = env.variables.qcm[num]["image"]
        if limg!='':
            lenonce+=f'\n \t ![illustration](./images/C{env.variables.qcm[num]["chapitre"]}/{limg})'
            lenonce+='{: .imgcentre}\n'
        modele = f'''
!!! fabquestion "**{index}.** {lenonce}
    === "Réponses"
        - [ ] a) {env.variables.qcm[num]["reponseA"]}
        - [ ] b) {env.variables.qcm[num]["reponseB"]}
        - [ ] c) {env.variables.qcm[num]["reponseC"]}
        - [ ] d) {env.variables.qcm[num]["reponseD"]}
    === "Correction"\n'''
        for rep in "ABCD":
            clerep = "reponse"+rep
            if env.variables.qcm[num]["bonne_reponse"]==rep:
                modele+=f"        - [x] {rep.lower()}) =={env.variables.qcm[num][clerep]}== \n"
            else:
                modele+=f"        - [ ] {rep.lower()}) ~~{env.variables.qcm[num][clerep]}~~ \n"
        return modele

    @env.macro
    def affiche_qcm(liste_question):
        qcm = ""
        for index in range(len(liste_question)):
            qcm+=affiche_question(liste_question[index],index+1)
        return qcm
    
    @env.macro
    def qcm_chapitre(num_chap):
        index=1
        qcmc=""
        for num in range(len(env.variables.qcm)):
            if int(env.variables.qcm[num]["chapitre"])==num_chap:
                qcmc+=affiche_question(num,index)
                index+=1
        return qcmc

#---------------------------------------------- QCM sans réponse ---------------------------

    with open("qcm_devoir.csv","r",encoding="utf-8") as f:
        questions_devoir = list(csv.DictReader(f,delimiter=","))
    env.variables['qcm_devoir']=questions_devoir

    @env.macro
    def affiche_question_devoir(num,index):
        lenonce = env.variables.qcm_devoir[num]["enonce"]
        # Traitement si enoncé sur plusieurs lignes
        nl = lenonce.find('\n')
        if nl>0:
            lenonce=lenonce.replace("\n",'"\n',1)
            lenonce=lenonce.replace("\n",'\n    ')
        else:
            lenonce+='"'
        # Traitement si image
        limg = env.variables.qcm[num]["image"]
        if limg!='':
            lenonce+=f'\n \t ![illustration](./images/C{env.variables.qcm_devoir[num]["chapitre"]}/{limg})'
            lenonce+='{: .imgcentre}\n'
        modele = f'''
!!! fabquestion "**{index}.** {lenonce}
    - [ ] a) {env.variables.qcm_devoir[num]["reponseA"]}
    - [ ] b) {env.variables.qcm_devoir[num]["reponseB"]}
    - [ ] c) {env.variables.qcm_devoir[num]["reponseC"]}
    - [ ] d) {env.variables.qcm_devoir[num]["reponseD"]}
'''
        return modele

    @env.macro
    def affiche_qcm_devoir(liste_question_devoir):
        qcm_devoir = ""
        for index in range(len(liste_question_devoir)):
            qcm_devoir+=affiche_question_devoir(liste_question_devoir[index],index+1)
        return qcm_devoir
    
    @env.macro
    def qcm_chapitre_devoir(num_chap):
        index=1
        qcmc=""
        for num in range(len(env.variables.qcm_devoir)):
            if int(env.variables.qcm_devoir[num]["chapitre"])==num_chap:
                qcmc+=affiche_question_devoir(num,index)
                index+=1
        return qcmc
#-------------------------------------    

    @env.macro
    def exo(titre,licones,numero=1):
        if numero==0:
            env.variables['num_exo']=1
        ligne=f"### {env.variables['devant_exo']}   Exercice {env.variables['num_exo']} "
        if titre!="":
            ligne+=f": *{titre}*"
        if licones!=[]:
            ligne+=f"<span style='float:right;'>"
            for icone in licones:
                ligne+=f"<span style='float:right;'>&thinsp; {env.variables['icones_exo'][icone]}</span>"
            ligne+="</span>"
        env.variables['num_exo']=env.variables['num_exo']+1
        return ligne
    # Titres des items travaillés sur l'année
    @env.macro
    def sec_titre(theme,titre):
            icone = env.variables.icones[theme]
            return f"### {icone} &nbsp; {titre}"

    @env.macro
    def cours(fichier):
        ccours = '''
Vous pouvez télécharger une copie au format pdf du diaporama de synthèse de cours :

<span class='centre'>[Diaporama de cours :fontawesome-regular-file-pdf:](../pdf/'''+fichier+'''){.md-button target=_blank}</span>
!!! warning "Attention"
    Ce diaporama n'est qu'une synthèse de cours et ne donne que quelques points de repères pour de vos révisions.'''
        return ccours

    @env.macro
    def aff_cours(num):
        fichier=f'../../pdf/C{num}/C{num}-cours.pdf'
        return cours(fichier)
    @env.macro
    def correction(bool, texte):
        if bool == False:
            return ""
        else:
            return texte

    @env.macro
    def sc(chaine):
        return f'<span style="font-variant:small-caps;">{chaine}</span>'

    @env.macro
    def chapitre(num,theme,titre,duree,lien):
        icone = env.variables["icones"][theme]
        return f"|{icone}|[C{num}- {titre}]({lien}) | {duree}\n"


#------------------DEVOIRS--------------------------
    @env.macro
    def devoir(num,theme,titre,duree,lien):
        icone = env.variables["icones"][theme]
        return f"|{icone}|[DS {num}- {titre}]({lien}) | {duree}\n" 


    @env.macro
    def sec_devoir(theme,devoir):
            icone = env.variables.icones[theme]
            return f"### {icone} &nbsp; {devoir}"

    @env.macro
    def devoir_chapitre(numero,devoir,theme,niveau):
        # Position de l'ancre pour repérage dans la page
        titre_bis = env.variables['devoir_'+niveau][numero][1]
        ligne=f"# <span class='numdevoir'>Devoir-{numero}</span> {titre_bis} "
        ligne+=f"<span style='float:right;'>{env.variables.icones[theme]}</span>"
        return ligne

    @env.macro
    def affiche_devoir(niveau):
        ret='''
| |Devoir       | Le  |
|-|-------------|-------|
        '''
        if niveau=="premiere":
            var_projet = env.variables.devoir_premiere
        else:
            var_projet = env.variables.devoir_terminale
        for k in var_projet:
           ret+=devoir(k,env.variables['devoir_'+niveau][k][0],env.variables['devoir_'+niveau][k][1],env.variables['devoir_'+niveau][k][2],env.variables['devoir_'+niveau][k][3])
        return ret

#--------------------------------------------------------------------------------------        


#------------------BAC--------------------------
    @env.macro
    def BAC(num,theme,titre,duree,lien):
        icone = env.variables["icones"][theme]
        return f"|{icone}|[Sujet BAC {num}- {titre}]({lien}) | {duree}\n" 


    @env.macro
    def sec_BAC(theme,BAC):
            icone = env.variables.icones[theme]
            return f"### {icone} &nbsp; {BAC}"

    @env.macro
    def devoir_chapitre(numero,devoir,theme,niveau):
        # Position de l'ancre pour repérage dans la page
        titre_bis = env.variables['BAC_'+niveau][numero][1]
        ligne=f"# <span class='numBAC'>Sujet BAC-{numero}</span> {titre_bis} "
        ligne+=f"<span style='float:right;'>{env.variables.icones[theme]}</span>"
        return ligne

    @env.macro
    def affiche_BAC(niveau):
        ret='''
| |BAC      | Le  |
|-|-------------|-------|
        '''
        if niveau=="premiere":
            var_projet = env.variables.BAC_premiere
        else:
            var_projet = env.variables.BAC_terminale
        for k in var_projet:
           ret+=BAC(k,env.variables['BAC_'+niveau][k][0],env.variables['BAC_'+niveau][k][1],env.variables['BAC_'+niveau][k][2],env.variables['BAC_'+niveau][k][3])
        return ret

#--------------------------------------------------------------------------------------        

    
    @env.macro
    def initexo(n):
        env.variables['compteur_exo'] = n
        return ""


    env.variables['nchap']=0
    env.variables['nelements']=0
    with open("exo_bac.csv","r",encoding="utf-8") as f:
        exo_bac = list(csv.DictReader(f,delimiter=","))
    env.variables['exo_bac']=exo_bac
    
    # Les sujets de bac avant 2023 (format 5 exos)
    with open("sujet_bac.csv","r",encoding="utf-8") as f:
        sujet_bac_5exos = list(csv.DictReader(f,delimiter=";"))
        sujet_bac_5exos = sorted(sujet_bac_5exos,key = lambda x : x['Repere'])
    env.variables['sujet_bac']=sujet_bac_5exos

    # Les sujets de bac après 2022 (format 3 exos)
    with open("sujet_bac2.csv","r",encoding="utf-8") as f:
        sujet_bac_3exos = list(csv.DictReader(f,delimiter=";"))
        sujet_bac_3exos = sorted(sujet_bac_3exos,key = lambda x : x['Repere'])
    env.variables['sujet_bac']=sujet_bac_3exos


    env.variables['compteur_exo'] = 0
    @env.macro
    def exercice():
        env.variables['compteur_exo'] += 1
        return f"Exercice  { env.variables['compteur_exo']}"

    @env.macro
    def liens(fichier,type=".pdf"):
        location="./pdf/"+fichier[0:2]+"/"
        return f"[:fontawesome-solid-download:]({location}{fichier}.pdf) [:fontawesome-regular-file:]({location}{fichier}.tex)"

    @env.macro
    def telecharger(description,fichier):
        liens =f"[{description} :material-download:](./{fichier})"
        liens+="{.md-button}"
        return "<span class='centre'>"+liens+"</span>"
#---------------- </exo perso>-------------------- 
    @env.macro
    def relation(nom, primaire, *reste) -> str:
        return f'<code><strong>{nom}</strong> (<span class="cle_primaire">{primaire}</span>, {", ".join(reste)})</code>'

    @env.macro
    def table_cle(table, cle) -> str:
        return f'<code><strong>{table}</strong>.{cle}</code>'

    @env.macro
    def sc(chaine):
        return f'<span style="font-variant:small-caps;">{chaine}</span>'
    
    env.variables['devant_act']=':black_small_square:'
    env.variables['num_act']=1
    @env.macro
    def titre_activite(titre,licones,numero=1):
        if numero==0:
            env.variables['num_act']=1
        ligne=f"### {env.variables['devant_act']}   Activité {env.variables['num_act']} "
        if titre!="":
            ligne+=f": *{titre}*"
        if licones!=[]:
            ligne+=f"<span style='float:right;'>"
            for icone in licones:
                ligne+=f"<span style='float:right;'>&thinsp; {env.variables['icones_act'][icone]}</span>"
            ligne+="</span>"
        env.variables['num_act']=env.variables['num_act']+1
        return ligne

    @env.macro
    def script(lang: str, nom: str, indentation=0, stop="") -> str:
        """Renvoie le script dans une balise bloc avec langage spécifié

        - lang: le nom du lexer pour la coloration syntaxique
        - nom: le chemin du script relativement au .md d'appel
        - indentation: nb d'espaces pour l'insertion dans un environnement
        - stop: si cette ligne est rencontrée, elle n'est pas affichée, ni la suite
        """
        # par Franck Chambon
        sortie = []
        with open("docs/" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"/{nom}", 'r') as f:
            for line in f.readlines():
                if line.upper().strip() == stop:
                    break
                nb_agc = 0 # nb accents graves consécutifs
                maxi_agc = 0
                for c in line:
                    if c == '`':
                        nb_agc += 1
                        if nb_agc > maxi_agc: maxi_agc = nb_agc
                    else:
                        nb_agc = 0
                sortie.append(" " * indentation + line)
        n = max(3, 1 + nb_agc)
        sortie = ["`" * n + lang + "\n"] + sortie
        sortie.append(" " * indentation + "`" * n + "\n")
        return "".join(sortie)


    @env.macro
    def py(nom: str, indentation=0, stop="") -> str:
        "macro python rapide"
        return script('python', nom + ".py", indentation, stop)

    @env.macro
    def py_sujet(nom: str, indentation=0, stop="# TESTS") -> str:
        "macro python rapide, pour un sujet sans les tests"
        return script('python', nom + ".py", indentation, stop)


    @env.macro
    def numworks():
        return f"""<iframe src="{env.variables.scripts_url}numworks/simulator.html" width="100%" height="500"></iframe>"""

    @env.macro
    def python_carnet(carnet: str = '', aux: str = '', module: str = '',
                      auxs=None, modules=None,
                      hauteur: int = 700,
                      chemin_relatif: bool = True,
                     ) -> str:
        """Renvoie du HTML pour embarquer un fichier `carnet.ipynb` dans un notebook
        + Basthon est la solution 2021, RGPD ok
        """

        if chemin_relatif:
            chemin = env.variables.site_url + os.path.dirname(env.variables.page.url.rstrip('/'))+'/'
        else:
            chemin = env.variables.scripts_url

        lien = f"https://notebook.basthon.fr/?"
        if carnet != '':
            lien += f"from={chemin}{carnet.lstrip('./')}&"
        else:
            lien += f"from={env.variables.scripts_url}py_vide.ipynb&"
        
        if aux != '':
            lien += f"aux={chemin}{aux.lstrip('./')}&"
        if auxs is not None:
            for aux in auxs:
                lien += f"aux={chemin}{aux.lstrip('./')}&"
        
        if module != '':
            lien += f"module={chemin}{module.lstrip('./')}&"
        if modules is not None:
            for module in modules:
                lien += f"module={chemin}{module.lstrip('./')}&"
        
        return f"<iframe src={lien} width=100% height={hauteur} onload=\"window.scrollTo({{ top: 0, behavior: 'smooth' }});\"></iframe>" + \
                f"[Lien dans une autre page]({lien}){{target=_blank}}"
    
    @env.macro
    def python_ide(script: str = '', aux: str = '', module: str = '',
                      auxs=None, modules=None,
                      hauteur: int = 700,
                      chemin_relatif: bool = True,
                     ) -> str:
        """Renvoie du HTML pour embarquer un fichier `script` dans une console
        + Basthon est la solution 2021, RGPD ok
        """

        if chemin_relatif:
            chemin = env.variables.site_url + os.path.dirname(env.variables.page.url.rstrip('/'))+'/'
        else:
            chemin = env.variables.scripts_url

        lien = f"https://console.basthon.fr/?"
        if script != '':
            lien += f"from={chemin}{script.lstrip('./')}&"
        else:
            lien += f"script=eJwDAAAAAAE"
        
        if aux != '':
            lien += f"aux={chemin}{aux.lstrip('./')}&"
        if auxs is not None:
            for aux in auxs:
                lien += f"aux={chemin}{aux.lstrip('./')}&"
        
        if module != '':
            lien += f"module={chemin}{module.lstrip('./')}&"
        if modules is not None:
            for module in modules:
                lien += f"module={chemin}{module.lstrip('./')}&"
        
        return f"<iframe src={lien} width=100% height={hauteur} onload=\"window.scrollTo({{ top: 0, behavior: 'smooth' }});\"></iframe>" + \
                f"[Lien dans une autre page]({lien}){{target=_blank}}"
    

    @env.macro
    def console(hauteur : int = 200) -> str:
        return "[Console pyodide, dernière en date](https://pyodide.org/en/stable/console.html){target=_blank}"

#------ Marcro sujet EP------
    @env.macro
    def titre_chapitre(numero,titre,theme,niveau):
        # Position de l'ancre pour repérage dans la page
        if theme=="devoir":
            titre_bis = env.variables['devoir_'+niveau][numero][1]
            ligne=f"# <span class='numdevoir'>Devoir {numero} : </span>  {titre_bis} "
            ligne+=f"<span style='float:right;'>{env.variables.icones[theme]}</span>"
        elif theme=="BAC":
            titre_bis = env.variables['BAC_'+niveau][numero][1]
            ligne=f"# <span class='numBAC'>Sujet BAC {numero} : </span> &nbsp; {titre_bis} "
            ligne+=f"<span style='float:right;'>{env.variables.icones[theme]}</span>"
        else:
            titre_bis = env.variables['progression_'+niveau][numero][1]
            ligne=f"# <span class='numchapitre'>C{numero}</span> {titre_bis} "
            ligne+=f"<span style='float:right;'>{env.variables.icones[theme]}</span>"
        return ligne
    

    @env.macro
    def titre_correction(annee,numero):
        ligne=f"# Corrigé sujet <span class='numchapitre'>{numero}</span> - Année : {annee} "
        return ligne
    
    @env.macro
    def correction_ex1(annee,numero):
        modele = f'''
```python3 linenums="1" \n
--8<-- "python/{annee}/{annee}-S{numero}-ex1.py"\n
```\n'''
        return modele
    
    @env.macro
    def correction_ex2(annee,numero,hl):
        modele = f'''
```python3 linenums="1" hl_lines="{hl}"\n
--8<-- "python/{annee}/{annee}-S{numero}-ex2.py"\n\n
```'''
        return modele
#------------------EP enonce test


    @env.macro
    def titre_enonce(annee,numero):
        ligne=f"# Enoncé sujet <span class='numchapitre'>{numero}</span> - Année : {annee} "
        return ligne
    
    @env.macro
    def enonce_ex1(annee,numero):
        modele = f'''
```python3 linenums="1" \n
--8<-- "python/{annee}/{annee}-S{numero}-ex1.py"\n
```\n'''
        return modele
    
    @env.macro
    def enonce_ex2(annee,numero,hl):
        modele = f'''
```python3 linenums="1" hl_lines="{hl}"\n
--8<-- "python/{annee}/{annee}-S{numero}-ex2.py"\n\n
```'''
        return modele
    
#------------EP provisoire
    @env.macro
    def ep2023(annee):
        aff="\n"
        aff+= "|Numéro | Lien de téléchargement| Thème exercice 1 | Thème exercice 2  | Code fourni |Correction|\n"
        aff+= "|-------|-------------------|------------------|-------------------|-------------|----------|\n"
        FNAME = f"./docs/officiels/Annales/EP/{annee}/l{annee}.txt"
        icones = {"N":":star:","B":"<span class='rouge'>:material-bug:</span>","D":"<span class='navy'>:material-bomb:</span>","M":":fontawesome-solid-square-root-variable:","W":"<span class='orange'>:fontawesome-solid-triangle-exclamation:</span>"}
        with open(FNAME,"r",encoding="utf-8") as f:
            nums=1
            for s in f:
                lf=s.split(",")
                if '0' in lf[3]:
                    correction = f"Voir 2022"
                else:
                    correction = f"[{annee}-S{str(nums).zfill(2)}](../../Corriges/{annee}-S{str(nums).zfill(2)}/)"
                    enonce = f"[{annee}-S{str(nums).zfill(2)}-ex1](../../../officiels/Annales/EP/{annee}/{annee}-S{str(nums).zfill(2)}/)"
                    #enonce2 = f"[{annee}-S{str(nums).zfill(2)}](../../../officiels/Annales/EP/{annee}/{annee}-S{str(nums)_2)/{enonce}.zfill(2)}/)"
                dnums ="**" +str(nums)+"** "
                for letter in icones:
                    if letter in lf[5]:
                        dnums = dnums + icones[letter]
                aff+=f"|{dnums}| [Sujet N°{nums}](../../../officiels/Annales/EP/{annee}/{lf[0]}/{lf[0]}.pdf) | {lf[2]} | {lf[3]} | [:material-download: Code](../../officiels/Annales/EP/{annee}/{lf[0]}/{lf[0]}.py) | {correction} |\n"
                nums+=1
        return aff

    @env.macro
    def enonce_ep2023(annee,numero):
        code = f'{str(annee)[-2:]}-NSI-{numero}'
        return f"<span class='centre'>[Sujet {numero} - 2023 :material-download:](../../officiels/Annales/EP/{annee}/{code}/{code}.pdf)"+"{.md-button}</span>"
#-------------------------------------

    @env.macro
    def ep(annee):
        aff="\n"
        aff+= "|Numéro | Lien de téléchargement| Thème exercice 1 | Thème exercice 2  | Code fourni |Correction|\n"
        aff+= "|-------|-----------------------|------------------|-------------------|-------------|----------|\n"
        FNAME = f"./docs/officiels/Annales/EP/{annee}/l{annee}.txt"
        with open(FNAME,"r",encoding="utf-8") as f:
            nums=1
            for s in f:
                lf=s.split(",")
                if lf[-1][0]=='0':
                    correction = f"[Sur Pixees](https://pixees.fr/informatiquelycee/term/ep/s{nums}.html)"+"{target=_blank}"
                else:
                    correction = f"[{annee}-S{str(nums).zfill(2)}](../../Corriges/{annee}-S{str(nums).zfill(2)}/)"
                aff+=f"|{nums}|[Sujet N°{nums}](../../officiels/Annales/EP/{annee}/{lf[0]}/{lf[0]}.pdf) | {lf[1]} | {lf[2]} | [:material-download: Code](../../officiels/Annales/EP/{annee}/{lf[0]}/{lf[0]}.py) | {correction} |\n"
                nums+=1
        return aff

    @env.macro
    def enonce_ep(annee,numero):
        code = f'{str(annee)[-2:]}-NSI-{numero}'
        return f"<span class='centre'>[Sujet {numero} - 2022 :material-download:](../../officiels/Annales/EP/{annee}/{code}/{code}.pdf)"+"{.md-button}</span>"

    
    @env.macro
    def code_insert(chap,nom,ntab=0):
        stab = '\t'*ntab
        modele = f'''
{stab}```python3 linenums="1" \n
{stab}--8<-- "python/C{chap}/{nom}"\n
{stab}```'''
        return modele

    @env.macro
    def correction_exobac(repere,numero):
            aff = f"# <span class='reperesujet'>{repere}</span> Correction exercice <span class='numchapitre'>{numero}</span> \n"
            index = 0
            while index<len(env.variables.exo_bac) and (env.variables.exo_bac[index]["Repere"]!=repere or env.variables.exo_bac[index]["Numero"]!=str(numero)):
                index += 1
            if index<len(env.variables.exo_bac):
                exo = env.variables.exo_bac[index]
                aff += f"Année : {exo['Annee']} &#8212; Jour : {exo['Jour']} <br>"
                aff += f"Centre : {exo['Centre']} <br>"
                aff += f"Thème : **{exo['Theme']}** <br> \n"
                aff += f"## Enoncé \n"
                aff += telecharger(f'Enoncé {repere} - Ex {numero}',f'../../Enoncés/{repere}-{numero}.pdf')
                aff += "\n"
                aff += "## Correction \n"
            return aff            

    @env.macro
    def ok():
        return ":fontawesome-solid-check:{.vert title='Compatible'}"
    
    @env.macro
    def nok():
        return ":fontawesome-solid-xmark:{.rouge title='Non compatible'}"
        
    @env.macro
    def correction_ecrit(annee):
        liste_repere = set(sujet["Repere"] for sujet in env.variables.exo_bac if sujet['Annee']==annee)
        aff = f"#<span class='numchapitre'>{annee}</span> Correction épreuves écrites\n"
        for repere in liste_repere:
            index = 0
            while index<len(env.variables.exo_bac) and env.variables.exo_bac[index]["Repere"]!=repere:
                index += 1
            centre = env.variables.exo_bac[index]["Centre"]
            jour = env.variables.exo_bac[index]["Jour"]
            aff += f"## {repere} : {centre} - Jour {jour} \n"
            for num_exo in range(1,6):
                index = 0
                while index<len(env.variables.exo_bac) and (env.variables.exo_bac[index]["Repere"]!=repere or env.variables.exo_bac[index]["Numero"]!=str(num_exo)):
                    index += 1
                aff += f"* Exercice {num_exo} : "
                exo = env.variables.exo_bac[index]
                if exo["Correction"]=='1':
                    aff += ":fontawesome-solid-check:{.vert title='Compatible'}"
                    aff+= f"[{exo['Theme']}](../Corriges/{repere}-{num_exo}) \n"
                else:
                    aff+= ":fontawesome-solid-xmark:{.rouge title='Non disponible'}"
                    aff+= f"{exo['Theme']}\n"
            aff+= '\n \n'
        return aff
    
    @env.macro
    def corrige_ecrit(annee):
        aff = f"#<span class='numchapitre'>{annee}</span> Correction épreuves écrites\n"
        return aff
    
    @env.macro
    def corrige_ecrit(annee):
        if int(annee)<2023:
            nb_exos,sujet_bac = 5,sujet_bac_5exos
        else:
            nb_exos,sujet_bac = 3,sujet_bac_3exos
        aff = f"#<span class='numchapitre'>{annee}</span> Correction épreuves écrites\n \n"
        aff += ''' 

!!! note "Remarques :" 
    * les sujets sont classés dans l'ordre alphabétique de leur repère,  
    * si un exercice est corrigé son numéro est indiqué en vert, sinon en rouge

'''
        aff+= "|Repère | Centre | Jour | Téléchargement |Correction|\n"
        aff+= "|-------|--------|------|----------------|----------|\n"
        for s in sujet_bac:
            if s['Annee']==annee:
                corr = ''
                for num in range(1,nb_exos+1):
                    if s["Correction"][num-1]=="1":
                        corr += ":material-numeric-"+str(num)+"-circle-outline:{.vert title='exercice"+str(num)+"corrigé'}"
                    else:
                        corr += ":material-numeric-"+str(num)+"-circle-outline:{.rouge title='exercice"+str(num)+"non corrigé'}"
                aff+=f"|{s['Repere']}|{s['Centre']}|{s['Jour']}|[{s['Repere']}](../../officiels/Annales/EE/{annee}/{s['Repere']}.pdf)|[{corr}](../../Corriges/{s['Repere']})|\n"
        return aff
    
    @env.macro
    def corrige_exo(repere,numero):
        aff = f"#<span class='numchapitre'>{repere}</span> Correction épreuves écrites\n"
        return aff
    
    @env.macro
    def liste_sujets(annee):
        if int(annee)<2023:
            nb_exos,sujet_bac = 5,sujet_bac_5exos
        else:
            nb_exos,sujet_bac = 3,sujet_bac_3exos
        aff = ""
        for s in sujet_bac:
            if s['Annee']==annee:
                aff+=f"##{s['Centre']} - jour {s['Jour']} : <a id={s['Repere']}>*{s['Repere']}*</a>\n"
                aff+=f"### Enoncé \n"
                aff+=telecharger(s['Repere'],f"../../officiels/Annales/EE/{annee}/{s['Repere']}.pdf")
                aff+='\n \n'
                for i in range(1,nb_exos+1):
                    if nb_exos==3:
                        aff+=f"* **Exercice {i} [{s['Pts'+str(i)]} points]** : *{s['Ex'+str(i)]}* \n \n"
                    else:
                        aff+=f"* **Exercice {i} ** : *{s['Ex'+str(i)]}* \n \n"
                corr = ""
                for num in range(1,nb_exos+1):
                    if s["Correction"][num-1]=="1":
                        corr += ":material-numeric-"+str(num)+"-circle-outline:{.vert title='exercice "+str(num)+" corrigé'}"
                    else:
                        corr += ":material-numeric-"+str(num)+"-circle-outline:{.rouge title='exercice "+str(num)+" non corrigé'}"                
                corr = f"### Correction  [{corr}](../../Corriges/{s['Repere']}) \n \n"
                aff = aff+corr
                #aff+=f"|{s['Repere']}|{s['Centre']}|{s['Jour']}|[{s['Repere']}](../../../officiels/Annales/EE/{annee}/{s['Repere']}.pdf)|[{corr}](../../../Annales/Corriges/{s['Repere']})|\n"
        return aff

    @env.macro
    def corrige_sujetbac(repere):
        aff = f'#<span class="numchapitre">{repere}</span> : Corrigé \n'
        for s in sujet_bac:
            if s['Repere']==repere:
                aff += f"Année : **{s['Annee']}** <br>"
                aff += f"Centre : **{s['Centre']}** <br>"
                aff += f"Jour : **{s['Jour']}** <br>"
                aff += f"Enoncé : [:fontawesome-solid-file-pdf:](../../officiels/Annales/EE/{s['Annee']}/{s['Repere']}.pdf)<br>"
                return aff
    
    @env.macro
    def corrige_sujetbac(repere):
        annee = 2000 + int(repere[0:2])
        if int(annee)<2023:
            nb_exos,sujet_bac = 5,sujet_bac_5exos
        else:
            nb_exos,sujet_bac = 3,sujet_bac_3exos
        aff = f'#<span class="numchapitre">{repere}</span> : Corrigé \n'
        for s in sujet_bac:
            if s['Repere']==repere:
                aff += f"Année : **{s['Annee']}** <br>"
                aff += f"Centre : **{s['Centre']}** <br>"
                aff += f"Jour : **{s['Jour']}** <br>"
                aff += f"Enoncé : [:fontawesome-solid-file-pdf:](../../../officiels/Annales/EE/{s['Annee']}/{s['Repere']}.pdf)<br>"
                aff = f"[:material-arrow-left-circle: Index des sujets {s['Annee']}](../../{s['Annee']}/EE) \n \n" + aff
                return aff

    @env.macro
    def corrige_exobac(repere,num):
        annee = 2000 + int(repere[0:2])
        if int(annee)<2023:
            nb_exos,sujet_bac = 5,sujet_bac_5exos
        else:
            nb_exos,sujet_bac = 3,sujet_bac_3exos
        aff = f'##Exercice {num} '
        for s in sujet_bac:
            if s['Repere']==repere:
                if annee<2023:
                    aff+=f" \n <span class='theme_exo'>*{s['Ex'+str(num)]}*</span> \n"
                else:
                    aff+=f"({s['Pts'+str(num)]} points) \n <span class='theme_exo'>*{s['Ex'+str(num)]}*</span> \n"
                return aff
    
    @env.macro
    def enonce_exobac(repere,num):
        aff = f'##Exercice {num} : '
        for s in sujet_bac:
            if s['Repere']==repere:
                aff+=f"<span class='theme_exo'>*{s['Ex'+str(num)]}*</span> \n"
                return aff
                
    @env.macro
    def binaire(nombre):
        to_disp = '$'
        m = len(nombre)-1
        for c in nombre:
            to_disp += "\overset{\displaystyle{_{2^"+str(m)+"}}}{\\boxed{\\strut"+c+"}}"
            m -= 1
        to_disp += '$'
        return to_disp
    

#---------------- <PYODIDE>-------------------- 
    @env.macro
    def script(lang: str, nom: str) -> str:
        "Renvoie le script dans une balise bloc avec langage spécifié"
        return f"""```{lang}
--8<---  "docs/""" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"""/{nom}"
```"""
    # f"docs/{os.path.dirname(env.variables.page.url.rstrip('/'))}/scripts/{nom}.py"
    
    @env.macro
    def py(nom: str) -> str:
        "macro python rapide"
        return script('python', "scripts/" + nom + ".py")

    env.variables['term_counter'] = 0
    env.variables['IDE_counter'] = 0

    @env.macro
    def terminal() -> str:
        """   
        Purpose : Create a Python Terminal.
        Methods : Two layers to avoid focusing on the Terminal. 1) Fake Terminal using CSS 2) A click hides the fake 
        terminal and triggers the actual Terminal.
        """        
        tc = env.variables['term_counter']
        env.variables['term_counter'] += 1
        return f"""<div onclick='start_term("id{tc}")' id="fake_id{tc}" class="terminal_f"><label class="terminal"><span>>>> </span></label></div><div id="id{tc}" class="hide"></div>"""

    def read_ext_file(nom_script : str) -> str:
        """
        Purpose : Read a Python file that is uploaded on the server.
        Methods : The content of the file is hidden in the webpage. Replacing \n by a string makes it possible
        to integrate the content in mkdocs admonitions.
        """
        short_path = f"""docs/{os.path.dirname(env.variables.page.url.rstrip('/'))}"""
        try: 
            f = open(f"""{short_path}/scripts/{nom_script}.py""")
            content = ''.join(f.readlines())
            f.close()
            content = content+ "\n"
            # Hack to integrate code lines in admonitions in mkdocs
            return content.replace('\n','backslash_newline')
        except :
            return
        
    def generate_content(nom_script : str) -> str:
        """
        Purpose : Return content and current number IDE {tc}.
        """
        tc = env.variables['IDE_counter']
        env.variables['IDE_counter'] += 1

        content = read_ext_file(nom_script)

        if content is not None :
            return content, tc
        else : return "", tc

    def create_upload_button(tc : str) -> str:
        """
        Purpose : Create upoad button for a IDE number {tc}.
        Methods : Use an HTML input to upload a file from user. The user clicks on the button to fire a JS event
        that triggers the hidden input.
        """
        return f"""<button class="emoji" onclick="document.getElementById('input_editor_{tc}').click()">⤴️</button>\
                <input type="file" id="input_editor_{tc}" name="file" enctype="multipart/form-data" class="hide"/>"""

    def create_unittest_button(tc: str, nom_script: str, mode: str) -> str:
        """
        Purpose : Generate the button for IDE {tc} to perform the unit tests if a valid test_script.py is present.
        Methods : Hide the content in a div that is called in the Javascript
        """
        stripped_nom_script = nom_script.split('/')[-1]
        relative_path = '/'.join(nom_script.split('/')[:-1])
        nom_script = f"{relative_path}/test_{stripped_nom_script}"
        content = read_ext_file(nom_script)
        if content is not None: 
            return f"""<span id="test_term_editor_{tc}" class="hide">{content}</span><button class="emoji_dark" onclick=\'executeTest("{tc}","{mode}")\'>🛂</button><span class="compteur">5/5</span>"""
        else: 
            return ''


    def blank_space() -> str:
        """ 
        Purpose : Return 5em blank spaces. Use to spread the buttons evenly
        """
        return f"""<span style="indent-text:5em"> </span>"""

    @env.macro
    def IDEv(nom_script : str ='') -> str:
        """
        Purpose : Easy macro to generate vertical IDE in Markdown mkdocs.
        Methods : Fire the IDE function with 'v' mode.
        """
        return IDE(nom_script, 'v')


    @env.macro
    def IDE(nom_script : str ='', mode : str = 'h') -> str:
        """
        Purpose : Create a IDE (Editor+Terminal) on a Mkdocs document. {nom_script}.py is loaded on the editor if present. 
        Methods : Two modes are available : vertical or horizontal. Buttons are added through functioncal calls.
        Last span hides the code content of the IDE if loaded.
        """
        content, tc = generate_content(nom_script)
        corr_content, tc = generate_content(f"""{'/'.join(nom_script.split('/')[:-1])}/corr_{nom_script.split('/')[-1]}""")
        div_edit = f'<div class="ide_classe">'
        if mode == 'v':
            div_edit += f'<div class="wrapper"><div class="interior_wrapper"><div id="editor_{tc}"></div></div><div id="term_editor_{tc}" class="term_editor"></div></div>'
        else:
            div_edit += f'<div class="wrapper_h"><div class="line" id="editor_{tc}"></div><div id="term_editor_{tc}" class="term_editor_h terminal_f_h"></div></div>'
        div_edit += f"""<button class="emoji" onclick='interpretACE("editor_{tc}","{mode}")'>▶️</button>"""
        div_edit += f"""{blank_space()}<button class="emoji" onclick=\'download_file("editor_{tc}","{nom_script}")\'>⤵️</button>{blank_space()}"""
        div_edit += create_upload_button(tc)
        div_edit += create_unittest_button(tc, nom_script, mode)
        div_edit += '</div>'

        div_edit += f"""<span id="content_editor_{tc}" class="hide">{content}</span>"""
        div_edit += f"""<span id="corr_content_editor_{tc}" class="hide">{corr_content}</span>"""
        return div_edit

#---------------- </PYODIDE>-------------------- 

#-----------------pile et file ------------------
    @env.macro
    def route(routeurs):
        aff = ''
        for i in range(len(routeurs)-1):
            aff += f'{routeurs[i]} :octicons-arrow-right-16: '
        return aff+routeurs[-1]
    
    @env.macro
    def file(elts):
        aff = '<table class="file"><tr>'
        for e in elts:
            aff += f'<td>{e}</td>'
        aff += '</tr></table>'
        return aff
    
    @env.macro
    def pile(elts):
        aff = '<table class="pile">'
        if elts==[]:
            aff += f'<tr><td>&nbsp;</td></tr>'
        for i in range(len(elts)-1,-1,-1):
            aff += f'<tr><td>{elts[i]}</td></tr>'
        aff += '</table>'
        return aff
