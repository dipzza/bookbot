import sys
from stats import get_num_words


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_file_text(book_path)
    word_count = get_num_words(text)
    char_count = count_characters(text)
    char_count_sorted = chars_dict_to_sorted_list(char_count)

    print(f"--- Begin report of {book_path} ---")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for item in char_count_sorted:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def count_characters(text):
    lower_case_text = text.lower()
    character_counts = {}

    for char in lower_case_text:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    return character_counts


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_file_text(path):
    with open(path) as f:
        return f.read()


main()
