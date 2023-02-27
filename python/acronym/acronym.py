def abbreviate(words):
    # Replace special characters with spaces
    words = words.replace(" - ", " ").replace("-", " ").replace("_", "").replace(",", "")
    word_list = words.split(" ")
    
    return "".join(word[0].upper() for word in word_list)
