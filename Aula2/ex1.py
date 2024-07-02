"""
    Criar um sistema para reconhecer o nome, idade, peso, altura.
    Converter a idade para receber somente numeros inteiros.
    Imprimir os tipos de dados
    Imprimir todas as informações concatenadas usando f string 
"""
nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

print(f"\nNome: {nome} Tipo: {type(nome)}, \nIdade: {idade} Tipo: {type(idade)}, \nPeso: {peso} Tipo: {type(peso)}, \nAltura: {altura} Tipo: {type(peso)}")

# print("\nNome: ",nome, type(nome))
# print("Idade: ",idade, type(idade))
# print("Peso:", peso, type(peso))
# print("Altura: ",altura, type(altura))



