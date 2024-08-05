def main() :
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    chars_dict = characters_count(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count(text)} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def sort_on(d):
    return d["num"]

def get_book_text(book_path):
    
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def word_count(text):
    words = text.split()
    return len(words)

def characters_count(text):
    characters={}
    
    for word in text:
        word_lowered = word.lower()
        for char in word_lowered:
            if char not in characters:
            
                characters[char] = 1
                
            else:
                characters[char] += 1
    return characters

main()