from stats import get_num_words, get_book_text
from stats import char_count_sort , character_count , get_book_text , get_num_words , sort_on 
import sys

frankenstein_path = "./books/frankenstein.txt"
frank_txt = get_book_text(frankenstein_path)
def print_pretty_report(texth) :
    sorted = char_count_sort(texth)
    
    print(  f"============ BOOKBOT ============" "\n"
            f"Analyzing book found at {frankenstein_path}..." "\n"
            f"----------- Word Count ----------" "\n"
            f"Found {len(get_num_words(frank_txt))} total words" "\n"
            f"--------- Character Count -------")
    sorted = char_count_sort(texth)

    for l in sorted :
        if str.isalpha(l["char"]) :
            print(f"{l["char"]}: {l["num"]}")
    print("============= END ===============")
# def text_from_path(path_name):
#     file = open(path_name)
#     return file.read()

def main():
    #print("e: 44538\nt: 29493\ne: 119354\nt: 89875\ne: 74451\nt: 50837")
    #print(sys.argv)
    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print_pretty_report(get_book_text(sys.argv[1]))
    
    #print(frank_txt)
main()