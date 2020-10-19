pessoas = {'nome':'Edson', 'sexo': 'M', 'idade': 31}

print(pessoas)    
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
del pessoas['sexo']
pessoas['nome'] = 'Onishi'
pessoas['peso'] = 90

for k,v in pessoas.items():
    print(f' {k} = {v}')

brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}    
estado2 = {'uf':'Sao Paulo ', 'sigla':'SP'}   
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0]['sigla'])
print(brasil[1]['uf'])

estado = dict()
for c in range(0,2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())# Fucao copy para copiar um dicionario 
print(brasil)    

for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}')

for e in brasil:
    for v in e.values():
        print(v, end=' ')