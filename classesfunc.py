from newdata import classes_all
from generalfunc import gen_code
# função que adiciona matérias a lista

def clas_add():
    sub_to_add = input("digite o nome da classe a ser adicionada: ")
    if sub_to_add in classes_all:
        print("essa classe já existe")
    else:
        classes_all[sub_to_add] = {"students": [], "teachers": [], "code": gen_code()}
        