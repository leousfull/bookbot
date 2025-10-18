def get_num_words(texto):
    qtd_palavras = len(texto.split())
    print(f"Found {qtd_palavras} total words")

def count_characters(texto):
    dicionario = {}
    for letra in texto.lower():
        if letra not in dicionario:
            dicionario[letra] = 1    
        else: 
            dicionario[letra] = dicionario[letra] + 1
    print(dicionario)
