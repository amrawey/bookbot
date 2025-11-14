import sys
from stats import word_count, chars_appearance_count,sorted_chars_by_appearance

def get_book_text(file_path):
        with open(file_path) as f:
         file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    count = word_count(text)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------")
    print(f"Found {count} total words\n--------- Character Count ------")
    sorted_chars = sorted_chars_by_appearance(text)
    for char, appearance in sorted_chars:
        print(f"{char}: {appearance}")
    print("============= END ===============")

main()

