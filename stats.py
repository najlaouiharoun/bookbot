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


def sort_dictionary(dictionary):
    def sort_on_helper(items):
        return items["num"]
    dic_list=[]
    for item  in dictionary:
        dic_list.append({"name":item,"num":dictionary[item]})
    
        
    dic_list.sort(reverse=True,key=sort_on_helper)
    return dic_list

sort_dictionary(repetition_count("sussus amogus"))

def print_dict_list(list):
    for dict in list:
        if dict["name"].isalpha():
            print(f"{dict["name"]} : {dict["num"]}")