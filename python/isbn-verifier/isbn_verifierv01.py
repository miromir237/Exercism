def is_valid(isbn):
    numbers = [int(x) if x.isdigit() else 10 if x == 'X' else 0 for x in isbn.replace('-', '')]
    return len(numbers) == 10 and sum(x * (10 - i) for i, x in enumerate(numbers)) % 11 == 0