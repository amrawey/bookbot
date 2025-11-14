def word_count(text):
    words = text.split()
    return len(words)

def chars_appearance_count(text):
    char_count = {}
    for char in text:
        if char.isalpha():  # Consider only alphabetic characters
            char = char.lower()
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def sorted_chars_by_appearance(text):
    char_count = chars_appearance_count(text)
    sorted_chars = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    return sorted_chars