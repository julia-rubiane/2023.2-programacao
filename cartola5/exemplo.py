import requests, json

cartola_dic = requests.get('https://api.cartolafc.globo.com/atletas/mercado')
cartola_dic = cartola_dic.json()
atletas = cartola_dic['clubes']
#print(atletas)
print(cartola_dic [atletas:3])

'''print(cartola_dic.keys)
latletas = cartola_dic ['atletas']
dposicoes = cartola_dic ['posicoes']
dclubes = cartola_dic ['clubes']
'''
'''for atleta in latletas:
    print(dposicoes[atleta['posicao_id']] ['nome'])
    print(atleta['apelido'])
    print(dclubes [atleta['clube_id']] ['nome']  ['60x60'])
    print(atleta['jogos_num'] * atleta['media_num'])
    print (atleta['foto'])
'''