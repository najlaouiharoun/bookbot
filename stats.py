def word_count(book_strig):
    word_list = book_strig.split()
    return len(word_list)

def repetition_count(book_strig):
    lowercase_book_string = book_strig.lower()
    letter_dictionary = {}
    for letter in lowercase_book_string:
        if letter in letter_dictionary:
            letter_dictionary[letter]+=1
        else:
            letter_dictionary[letter]=1
    return letter_dictionary



