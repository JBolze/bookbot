def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---\n")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document.\n")
    num_characters = count_characters(text)
    
    for char_data in process_characters(num_characters):
        if char_data["character"].isalpha():
            print(f"The {char_data['character']} character was found {char_data['num']} times.")
    
    print("\n--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    character_count = {}
    lower_text = text.lower()

    for character in lower_text:
        if character in character_count:
            character_count[character] += 1
        elif character not in character_count:
            character_count[character] = 1
    return character_count

def transform(char_count):
    return [{"character": char, "num": count} for char, count in char_count.items()]

def sort_transformed_list(char_list):
    char_list.sort(key=lambda item: item["num"], reverse=True)
    return char_list

def process_characters(char_count):
    char_list = transform(char_count)
    sorted_list = sort_transformed_list(char_list)
    return sorted_list

    

main()