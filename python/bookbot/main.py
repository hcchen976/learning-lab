import sys
from stats import (
    get_num_words, 
    count_char, 
    sort_dict,
)


def get_book_text(PATH):
    with open(PATH) as f:
        return f.read()

def print_report(book_path, num_words, char_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    print("--------- Character Count -------")

    for item in sort_dict(char_dict):
        if item["char"].isalpha():
            print(item["char"],": ", item["num"], sep="")
    
    print("============= END ===============")

def check_sys_argv():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    check_sys_argv()
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = count_char(text)
    chars_sorted_list = sort_dict(char_dict)
    
    print_report(book_path, num_words, char_dict)


main()

