def rebase(input_base, digits, output_base):
    decimal = []
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if len(digits) == 0:
        return [0]
    for i in digits:
        if i < 0 or i >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    decimal = convert_to_decimal(input_base, digits)
    return convert_from_decimal(output_base, decimal)


def convert_to_decimal(input_base, digits):
    decimal = 0
    for i in range(len(digits)):
        decimal += digits[i] * input_base ** (len(digits) - i - 1)
    return decimal

def convert_from_decimal(output_base, decimal):
    if decimal == 0:
        return [0]
    digits = []
    while decimal > 0:
        digits.append(decimal % output_base)
        decimal = decimal // output_base
    digits.reverse()
    return digits