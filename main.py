def get_book_text(filepath):
    with open(filepath) as f:
        #print(f.read())
        return f.read()
def get_words(text):
    arr = text.split()
    return arr
def main():
    arr = get_words(get_book_text("./books/frankenstein.txt"))
    num_words = len(arr)
    print (f"Found {num_words} total words")

main()