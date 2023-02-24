def sum_of_multiples(limit, multiples):
    xx = []
    for x in range(limit):
        for m in multiples:
            if m == 0:
                continue
            if x % m == 0:
                xx.append(x)
                break
    return sum(xx)
