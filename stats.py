def get_num_words(texto):
    qtd_palavras = len(texto.split())
    return qtd_palavras


def count_characters(texto):
    dicionario = {}
    for letra in texto.lower():
        if letra not in dicionario:
            dicionario[letra] = 1    
        else: 
            dicionario[letra] = dicionario[letra] + 1
    return dicionario

def sorted_list(item):
    return item['num']

def report(listagem):
    lista_dicionarios = []
    for chave, valor in listagem.items():
        dicionario = {}
        dicionario['char'] = chave
        dicionario['num'] = valor
        lista_dicionarios.append(dicionario) 
    lista_dicionarios.sort(reverse = True, key=sorted_list)
    return lista_dicionarios




