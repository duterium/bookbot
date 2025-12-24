def get_book_text(filepath):
    #takes input of file path and returns the content as a string 
    with open(filepath) as f:
        #print(f.read())
        return f.read()

def get_num_words(text):
    #takes input of a string and returns a list (array) containg that string split at white space
    arr = text.split()
    return arr

def character_count(text):
    char_dict = {}
    for c in text:
        if c in char_dict :
            char_dict[c] += 1
        else :
            char_dict[c] = 1
    return char_dict
