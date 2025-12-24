from stats import get_num_words, get_book_text
from stats import *
def main():
    arr = get_num_words(get_book_text("./books/frankenstein.txt"))
    num_words = len(arr)
    print (f"Found {num_words} total words")

main()