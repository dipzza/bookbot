def main():
  book_path = "books/frankenstein.txt"
  text = get_file_text(book_path)
  word_count = count_words(text)
  char_count = count_characters(text)
  char_count_sorted = chars_dict_to_sorted_list(char_count)

  print(f"--- Begin report of {book_path} ---")
  print(f"{word_count} words found in the document")
  print()

  for item in char_count_sorted:
    if item["char"].isalpha():
      print(f"The '{item['char']}' character was found {item['num']} times")

  print("--- End report ---")

def count_words(text):
  words = text.split()
  return len(words)

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