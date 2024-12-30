import random
import string

def gen_code():
    num = ''.join(str(random.randint(0,9)) for _ in range(4))
    leter = random.choice(string.ascii_uppercase)
    code = leter + num
    return code 