def encode(plain_text):
    atbash = str.maketrans('abcdefghijklmnopqrstuvwxyz1234567890', 'zyxwvutsrqponmlkjihgfedcba1234567890', ' !@#$%^&*()_+-=,./<>?;:[]{}|`~')
    encoded = plain_text.lower().translate(atbash)
    # split encoded by 5 characters
    encoded = ' '.join(encoded[i:i+5] for i in range(0, len(encoded), 5))
    return encoded

def decode(ciphered_text):
    atbash = str.maketrans('zyxwvutsrqponmlkjihgfedcba1234567890','abcdefghijklmnopqrstuvwxyz1234567890', ' !@#$%^&*()_+-=,./<>?;:[]{}|`~')
    return ciphered_text.lower().translate(atbash)
