# -*- coding: utf-8 -*-
import os
import sys
import json


ano = input("Selecione o ano: ")
try:
    ano = int(ano)
except:
    print("Ano inválido")
    sys.exit(1)


DIRATUAL = os.path.dirname(os.path.abspath(__file__))

local_arquivo = os.path.join(DIRATUAL,'dados', f'cartola_fc_{ano}.txt')

if not os.path.exists(local_arquivo):
    print("Não existe dados para o ano informado")
    sys.exit(1)
    


try:
    print(local_arquivo)
    with open(local_arquivo, 'rb') as arquivo:
        cartola_dic = json.loads(arquivo.read().decode('utf-8'))
except:
    print("Dados no formato inválido")
    sys.exit(1)

#Item D:
# Definindo a formação do Esquema Tático
defesa, meio, ataque = (0,0,0)
while True:
    try:
        print('escolha a formação:')
        defesa, meio, ataque = (input("Defesa: "),
                               input("Meio: "),
                               input("Ataque: "))
        defesa = int(defesa)
        meio = int(meio)
        ataque = int(ataque)
        assert defesa + meio + ataque == 10
        assert 2 < defesa < 6
        assert 2 < meio < 6
        assert 0 < ataque < 4
        break
    except ValueError:
        print('Insira no formato (numero numero numero)')
    except AssertionError as e:
        print('A formação deve conter 10 jogadores. Sendo: de 3 a 5 defensores; de 3 a 5 meias; de 1 a 3 atacantes.')

existe_laterais = defesa >= 4
quantidade_lat = 2 if existe_laterais else 0
quantidade_zag = defesa - quantidade_lat

quant =  {
    'zag': quantidade_zag,
    'lat': quantidade_lat,
    'mei': meio,
    'ata': ataque,
    'gol': 1,
    'tec': 1
}
melhores_atletas = {
    'zag': [],
    'lat': [],
    'mei': [],
    'ata': [],
    'gol': [],
    'tec': []
}
for atleta in cartola_dic['atletas']:
    posicao = filter(lambda x:x['id'] == atleta['posicao_id'], cartola_dic['posicoes'].values())
    posicao = list(posicao)[0]
    
    atleta_pont = atleta['media_num'] * atleta['jogos_num']
    atleta['pontos_num'] = atleta_pont
    pos = posicao['abreviacao']

    if len(melhores_atletas[pos]) < quant[pos]:
        melhores_atletas[pos].append(atleta)
    else:
        for i, atleta2 in enumerate(melhores_atletas[pos]):
            if atleta2['pontos_num'] < atleta['pontos_num']:
                melhores_atletas[pos][i] = atleta
                break
    melhores_atletas[pos].sort(key=lambda x: x['pontos_num'], reverse=False)


local_arquivo_selecao = os.path.join(DIRATUAL, f'selecao_cartola_fc_{ano}.txt')
with open(local_arquivo_selecao, 'wb') as arquivo_selecao:
    colunas = [
        'posição',
        'nome',
        'url_foto',
        'pontuação',
        'time',
        'url_escudo_time'
    ]
    arquivo_selecao.write(';'.join(colunas).encode('utf8'))


    print('=' * 100)
    print(f'{"Posição".ljust(8," ")} \t {"Nome".ljust(30," ")} \t Time \t\t Pontuação')
    print('=' * 100)
    
    for pos in melhores_atletas:
        for atleta in melhores_atletas[pos]:
            posicao = filter(lambda x:x['id'] == atleta['posicao_id'], cartola_dic['posicoes'].values())
            posicao = list(posicao)[0]
            clube = filter(lambda x:x['id'] == atleta['clube_id'], cartola_dic['clubes'].values())
            clube = list(clube)[0]
            url_escudo_time = clube['escudos'].get('60x60', 'sem escudo')
            url_foto = atleta.get('foto') or 'sem foto'
            linha = [
                posicao["nome"],
                atleta["apelido_abreviado"],
                url_foto,
                str(atleta["pontos_num"]),
                clube["nome"],
                url_foto
            ]
            arquivo_selecao.write(b'\n')
            arquivo_selecao.write(';'.join(linha).encode('utf-8'))

        print(f'{posicao["nome"].ljust(8," ")} \t {atleta["apelido_abreviado"].ljust(30," ")} \t {clube["nome"]} \t {atleta["pontos_num"]}')
