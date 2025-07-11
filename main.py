from stats import word_count, char_count, sort_on_letters


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read() 
    return file_contents


def main():
    book_text=get_book_text("books/frankenstein.txt")
    total_word_count=word_count(book_text)
    word_dic=char_count(book_text)
    sorted_dic = sort_on_letters(word_dic)
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------\nFound {total_word_count} total words")
    print("--------- Character Count -------")
    for dic in sorted_dic:
        if dic["char"].isalpha():
            print(f"{dic["char"]}: {dic["num"]}")



main()
