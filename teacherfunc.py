from faker import Faker
faker = Faker('pt_BR')
import random
from newdata import teachers_full, subjects
from subjectfunc import show_subject
import string
from generalfunc import gen_code

def resumed_teachers():         
    for code, teacher in teachers_full.items():
        print(f"Matrícula: {code}, nome: {teacher['Nome']}, Turma(s): {teacher['Turmas']}, Matéria(s): {teacher['Materia']}")
                                                                                           
def register_teacher():
    code = gen_code()
    birth = faker.date_of_birth()
    gender = random.choice(["male", "female"])
    if gender == "male":
        name = f"{faker.first_name_male()} {faker.last_name()}"
    else:
        name = f"{faker.first_name_female()} {faker.last_name()}"
    adress = faker.address()
    cell = faker.cellphone_number()
    email = faker.email()
    teacher=  {'Nome': name,
               'Matrícula': code,
               'Nascimento': birth,
               'Endereço': adress,
               "Telefone": cell,
               "Email": email,
               "Materia": [],
               "Turmas": []}
    teachers_full[code] = teacher
    
def remove_teacher():
    resumed_teachers()
    remover = input("digite o código do professor a ser removido: ").upper()
    if remover in teachers_full:
        del teachers_full[remover]
        print("professor removido")
    else:
        print("esse professor não existe")
        
# moves the teacher to a designated subject
def move_teacher():
    resumed_teachers()
    chose_teacher = input("selecione o código do professor a ser movido: ").upper()
    if chose_teacher in teachers_full:
        show_subject()
        chose_subject = input("digite o código da matéria para adicionar o professor: ").upper()
        if chose_subject in subjects:
            teachers_full[chose_teacher]['Materia'].append(subjects[chose_subject])
        else:
            print("comando inválido")          
    else:
        print("esse professor não se encontra no sistema")
    
    
    

    
