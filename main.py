def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read() 
    return file_contents

def split_text(text):
    split_list= text.split()
    word_count=len(split_list)
    print(f"{word_count} words found in the document")
    return word_count



def main():
    split_text(get_book_text("books/frankenstein.txt"))


main()
