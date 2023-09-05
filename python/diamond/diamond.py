def rows(letter):

    # Return ord of letter
    letter_ord = ord(letter)
    # Return range of letters from A to letter
    letters = [chr(i) for i in range(65, letter_ord + 1)]
    # Return length of letters
    n = len(letters)

    # print letters
    #print(letters)

    # if letters is A then return A
    if letters == ['A']:
        return ['A']

    # Return array of letters
    rows = []
    for i in range(n):
        letter = letters.pop(0)
        print(i)
        # if letters are not empty
        if letters:
            if letter == 'A':
                rows.append( (n-1)*' ' + 'A' + (n-1)*' ' )
            else:
                rows.append( (n-i-1)*' ' + letter + (i+(i-1))*' ' + letter + (n-i-1)*' ')
        else:
            rows.append( letter + (i+(i-1))*' ' + letter )
            # Return rows + reverse rows
            return rows + rows[::-1][1:]
        #print(rows[i])

    
    
    

def main():
    #print(rows('G'))
    for i in rows('A'):
        print(i)

if __name__ == '__main__':
    main()

# Path: difference-of-squares/difference_of_squares.py
