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


