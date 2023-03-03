import re

def count_words(sentence):
    word_count = {}
    # split sentence by any white form of white space or punctuation
    for word in re.split(r"\s|,|:|!|\.|\&|\@|\$|\%|\^|_", sentence):
        # remove any leading or trailing punctuation
        word = word.strip("'")
        # ignore empty strings
        if word:
            # convert to lowercase
            word = word.lower()
            # add to dictionary
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    
    return word_count
