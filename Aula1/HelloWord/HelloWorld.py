"""
Comentario 
    de 
        Bloco
"""

# Comentário de Linha
print("Hello world!")

# Caclular média
nota1 = 30
nota2 = 50
nota3 = 40

# Processamento #
soma = nota1 + nota2 + nota3
media = soma / 3

print(media)

# Variáveis
nome = "Rafael" 
peso = 70.0
altura = 1.75
instrutor = False # True e False, inciais maiúsculas

print("nome: "+nome)
print(altura, type(altura)) # Verificar o tipo da variavel
print(instrutor, type(instrutor))
print(nome, altura, peso)

# Convertendo valor

valor = 15
print(valor, type(valor)) 
valor = str(valor) # Converte o valor da variavel valor(int) para String
print(type(valor))

# Entradada de dados pelo input, e salvando na variavel nome

nome = input("\nDigite o seu nome:")
print("Meu nome é: "+nome)
print("\n\n")

idade = int(input("Digite a sua idade: ")) # Converter em inteiro
print(idade, type(idade))


# Concatenaço 3 formas diferentes~

print('\nOlá meu nome é: '+nome + '! Tenho: '+ str(idade)+ ' de idade') # 1° Forma

print('\nOlá, meu nome é: ',nome, 'Tenho ', idade, 'anos de idade') # 2 ° Forma

print(f'Olá, meu nome é: {nome} tenho {idade} de idade')# 3° Forma