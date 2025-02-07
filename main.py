
import random
import string
from subjectfunc import register_subject, show_subject, remove_subject, assign_subject
from data import subjects, teachers_full, classes_all, students_full
from teacherfunc import register_teacher, remove_teacher, resumed_teachers, move_teacher_subject, move_teacher_clas
from classesfunc import clas_add, show_clas, remove_clas
from generalfunc import error_message
from studentfunc import register_student, remove_student, complete_students, move_student

working = True

def students_page():
    while True:
        print("////////////////////")
        print("página de Estudantes")
        print("1 Ver Todos os Alunos")
        print("2 Cadastrar Aluno")
        print("3 Remover Aluno")
        print("4 Alocar aluno em uma turma")
        print("0 Voltar ao Menu principal")
        option = input("Selecione uma das opções: ")
        if option == "1":
            complete_students()
        elif option =="2":
            register_student()
        elif option == "3":
            remove_student()
        elif option == "4":
            move_student()    
        elif option == "0":
            print("////////////////////")
            break
        else:
            error_message()
        
def teachers_page():
    while True:
        print("////////////////////")
        print("página de Professores")
        print("1 Cadastrar Professor")
        print("2 Alocar Professor em uma matéria")
        print("3 Alocar professor em uma turma")
        print("4 Remover Professor")
        print("5 ver todos os professores")
        print("0 Voltar ao Menu principal")
        option = input("Selecione uma das opções: ")
        if option == "1":
            register_teacher()
            print("professor Adicionado")
        elif option == "2":
            move_teacher_subject()
        elif option == "3":
            move_teacher_clas()   
        elif option == "4":
            remove_teacher()
        elif option == "5":
            resumed_teachers()
        elif option == "0":
            print("////////////////////")
            return
        else:
            error_message()
            
def subjects_page():
    while True:
        print("////////////////////")
        print("Página de Disciplinas")
        print("1 Visualizar Todas as Disciplinas")
        print("2 Adicionar uma disciplina")
        print("3 Alocar disciplina em uma turma")
        print("4 remover uma disciplina")
        print("0 voltar ao menu principal")
        # selection of subject options
        option = input("selecione uma das opções: ") 
        if option == "1":
            show_subject()
        elif option == "2":
            register_subject()
        elif option == "3":
            assign_subject()
        elif option == "4":
            remove_subject()
        elif option == "0":
            print("voltando a página principal")
            print("////////////////////")
            return
        else:
            error_message()
                    
def classes_page():
    while True:
        print("////////////////////")
        print("Página de turmas")
        print("1 Visualizar todas as turmas")
        print("2 Adicionar uma turma")
        print("3 remover uma turma")
        print("0 voltar ao menu principal")
        option = input("selecione uma das opções: ")
        if option == "1":
            show_clas()
        elif option == "2":
            clas_add()
        elif option == "3":
            remove_clas()
        elif option == "0":
            print("voltando a página principal")
            print("////////////////////")
            return
        else:
            error_message()
            
def exitprog():
    print("obrigado por utilizar o Sistema Escolar 2025")
    global working
    working = False
    
def program_start():
    print("Bem vindo ao Sistema Escolar 2025, selecione uma das opções disponíveis")
    print("1 Página de Alunos")
    print("2 página de professores")
    print("3 página de disciplinas")
    print("4 página de turmas")
    print("0 para sair do Sistema")

start_menu = {
    "1": students_page,
    "2": teachers_page,
    "3": subjects_page,
    "4": classes_page,
    "0": exitprog
}
   
while working:
        program_start()
        option = input("Escolha a página a acessar: ")
        if option in start_menu:
            start_menu[option]()
        else:
            print("opção inválida, tente novamente")
        
          
