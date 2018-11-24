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
        print('-=' * 25)
        for x in phrase:
            print(f'{x}.')


definição()

