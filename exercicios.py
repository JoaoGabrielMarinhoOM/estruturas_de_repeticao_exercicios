#exercicio1
for num in range(1000, 2001):
    if num % 11 == 5:
        print(num)

#exercicio2
for p in range(1, 11):
    print(f'tabuada do {p}:')
    for s in range(1, 11):
        resultado = (p * s)
        print(f'{p} x {s} = {resultado}')
    print()

#exercicio3
amigos = ["Andrey", "Julio", "Eduardo", "Calvin"]
for amigo in amigos:
    print(amigo)

#exercicio4
num = int(input("Digite um número: "))
print(f' Tabuada do {num}: ')
for i in range(1, 11):
    resultado = num * i
    print(f'{num} x {i} = {resultado}')

#exercicio5
amigos = ["Andrey", "Julio", "Eduardo", "Calvin"]
for amigo in amigos:
    print(f'Olá {amigo}! como vai você?')

#exercicio6
lista_convidados = ["Cristiano Ronaldo", "Neymar", "Ramon Dino", "Renato Cariani", "Cris Bumbsted"]

convidados2 = ["Messi", "Haaland", "Vinicius jr"]

convidados_nao_vao = ["Cristiano Ronaldo", "Neymar", "Cris Bumbsted"]

for convidado in lista_convidados:
    print(f'Saudações {convidado}, é com muita honra e muito carinho que eu te chamo para poder ceiar na minha casa!')
    confirmacao = input(f'Está confirmado sua presença, {convidado}? ')

    if confirmacao == "sim":
        print(f'Então minhas portas estão abertas para você! {convidado}.')
    else:
        print(f'Que pena {convidado}, espero que uma proxima vez de certo.')
    print()

for convidado_nao_vai in convidados_nao_vao:
    print(f'Infelizmente o convidado {convidado_nao_vai} não irá comparecer no jantar.')
    print()

for convidado1 in convidados2:
    print(f'Saudações {convidado1}!, é com muita honra e muito carinho que eu te chamo para poder ceiar na minha casa!')
    confirmacao2 = input(f'Está confirmado sua presença, {convidado1}? ')
    print()
print(f'Espero ansiosamente por todos vocês!')

#exercicio7
print("Olá viajante da internet! Para começar esse cadastro preciso que você coloque algumas informações abaixo:")
print()

usuario = input("Digite um nome e usuário: ")
nome = input("Digite seu nome completo: ")
email = input("Digite seu email: ")
senha = input("Digite uma senha: ")
print()

cadastro = (usuario, nome, email, senha)
conclusao = input(f'{cadastro} Tem certeza que essas informações estão certas? ')
if conclusao == "sim":
    print(f'Então está tudo certo {usuario}! Agora desfrute desse incrivel programa!')
else:
    print("Então reescreva as informações novamente, por favor.")
print()