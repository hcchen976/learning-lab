#def get_book_word_count(PATH):
#    word_list = []
#    with open(PATH) as f:
#        file_content = f.read()
#        word_list = file_content.split()
#
#    return len(word_list)


def get_num_words(text):
    words = text.split()
    return len(words)

def count_char(text: str) -> dict:
    char_dict = {}

    for char in text:
        char = char.lower()
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    return char_dict



