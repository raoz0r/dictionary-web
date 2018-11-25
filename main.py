import urllib.request
import urllib.parse
import json
import re


def search(word):
    word = urllib.parse.quote(word)
    data = urllib.request.urlopen('http://dicionario-aberto.net/search-json/' + word)
    return json.load(data)

def clean(a):
    clear = ('<br/>', 'geo', 'gramGrp', ',', 'def', "'", '{', '}', '@id',
             'usg', '@type', 'dom', '#text', '[', ']', '@ast', '1', ':',
             'Bras')
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



d = search('Jacaré')
orth, lista = clean(d)
imprimir(orth, lista)
