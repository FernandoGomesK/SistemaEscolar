from faker import Faker 
faker = Faker('pt_BR')
import random
import string

Students = []

subjects = {'matemática': [], 
            'artes': [],
            'ciência': [],
            'Educação Física': [],
            'português': [],
            'inglês': [],
            'geográfia': [],
            'história': []}

Teachers = []

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
    Students.append(student)
    student = {'Nome': name, 'Matrícula': code, 'Nascimento': birth, 'Endereço': adress, "Telefone": cell, "Email": email}

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

resp = 'A'
while(resp == 'A'):
    print('para Cadastrar Aluno: digite 1')
    print('para Cadastrar professor: digite 2')
    print('para cadastrar Disciplina: digite 3')
    print('para Cadastrar Turma: digite 4')
    print('para Filtar professores por disciplina: digite 5')
    print('para Matricular aluno em turnma: digite 6')
    print('para sair do programa digite: "n"')
    resp = input("digite um número: ")
    if resp == "1":
        register_student()
        print(Students)
        resp = 'A'
    elif resp =="2":
        while resp == "2":
            print("digite s para cadastrar professor")
            print("digite n para sair da aba de cadastro")
            select_teacher = input("s/n: ")
            if select_teacher == "s":
                register_Teacher()
                print(Teachers)
                print('////////////////')
                resp = "2"
            elif select_teacher == "n":
                resp = "A"
                print('////////////////')
            else:
                print("comando inválido")
                print('////////////////')   
    elif resp == "5":
        for x in subjects.keys():
            print(x)
        select = input("selecione a matéria para visualização dos professores: ")
        if select in subjects:
            print(subjects[select])
    elif resp == "n":
        print("Obrigado por utilizar este programa!")
    else:
        print("comando inválido")
        print('////////////////')
        resp = 'A'

        

