from stats import get_num_words, count_char

def get_book_text(PATH):
    with open(PATH) as f:
        return f.read()


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f'Found {num_words} total words')
    print(count_char(text))

main()
