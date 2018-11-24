import urllib.request
import json
import re


def definição():
    data = urllib.request.urlopen(f'http://dicionario-aberto.net/search-json/celula')
    d = json.load(data)
    clean = ('<br/>', ':', 'gramGrp', ',', 'def', "'", '{', '}')
    for x in range(0, len(d['entry']['sense'])):
        de = str(d['entry']['sense'][x])
        for x in clean:
            de = de.replace(x, '')
        phrase = re.split(r'[.]', de.strip())
        phrase.pop()
        #print('-=' * 25)
        #print(f'Palavra a ser procurada: ')
        print('-=' * 25)
        for x in phrase:
            print(f'{x}.')


#print('-=' * 25)
definição()
#print('-=' * 25)

'''O programa ainda não consegue buscar palavras com acento
   Algumas palavras o key do dicionário é SuperEntry ao invés de Entry
   Algumas palavras possuem mais de uma definição preciso de uma solução para isso também.
   Precisa arrumar a formatação dos itens'''
