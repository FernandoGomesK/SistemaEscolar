# from faker import Faker
# faker = Faker('pt_BR')
from datetime import*
import random
from newdata import teachers_full, subjects, classes_all
from subjectfunc import show_subject
import string
from generalfunc import gen_code
from classesfunc import show_clas

def resumed_teachers():         
    for code, teacher in teachers_full.items():
        print(f"Matrícula: {code}, nome: {teacher['Nome']}, Turma(s): {teacher['Turmas']}, Matéria(s): {teacher['Materia']}")
                                                                                           
def register_teacher():
    #Validação do Nome
    while True:
        name = input("Digite o nome do professor: ").strip()
        if len(name.split()) >= 2 and name.replace(" ", '').isalpha():
            break
        else:
            print("nome inválido")
    #gera o código do professor      
    code = gen_code()
    #Verifica a idade, e se o professor tem mais de 18 anos
    while True:
        birth = input("digite a data de nascimento: DD/MM/AAAA")
        try:
            works = datetime.strptime(birth, "%d/%m/%Y")
            age = (datetime.now() - works).days // 365
            if age >= 18:
                     break
            else: 
                    print("o Professor deve ser maior de 18 anos")
        except ValueError:
                print("Data inválida, Utilize o formato DD/MM/AAAA")
    #Verifica o Genero
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
    
    teacher=  {'Nome': name,
               'Matrícula': code,
               'Nascimento': birth,
               'Endereço': adress,
               "Telefone": cell,
               "Email": email,
               "Materia": [],
               "Turmas": []}
    teachers_full[code] = teacher
    
# deletes the teacher from the system
def remove_teacher():
    resumed_teachers()
    remover = input("digite o código do professor a ser removido: ").upper()
    if remover in teachers_full:
        del teachers_full[remover]
        print("professor removido")
    else:
        print("esse professor não existe")
        
# moves the teacher to a designated subject
def move_teacher_subject():
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
        
# moves the teacher to a designated class
def move_teacher_clas():
    resumed_teachers()
    chose_teacher = input("selecione o código do professor a ser movido: ").upper()
    if chose_teacher in teachers_full:
        show_clas()
        chose_clas = input("digite o código da matéria para adicionar o professor: ").upper()
        if chose_clas in classes_all:
            classes_all[chose_clas]['Professores'].append(teachers_full[chose_teacher])
        else:
            print("comando inválido")          
    else:
        print("esse professor não se encontra no sistema")
    

    
