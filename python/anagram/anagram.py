def find_anagrams(word, candidates):
    return [c for c in candidates if is_anagram(word, c)]

def is_anagram(word, candidate):
    return (
        word.lower() != candidate.lower()
        and sorted(word.lower()) == sorted(candidate.lower())
    )
