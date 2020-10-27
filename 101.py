'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''



def voto(ano=0):
    from datetime import date
    ano_atual = date.today().year
    voto =  ano_atual - ano

    if voto < 16:
        valor = 'OBRIGATÓRIO'
        return f'Com {voto}a nos o voto é NEGADO'
    elif 16 <= voto < 18 or voto > 65:  
        return f'Com {voto} anos o voto é OPCIONAL' 
    else:
        return f'Com {voto} anos o voto é OBRIGATÓRIO'     



a = int(input('Digite o ano do seu nascimento: '))
print(voto(a))
