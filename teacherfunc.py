# from faker import Faker
# faker = Faker('pt_BR')
from datetime import*
import random
from data import teachers_full, subjects, classes_all
from subjectfunc import show_subject
import string
from generalfunc import gen_code, verify_gender, check_email, check_number
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
        birth = input("digite a data de nascimento DD/MM/AAAA: ")
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
    gender = verify_gender()
            
    while True:       
        adress = input("digite o endereço do Professor: ").strip()
        if adress:
            break
        else:
            print("endereço inválido")
            
    while True:
        cell = input("digite o número de telefone do Professor (+** (**) *****-**): ").strip()
        if not cell:
            print("Por favor digite um número válido")
            continue      
        if not check_number(cell):
            print("Número inválido, por favor digite no formato (+** (**) *****-**):")
            continue
        break
        
    while True:
        email = input("digite o Email: ").strip()
        if not email:
            print("por favor digite um endereço de e-mail válido")
            continue  
        if not check_email(email):
            print("E-Mail inválido")
            continue
        break
    
    teacher=  {'Nome': name,
               'Matrícula': code,
               'Gênero': gender,
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
            
            if chose_teacher not in classes_all[chose_clas]['Professores']:
                classes_all[chose_clas]['Professores'].append(chose_teacher)
            else:
                print("esse Professor já se encontra nessa turma")
                
            if chose_clas not in teachers_full[chose_teacher]['Turma']:
                teachers_full[chose_teacher]['Turma'].append([chose_clas])
            else:
                print("Este Professor já se encontra nessa turma")   
                
    else:
        print("esse professor não se encontra no sistema")
    

    
