import string
from random import randint
import threading
import time

alfabeto = string.ascii_lowercase
caracteres = []

for letra in alfabeto:
    caracteres.append(letra)

for numero in range(0 , 10):
    caracteres.append(str(numero))

senha = input("Insira a senha a ser quebrada: ")
senha = senha.lower()
assert len(senha) == 9, "Senha com menos de 9 caracteres"

comeco = time.time()
qtd_tentativas = 0

def funcao_thread(name):
    tentativa = []
    tentar = True
    global qtd_tentativas

    while(tentar):
        qtd_tentativas += 1
        while(len(tentativa) < 9):
            atual = randint(0, len(caracteres)-1)
            tentativa.append(caracteres[atual])
        str_tentativa = ''.join(tentativa)
        print(" {} ".format(str_tentativa))
        if str_tentativa == senha:
            final = time.time() - comeco
            print("A senha foi quebrada na tentativa: {} \nPela Thread: {}\nEm {} ms".format(qtd_tentativas, name, final))
            tentar = False
            exit(0)
        tentativa = []


threads = list()
for index in range(3):
    x = threading.Thread(target=funcao_thread, args=(index,))
    x.start()