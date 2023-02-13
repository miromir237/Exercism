def is_valid(isbn):
    i = 0
    sum = 0

    numbers = isbn.split('-')
    numbers = ''.join(numbers)
    
    if len(numbers) != 10:
        return False
    else:
        for x in numbers:
            if x.isdigit():
                sum += int(x) * (10 - i)
            elif x == 'X' and i == 9:
                sum += 10 * (10 - i)
            else:
                return False
            i+=1
        return sum % 11 == 0