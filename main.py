import sys
from stats import (display_word_count, count_characters, sorted_dict)

def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        book_path = sys.argv[1]

        try:
            content = get_book_text(book_path)
        except FileNotFoundError:
            print(f"Error: Could not find file at {book_path}")
            return
        except Exception as e:
            print(f"Error reading file: {e}")
            return

        word_count = display_word_count(content)
        chars = count_characters(content)
        sorted_chars = sorted_dict(chars)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for items in sorted_chars:
            chars = items['char']
            count = items['count']
            if chars.isalpha():
                print(f"{chars}: {count}")
        print("============= END ===============")



if __name__ == "__main__":
    main()
