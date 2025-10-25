from stats import word_count
from stats import repetition_count
def main():
    letter_count = repetition_count(get_book_text())
    word_num = word_count(get_book_text())
    print(f"Found {word_num} total words")
    print(f"and this is the lettter count: {letter_count}")



def get_book_text():

    with open("./books/frankenstein.txt") as f:
        frankenstein=f.read()
    return frankenstein



main()