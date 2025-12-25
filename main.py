from stats import get_num_words, get_book_text
from stats import char_count_sort , character_count , get_book_text , get_num_words , sort_on 

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


def main():
    #print_pretty_report(frank_txt)
    #print("e: 44538\nt: 29493")
    print(frank_txt)
main()