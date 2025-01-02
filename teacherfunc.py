from faker import Faker
faker = Faker('pt_BR')
import random
from newdata import subjects, teachers_full, teachers_code_name
import string
from generalfunc import gen_code

    #  print("////////////////////")
    #     print("página de Professores")
    #     print("1 Cadastrar Professor")
    #     print("2 Alocar Professor em uma matéria")
    #     print("3 Alocar professor em uma turma")
    #     print("4 Remover Professor")
    #     print("0 Voltar ao Menu principal")
    #     option = input("Selecione uma das opções: ")
    #     if option == "1":
    #         print("vazio")
    #         print("////////////////////")
    #     elif option == "0":
    #         print("////////////////////")
    

    
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
    # discipline = random.choice(subjects)
    # if discipline in subjects:
        # subjects[discipline].append(name)
    teacher=  {'Nome': name, 'Matrícula': code, 'Nascimento': birth, 'Endereço': adress, "Telefone": cell, "Email": email, "discipline": []}
    teachers_code_name[code] = [name]
    teachers_full.append(teacher)
    print(f"todas as informações {teachers_full}")
    print("")
    print(f"código e nome {teachers_code_name}")
    
    
    

    
