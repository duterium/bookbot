from stats import get_num_words, get_book_text
from stats import *

frankenstein_path = "./books/frankenstein.txt"
frank_txt = get_book_text(frankenstein_path)

def main():
    print(character_count(str.lower(frank_txt)))
main()