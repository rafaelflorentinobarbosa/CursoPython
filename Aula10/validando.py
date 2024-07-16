cpf = ['121.834.496-24']

novo_cpf = input('Digite um CPF: ')

if novo_cpf in cpf:
    print(f'O CPF já existe: ')
else:
    cpf.append(novo_cpf)
    print('CPF cadastrado com sucesso!')

print(cpf)