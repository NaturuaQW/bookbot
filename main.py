
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total_words = count_words(text)
    total_letter_count = count_letters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{total_words} words found in the document")
    sorted_list = sorted(total_letter_count.items(), key=lambda item: item[1], reverse = True) #can use valuegetter as key
    for x in sorted_list:
        print(f"The '{x[0]}' character was found {x[1]} times")
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(x):
    count = 0
    words = x.split()
    for word in words:
        count += 1
    return count

def count_letters(words):
    letter_count = {}
    for word in words:
        word = word.lower()
        for letter in word:
            if letter in letter_count:
                letter_count[letter] += 1
            if letter.isalpha() and letter not in letter_count:
                letter_count[letter] = 1
    return(letter_count)
    
def value_getter(item):
    return item[1]

main()
