from generalfunc import gen_code
from newdata import students_full, subjects, classes_all
from subjectfunc import show_subject
from classesfunc import show_clas
import random
import string
from datetime import*
# from faker import Faker
# faker = Faker('pt_BR')

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
    while True:
        name = input("Digite o nome do aluno(Nome e Sobrenome): ").strip()
        if len(name.split()) >= 2 and name.replace(" ", "").isalpha():
            break
        else:
            print("Nome inválido")
    #gera um código para o aluno
    code = gen_code()
    
    while True:
        birth = input("digite a data de nascimento do aluno: DD/MM/AAAA: ")
        try: 
            works = datetime.strptime(birth, "%d/%m/%Y")
            if works <= datetime.now():
                break
            else:
                print("A data de nascimento não pode ser maior que a data atual")           
        except ValueError:
            print("Data inválida, Utilize o formato DD/MM/AAAA")
            

    while True:
        gender = input("Digite o Gênero: M/F: ").upper()
        if gender == "M":
            gender = "Masculino"
            break
        elif gender == "F":
            gender = "Feminino"
            break
        else:
            print("Gênero inválido")
    while True:       
        adress = input("digite o endereço do Aluno: ").strip()
        if adress:
            break
        else:
            print("endereço inválido")
            
    while True:
        cell = input("digite o número de telefone do responsável: ").strip()
        if cell:
            break
        else:
            print("número inválido")
        
    while True:
        email = input("digite o Email: ").strip()
        if email:
            break
        else:
            print("E-Mail, inválido")
        
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
        show_clas()
        chose_clas = input("digite o código da turma para adicionar o aluno: ").upper()
        if chose_clas in classes_all:
            classes_all[chose_clas]['Estudantes'].append(students_full[chose_student])
        else:
            print("comando inválido")          
    else:
        print("esse aluno não se encontra no sistema")