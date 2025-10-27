#!/usr/bin/python3


import sys
from stats import word_count
from stats import repetition_count
from stats import sort_dictionary
from stats import print_dict_list

def main():
    if len(sys.argv) == 2:
        print_report()
        return
    print("Usage: python3 main.py <path_to_book>. wrong path error")
    sys.exit(1)

def print_report():
    book = sys.argv[1]
    content = get_book_text(book)
    word_num = word_count(content)
    character_count = repetition_count(content)
    sorted_character_count=sort_dictionary(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {word_num} total words")
    print(f"--------- Character Count -------")
    print_dict_list(sorted_character_count)
    print("============= END ===============")

def get_book_text(book):

    with open(book) as f:
        frankenstein=f.read()
    return frankenstein


main()
