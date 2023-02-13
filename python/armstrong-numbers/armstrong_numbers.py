def is_armstrong_number(number):
    power = len(str(number))
    sum = 0
    for digit in str(number):
        sum += int(digit) ** power

    return sum == number
