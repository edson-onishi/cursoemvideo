'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário 
com as seguintes informações:
- Quantidade de notas                                                                                                                                                  
– A maior nota                                                                                                                                                                
– A menor nota                                                                                                                                                              
– A média da turma                                                                                                                                                      
– A situação (opcional)'''

def notas(*n,situacao=False):
    """
    Programa para recever varias notas de uma turma e guarda em um dicionario
    :param n: recebe varios numeros
    :param situacao: (opcional) guarda a situacao da media da turma.
    :return: retorna um dicionario com a maior, menor e media da turma e a situacao.
    """
    turma = dict()
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['media'] = sum(n)/len(n)
    if situacao:
        if turma['media'] < 5: 
            turma['situacao'] = 'RUIM'
        elif turma['media'] >= 7:
            turma['situacao'] = 'BOA'
        else:
            turma['situacao'] = 'EXCELENTE'     
    return turma

r = notas(2,3,4,5,situacao=True)

print(r)