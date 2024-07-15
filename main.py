def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    words_dict = get_chars_dict(text)
    print("--- Begin Reports of", book_path , "---")
    print(num_words, "words found in the document")
    print()
    lists_of_dicts = get_list_of_dict(words_dict)
    for dict in lists_of_dicts:
        print("the", dict["word"], "character was found", dict["count"], "times")
    print("--- End report ---")




def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_list_of_dict(words_dict):
    list_dicts = []
    for dict in words_dict:
        new_dict = {}
        if dict.isalpha():
            new_dict["word"] = dict
            new_dict["count"] = words_dict[dict]
            list_dicts.append(new_dict)
    list_dicts.sort(reverse=True, key=sort_on)
    #print(list_dicts)
    return(list_dicts)

def sort_on(dict):
    return dict["count"]

def get_chars_dict(text):
    words_dict = {}
    for word in text:
        lowered = word.lower()
        if lowered not in words_dict:
            words_dict[lowered] = 1
        else:
            words_dict[lowered] += 1
    return words_dict



main()