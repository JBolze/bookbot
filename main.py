character_count = {}

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    num_characters = count_characters(text)
    print(num_characters)


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    lower_text = text.lower()

    for character in lower_text:
        if character in character_count:
            character_count[character] += 1
        elif character not in character_count:
            character_count[character] = 1
    return character_count

    

main()