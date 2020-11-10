def aumentar(n, taxa, formato = False):
    """
        Calcula o aumento de um determinado valor,
        retornando o resultado com ou sem formatacao.
        :param n: valor a ser ajustado.
        :param taxa: Porcentagem de aumento
        :param formato: Saida formatada ou nao
        :return: o valor ajustado com o sem formatacao.
    """
    r =  n + (n * taxa/100)
    return r if formato is False else moeda(r)
    

def diminuir(n, taxa,formato = False):
    r = n - (n * taxa/100)
    return r if formato is False else moeda(r)

def dobro(n,formato = False):
    r = n * 2
    return r if formato is False else moeda(r)


def metade(n,formato = False):
    r = n / 2
    return r if formato is False else moeda(r)

def moeda(n):
    return f'{n:8.2f}'.replace('.',',')   

def resumo(n,taxa,d):
    print('-' * 30)
    print('Resumo do Valor'.center(30))
    print('-' * 30)