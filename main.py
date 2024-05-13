def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()








# Old Code
# def main(): 
#     # store book path in a variable
#     book_path = "books/frankenstein.txt"

#     #store a variable that opens the book from it's path
#     text = get_book_text(book_path)

#     #store num of words in a variable using function that splits the text and returns the len of words
#     num_words = get_num_words(text)

#     # Count the occurences of each character in the text
#     char_counts = get_num_appears(text)

#     #prints out num_words
    

#     print(char_counts)

#     char_list = []
#     for c in char_counts:
#         char_list.append({"char": c, "num": char_counts[c]})


#     char_list.sort(key=sort_on, reverse=True)

#     print(f"--- Begin report of '{book_path}' ---")
#     print(f"{num_words} words found in the document")
#     print()
#     # iterate over now sorted char_list
#     for char in char_list:
#         print(f"The '{char['char']}' character was found {char['num']} times")
#     print("--- End report ---")




# def sort_on(dict):
#     return dict["num"]

# def get_num_appears(text):
#     count_dictionary = {}
#     for char in text:
#         char = char.lower()
#         if char.isalpha():
#             if char in count_dictionary:
#                 count_dictionary[char] += 1
#             else:
#                 count_dictionary[char] = 1
#     return count_dictionary

# def get_num_words(text):
#     words = text.split()
#     return len(words)


# def get_book_text(path):
#     with open("books/frankenstein.txt") as f:
#         return f.read()

# main()
