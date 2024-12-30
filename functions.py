import random
import string
from faker import Faker 
faker = Faker('pt_BR')
from data import*

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