def get_book_text(filepath):
    with open(filepath) as f:
        #print(f.read())
        return f.read()
def get_num_words(text):
    arr = text.split()
    return arr