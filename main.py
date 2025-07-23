from stats import word_count, char_count, sort_on_letters
import sys

#Reading in the the .txt file and returing as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read() 
    return file_contents


def main():
    #Testing to make sure the command include the file path to the book
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        #Reading in file path and sending to get_book_text
        book_text=get_book_text(sys.argv[1])
        #Calling word_count to get the total word count
        total_word_count=word_count(book_text)
        #Calling char_count to get the a dictionary of all the words in the text
        word_dic=char_count(book_text)
        #Calling sort_on_letters to get dictionary ex. {"char": "b", "num": 4868}
        sorted_dic = sort_on_letters(word_dic)
        print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...")
        print(f"----------- Word Count ----------\nFound {total_word_count} total words")
        print("--------- Character Count -------")
        for dic in sorted_dic:
            if dic["char"].isalpha():
                print(f"{dic["char"]}: {dic["num"]}")



main()
