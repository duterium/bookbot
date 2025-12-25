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
def sort_on(items):
    return items["num"]



def char_count_sort(text) :
    # takes input of a string, returns a list of dictionaries sorted from greatest to least containig {"char": '?' , "num" : ***}
    char_dict = character_count(text)
    dict_list = []
    for chr in char_dict :
        # print(f"{chr} : {char_dict[chr]}")
        dict_list.append({
            "char": chr,
            "num": char_dict[chr]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list