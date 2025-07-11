from stats import split_text


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read() 
    return file_contents


def main():
    split_text(get_book_text("books/frankenstein.txt"))


main()
