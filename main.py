import sys
from stats import (
    get_num_words,
    count_characters,
    report
)





def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_path = sys.argv[1]

    conteudo = get_book_text(book_path)
    contagem = get_num_words(conteudo)
    letras = count_characters(conteudo)
    reporte = report(letras)
    impressao(book_path,contagem,reporte)




def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def impressao(book_path,contagem,reporte):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {contagem} total words")
    print("----------- Character Count -------")
    for i in reporte:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")
        else:
            continue
    print("============= END ===============")

main()
