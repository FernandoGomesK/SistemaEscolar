from newdata import classes_all
from generalfunc import gen_code
# função que adiciona matérias a lista

def show_clas():
    for code, clas in classes_all.items():
        print(f"Código: {code}, Nome: {clas['Nome']}, Alunos: {clas["Estudantes"]}, Professores: {clas["Professores"]}, Matérias: {clas["Matérias"]}")

def clas_add():
    clas_to_add = input("digite o nome da classe a ser adicionada: ")
    if clas_to_add in classes_all:
        print("essa classe já existe")
    else:
        classes_all[gen_code()] = {"Estudantes": [], "Professores": [], "Matérias": [], "Nome": clas_to_add}
        print(classes_all)
        
def remove_clas():
    show_clas()
    remover = input("digite o código da turma a ser removido").upper
    if remover in classes_all:
        del classes_all[remover]
        print("Turma removida")
    else:
        print("Essa turma não existe")