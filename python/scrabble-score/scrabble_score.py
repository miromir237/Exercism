def score(word):
    scoring = {
        'AEIOULNRST': 1,
        'DG': 2,
        'BCMP': 3,
        'FHVWY': 4,
        'K': 5,
        'JX': 8,
        'QZ': 10,
    }
    score = 0
    for letter in word.upper():
        for key, value in scoring.items():
            if letter in key:
                score += value

    return score
