import random
import string
import re

def gen_code():
    num = "".join(str(random.randint(1,9)) for _ in range(1,4))
    letter = random.choice(string.ascii_uppercase)
    code = letter + num
    return code

def error_message():
    print("Opcção inválida, tente novamente!")
    print("////////////////////")

def verify_gender():
    while True:
        gender = input("Digite o Gênero: M/F: ").strip().upper()
        if gender == "M":
            return "Masculino"
        elif gender == "F":
            return "Feminino"
        else:
            print("Gênero inválido")

def check_email(x):
        pattern = r'^([a-z\d.-]+)@([a-z\d-]+)\.([a-z]{2,8})(\.[a-z]{2,8})?$'
        if re.match(pattern, x):
            return True
        return False
    
def check_number(x):
    pattern =    r'^\+(\d{1,3})\s\((\d{1,3})\)\s(\d{4,5})-(\d{4})$'
    if re.match(pattern, x):
        return True
    return False