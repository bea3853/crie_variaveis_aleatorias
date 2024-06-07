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



# CRIAÇÃO DE VARIÁVEIS E DESEMPATANDO DA LISTA 
# CRIANDO NOVOS DICIONÁRIOS




a,b,c,d =  [1,3,6,6,]
d = dict(a=a,b=b,c=c,d=d)
print(d)

a,b,c,d =  [1,3,6,6,]
d = dict(a=a,b=b,c=c,d=d)
a = list(d.keys())
f =  tuple(d.values())
g =  d.items()
print(a, f)
