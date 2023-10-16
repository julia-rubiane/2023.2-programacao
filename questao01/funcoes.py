import random, os

DIRATUAL = os.path.dirname(os.path.abspath(__file__)) 


# ----------------------------------------------------------------------
def gerar_lista(quantidade:int, valor_minimo:int=1, valor_maximo:int=1000000):
    boolSucesso = False
    lstRetorno  = None

    lista = []
    for _ in range(quantidade):
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
    nome_arquivo = os.path.join(DIRATUAL, nome_arquivo)

    try:
        with open(f'{nome_arquivo}', 'w') as arquivo:
            arquivo.write('\n'.join([str(x) for x in nome_lista]))
    except:
        return False
    else:
        return True
    

def ler_arquivo(nome_arquivo: str):
    try:
        with open(f'{nome_arquivo}', 'r') as arquivo:
            lista_arquivo = [int(s) for s in arquivo.read().splitlines()]
            return True, lista_arquivo
    except:
        return False, None


def ordena_lista(nome_lista, metodo_ordena):
    ...


def ordena_bubble(nome_lista: str):
    ordenado = False
    lista_ordenada = [x for x in nome_lista]
    try:
        while not ordenado:
            ordenado = True
            ultimo = len(lista_ordenada) - 1
            for i in range(0, ultimo):
                if lista_ordenada[i] > lista_ordenada[i + 1]:
                    ordenado = False
                    item = lista_ordenada[i] 
                    lista_ordenada[i] = lista_ordenada[i + 1]  
                    lista_ordenada[i + 1] = item
        return True, lista_ordenada
    
    except:
        return False, None


def ordena_insertion(nome_lista):
    lista_ordenada = [x for x in nome_lista]
    try:
        for i in range(1, len(lista_ordenada)):
            for j in range(i, 0, -1):
                if lista_ordenada[j] < lista_ordenada[j - 1]:
                    item = lista_ordenada[j] 
                    lista_ordenada[j] = lista_ordenada[j - 1]  
                    lista_ordenada[j - 1] = item
                else:
                    break
        return True, lista_ordenada
    except:
        return False, None

def ordena_selection (nome_lista):
    lista_ordenada = [x for x in nome_lista]
    try:
        for i in range(0, len(lista_ordenada) -1):
            menor_indice = i
            for j in range(i + 1, len(lista_ordenada)):
                if lista_ordenada[j] < lista_ordenada[menor_indice]:
                    menor_indice = j
            if menor_indice > i:
                item = lista_ordenada[i] 
                lista_ordenada[i] = lista_ordenada[menor_indice]
                lista_ordenada[menor_indice] = item
        return True, lista_ordenada
    except:
        return False, None


def ordena_quick (nome_lista):
    lista_ordenada = [x for x in nome_lista]
    try:
        def quick(inicio, fim):
            if inicio < fim:
                pivo = lista_ordenada[inicio]
                i = inicio
                for j in range(inicio+1, fim):
                    if pivo > lista_ordenada[j]:
                        i += 1
                        item = lista_ordenada[j]
                        lista_ordenada[i] = lista_ordenada[j]
                        lista_ordenada[j] = item
                        
                item = lista_ordenada[i]
                lista_ordenada[i] = lista_ordenada[inicio]
                lista_ordenada[inicio] = item
                i += 1
                quick(inicio, i -1)
                quick(i +1, fim)
        quick(0, len(lista_ordenada))
        return True, lista_ordenada
    except:
        return False, None