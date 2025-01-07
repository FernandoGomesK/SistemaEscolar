import random
import string
from faker import Faker 
faker = Faker('pt_BR')
from main.data import*

def gen_code():
    num = ''.join(str(random.randint(0,9)) for _ in range(4))
    leter = random.choice(string.ascii_uppercase)
    code = leter + num
    return code 

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
    clasn = random.choice(["primeiro", "segundo","terceiro"])
    if clasn in Clas:
        Clas[clasn].append(name)
    student = {'Nome': name, 'Matrícula': code, 'Nascimento': birth, 'Endereço': adress, "Telefone": cell, "Email": email, "clas" : clasn}
    Students.append(student)
    
    

def register_Teacher():
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
    discipline = random.choice(['matemática', 'artes', 'ciência', 'Educação Física', 'português', 'inglês', 'geográfia', 'história'])
    if discipline in subjects:
        subjects[discipline].append(name)
    teacher=  {'Nome': name, 'Matrícula': code, 'Nascimento': birth, 'Endereço': adress, "Telefone": cell, "Email": email, "matéria": discipline}
    Teachers.append(teacher)

def program_start():
    print('////////////////')
    print("")
    print("Bem Vindo ao sistema escolar!")
    print("")
    print('para Cadastrar Aluno: digite 1')
    print('para Cadastrar professor: digite 2')
    print('para cadastrar Disciplina: digite 3')
    print('para Cadastrar Turma: digite 4')
    print('para Filtar professores por disciplina: digite 5')
    print('para Matricular aluno em turnma: digite 6')
    print('para mostrar as turmas: digite 7')
    print('para alocar uma disciplina em uma turma, digite 8')
    print('para sair do programa digite: "n"')
    