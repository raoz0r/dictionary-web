import urllib.request
import json
import re


def search():
    data = urllib.request.urlopen('http://dicionario-aberto.net/search-json/celula')
    return json.load(data)

def clean(a):
    clear = ('<br/>', ':', 'gramGrp', ',', 'def', "'", '{', '}', '@id',
             'usg', '@type', 'dom', '#text', '[', ']')
    orth = a['entry']['form']['orth']
    for c in range(0, len(d['entry']['sense'])):
        clean = str(a['entry']['sense'])
    for p in clear:
        clean = clean.replace(p, '')
    clean = re.split(r'[.]', clean)
    clean.pop()
    return orth, clean

def imprimir(orth, lista):
    print(orth)
    for x in lista:
        print(f'{x.strip()}.')



d = search()
orth, lista = clean(d)
imprimir(orth, lista)


'''

            for x in range(0, len(d['entry']['sense'])):
                de = str(d['entry']['sense'][x])
                for x in clean:
                    de = de.replace(x, '')
                phrase = re.split(r'[.]', de.strip())
                phrase.pop()
                print('-=' * 25)
                for x in phrase:
                    print(f'{x}.')'''

