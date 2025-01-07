from data import subjects, classes_all
from generalfunc import gen_code
from classesfunc import show_clas


def register_subject():
    sub_code = gen_code()
    new_sub = input("digite o nome da matéria a ser adicionada: ").lower()
    if new_sub in subjects:
        print("essa matéria já existe")
    else:
        subjects[sub_code] = [new_sub]
        
def show_subject():
    organized_sub = sorted(subjects.keys())
    for code, subject in subjects.items():
        print(f"Código: {code}, matéria: {subjects[code]}")

def remove_subject():
    show_subject()
    sub_remover = input("digete o código da matéria a ser removida: ").upper()
    if sub_remover in subjects:
        del subjects[sub_remover]
        print("matéria removida com sucesso")
    else:
        print("essa matéria não se encontra na lista de matérias")

def assign_subject():
    show_subject()
    print("digite o nome da matéria para ser adicionada a uma turma")
    chose_subject = input("selecione o código da Disciplina a ser movida: ").upper()
    if chose_subject in subjects:
        show_clas()
        chose_clas = input("digite o código da Turma para adicionar a Disciplina: ").upper()
        if chose_clas in classes_all:
            classes_all[chose_clas]['Matérias'].append(subjects[chose_subject])
        else:
            print("comando inválido")          
    else:
        print("essa Matéria não se encontra no sistema")

