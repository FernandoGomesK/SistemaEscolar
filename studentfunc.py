from generalfunc import gen_code
from newdata import students_full, subjects
from subjectfunc import show_subject
import random
import string
from faker import Faker
faker = Faker('pt_BR')

def resumed_students():
    for code, student in students_full.items():
        print(f"Matrícula: {code}, Nome: {student['Nome']}, Turma: {student['Turma']}")
        print("////////////////////")
        
def complete_students():
    print("////////////////////")
    print("Mostrando Todos os Alunos")
    for code, student in students_full.items():
        print(f"Matrícula: {code}, Nome: {student['Nome']}, Turma: {student['Nascimento']}, Endereço: {student['Endereco']}, Telefone: {student['Telefone']}, Email: {student['Email']}, Turma: {student['Turma']}")
        print("////////////////////")

def register_student():
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
    student = {'Nome': name,
               'Matrícula': code,
               'Nascimento': birth,
               'Endereco': adress,
               "Telefone": cell,
               "Email": email,
               "Turma" : []}
    students_full[code] = student

def remove_student():
    resumed_students()
    remover = input("digite o código do Aluno a ser removido").upper
    if remover in students_full:
        del students_full[remover]
        print("Aluno Removido")
    else:
        print("Esse Aluno não existe")
        
def move_student():
    resumed_students()
    chose_student = input("selecione o código do Aluno a ser movido: ").upper()
    if chose_student in students_full:
        show_subject()
        chose_subject = input("digite o código da matéria para adicionar o aluno: ").upper()
        if chose_subject in subjects:
            students_full[chose_student]['Materia'].append(subjects[chose_subject])
        else:
            print("comando inválido")          
    else:
        print("esse aluno não se encontra no sistema")