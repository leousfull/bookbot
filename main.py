from stats import get_num_words, count_characters
def main():
    conteudo = get_book_text("books/frankenstein.txt")
    contagem = get_num_words(conteudo)
    letras = count_characters(conteudo)
def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

main()
