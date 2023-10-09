import random, os

DIRATUAL = os.path.dirname(os.path.abspath(__file__)) 

# ----------------------------------------------------------------------
def gerar_lista(quantidade:int, valor_minimo:int=1, valor_maximo:int=1000000):
    boolSucesso = False
    lstRetorno  = None

    lista = []
    for n in range(quantidade):
        num = random.randint(valor_minimo,valor_maximo)
        lista.append(num)
    if len(lista) == quantidade:
        boolSucesso = True
        lstRetorno = lista
    else:
        boolSucesso = False
        lstRetorno  = None
        
    return boolSucesso, lstRetorno


# ----------------------------------------------------------------------
def salvar_lista(nome_lista: list, nome_arquivo: str):
    boolSucesso  = False
    nome_arquivo = DIRATUAL + '\\' + nome_arquivo

    arquivo = (open(f'{nome_arquivo}', 'w'))
    arqatual = os.path.dirname(nome_arquivo)
    for a in range(len(nome_lista)):
        arquivo.write(str(f'\n{nome_lista[a]}'))
    if arqatual == DIRATUAL:
        boolSucesso = True

    return boolSucesso