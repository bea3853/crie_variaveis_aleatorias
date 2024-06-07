import random 
import string

def criarvar(numer):
    var = {}
    for _ in range(numer):
        nome_var = ''.join(random.choices(string.ascii_letters, k=3))
        valor_var = random.randint(1,100)
        var[nome_var] = valor_var
    return var

r = criarvar(4)

for nome_var in r:
    print(nome_var)
