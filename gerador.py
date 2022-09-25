import random
import string

c = list(string.ascii_letters + string.digits + "!@#$%¨&*()")

tamanho = int(input("Qual o tamanho da senha que voce deseja?"))


random.shuffle(c)

senha = []
for i in range(tamanho):
    senha.append(random.choice(c))

random.shuffle(senha)

print("".join(senha))