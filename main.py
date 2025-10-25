from stats import word_count

def main():

    word_num = word_count(get_book_text())
    print(f"Found {word_num} total words")



def get_book_text():

    with open("./books/frankenstein.txt") as f:
        frankenstein=f.read()
    return frankenstein



main()