import shutil
md_path = '/home/fenarius/Travail/Cours/fabricenativel.github.io/docs/Terminale/Annales/Corriges/'
py_path = '/home/fenarius/Travail/Cours/fabricenativel.github.io/python/terminale/annales'

print("Copie de fichiers de corrections ")
old_annee = input("Ancienne année du sujet : ")
old_num = input("Ancien numéro du sujet : ")
new_annee = input("Nouvelle année du sujet : ")
new_num = input("Nouveau numéro du sujet : ")

old_num = old_num.zfill(2)
new_num = new_num.zfill(2)


old_md_name = f"{md_path}/{old_annee}-S{old_num}.md"
new_md_name = f"{md_path}/{new_annee}-S{new_num}.md"

old_ex1_name = f"{py_path}/{old_annee}-S{old_num}-ex1.py"
new_ex1_name = f"{py_path}/{new_annee}-S{new_num}-ex1.py"

old_ex2_name = f"{py_path}/{old_annee}-S{old_num}-ex2.py"
new_ex2_name = f"{py_path}/{new_annee}-S{new_num}-ex2.py"

shutil.copy(old_ex1_name,new_ex1_name)
shutil.copy(old_ex2_name,new_ex2_name)

with open(old_md_name) as md:
    content = md.read()

content = content.replace(f'% set annee = {old_annee} %',f'% set annee = {new_annee} %')
content = content.replace(f'% set numero = "{old_num}" %',f'% set numero = "{new_num}" %')

with open(new_md_name,"w") as md:
    md.write(content)

print("Work done !")
