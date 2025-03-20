import random
import string

def gerador_de_senha(comprimento_senha = 8):
    ascii_options = string.ascii_letters
    numbers_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + numbers_options + punt_options

    senha_usuario = ""

    for i in range(0, comprimento_senha):
        digit = random.choice(options)
        senha_usuario = senha_usuario + digit

    return senha_usuario

escolha_usuario = input("Quantos digitos tem a senha?")

if escolha_usuario.isdigit():
    escolha_usuario = int(escolha_usuario)
else:
    print("Entrada invalida")
    quit()

resposta = gerador_de_senha(comprimento_senha = escolha_usuario)
print(f"Senha gerada: \n{resposta}")


        