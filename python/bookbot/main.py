def get_book_text(PATH):
    with open(PATH) as f:
        file_content = f.read()

    return file_content

def get_book_word_count(PATH):
    word_list = []
    with open(PATH) as f:
        file_content = f.read()
        word_list = file_content.split()

    return len(word_list)

def main():
    print(f"Found {get_book_word_count('./books/frankenstein.txt')} total words")


main()
