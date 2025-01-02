from newdata import subjects

def register_subject():
    new_sub = input("digite o nome da matéria a ser adicionada: ").lower()
    if new_sub in subjects:
        print("essa matéria já existe")
    else:
        subjects[new_sub] = []

def show_subject():
    print(sorted(subjects.keys()))

def remove_subject():
    show_subject()
    sub_remover = input("digete o nome da matéria a ser removida: ").lower()
    if sub_remover in subjects:
        del subjects[sub_remover]
    else:
        print("essa matéria não se encontra na lista de matérias")

def assign_subject():
    pass

