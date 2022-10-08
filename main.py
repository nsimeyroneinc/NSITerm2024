import os
from cgitb import small
import csv

def define_env(env):
    "Hook function"

#---------------- <exo perso>-------------------- 

    @env.macro
    def correction(bool, texte):
        if bool == False:
            return ""
        else:
            return texte



    @env.macro
    def initexo(n):
        env.variables['compteur_exo'] = n
        return ""




    env.variables['compteur_exo'] = 0
    @env.macro
    def exercice():
        env.variables['compteur_exo'] += 1
        return f"Exercice  { env.variables['compteur_exo']}"

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
    def titre_correction(annee,numero):
        ligne=f"# Corrigé sujet <span class='numchapitre'>{numero}</span> - Année : {annee} "
        return ligne
    
    @env.macro
    def correction_ex1(annee,numero):
        modele = f'''
```python3 linenums="1" \n
--8<-- "python/{annee}-S{numero}-ex1.py"\n
```\n'''
        return modele
    
    @env.macro
    def correction_ex2(annee,numero,hl):
        modele = f'''
```python3 linenums="1" hl_lines="{hl}"\n
--8<-- "python/{annee}-S{numero}-ex2.py"\n\n
```'''
        return modele

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
        return f"<span class='centre'>[Sujet {numero} - 20222 :material-download:](../../officiels/Annales/EP/{annee}/{code}/{code}.pdf)"+"{.md-button}</span>"

    
    @env.macro
    def code_insert(chap,nom,ntab=0):
        stab = '\t'*ntab
        modele = f'''
{stab}```python3 linenums="1" \n
{stab}--8<-- "python/C{chap}/{nom}"\n
{stab}```'''
        return modele



