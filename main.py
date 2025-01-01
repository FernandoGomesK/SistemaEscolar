from faker import Faker 
faker = Faker('pt_BR')
import random
import string
from functions import* 
from data import*

resp = 'A'
while(resp == 'A'):
    program_start()
    resp = input("digite um número: ")
    if resp == "1":
        while resp == "1":
            print("digite s para cadastrar Aluno")
            print("digite n para sair da aba de cadastro")
            select_student = input('s/n: ')
            if select_student == "s":
                register_student()
                print(Students)
                print('////////////////')
                resp = "1"
            elif select_student == "n":
                resp = "A"
                print('////////////////')
            else:
                print("comando inválido")
                print('////////////////')          
        
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
                
    elif resp =="3":
        while resp == "3":
            print("digite s para adicionar uma matéria")
            print("digite n para sair da aba de cadastro")
            subject_writing = input("s/n: ")
            if subject_writing == "s":
                print("o máximo de matérias já foi atingido")
                print('////////////////') 
                resp = "A"
            elif subject_writing =="n":
                resp= "A"
            else:
                print("comando inválido")
                print('////////////////') 
            
                
    elif resp == "5":
        while resp == "5":
            for x in subjects.keys():
                print(x)
            select = input("selecione a matéria para visualização dos professores: ")
            if select in subjects:
                print(subjects[select])
                second_subject = input("deseja consultar outra matéria? s/n: ")
                if second_subject == "s":
                    resp = "5"
                elif second_subject == "n":
                    resp = "A"
                else:
                    print("comando inválido, tente novamente")
                    print('////////////////')               
            else:
                print("comando inválido, tente novamente")
    
    elif resp == "7":
        print(Clas)
        resp = "A"
        
    elif resp == "n":
        print("Obrigado por utilizar este programa!")
    else:
        print("comando inválido")
        print('////////////////')
        resp = 'A'

        

