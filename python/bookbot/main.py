from stats import get_num_words, count_char, sort_dict

def get_book_text(PATH):
    with open(PATH) as f:
        return f.read()


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = count_char(text)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")

    for item in sort_dict(char_dict):
        print(item["char"],": ", item["num"], sep="")
    
    print("============= END ===============")

main()
