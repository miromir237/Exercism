# Author: David Prager Branner
# Date: 2017-10-31
# License: Public Domain
# Description: Translate English to Pig Latin.

def translate(text):
    words = text.split()
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = "bcdfghjklmnpqrstvwxyz"
    result = []
    for word in words:
        if word[0] in vowels:
            result.append(word + 'ay')
        elif word[0:2] == 'qu':
            result.append(word[2:] + word[0:2] + 'ay')
        elif word[0] in consonants and word[1:3] == 'qu':
            result.append(word[3:] + word[0:3] + 'ay')
        elif word[0:3] == 'thr':
            result.append(word[3:] + word[0:3] + 'ay')
        elif word[0:3] == 'sch':
            result.append(word[3:] + word[0:3] + 'ay')            
        elif word[0:2] == 'xr':
            result.append(word + 'ay')
        elif word[0:2] == 'yt':
            result.append(word + 'ay')
        elif word[0:2] == 'ch':
            result.append(word[2:] + word[0:2] + 'ay')
        elif word[0:2] == 'th':
            result.append(word[2:] + word[0:2] + 'ay')
        elif word[1] == 'y' and len(word) == 2:
            result.append(word[1:] + word[0] + 'ay')
        elif word[0] in consonants and word[1] in consonants and word[2] == 'y':
            result.append(word[2:] + word[0:2] + 'ay')
        else:
            result.append(word[1:] + word[0] + 'ay')


    return ' '.join(result)

