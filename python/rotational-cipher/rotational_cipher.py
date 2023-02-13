def rotate(text, key):
    """Rotate the characters in a string by a given amount.

    This is a simple Caesar cipher, also sometimes called a rotation cipher.
    """
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            result += char
    return result