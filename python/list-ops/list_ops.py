

def append(list1, list2):
    return list1 + list2


def concat(lists):
    return sum(lists, [])


def filter(function, list):
    return [x for x in list if function(x)]


def length(list):
    return len(list)


def map(function, list):
    return [function(x) for x in list]


def foldl(function, list, initial):
    # Given a function, a list, and initial accumulator, fold (reduce) each item into the accumulator from the left using function(accumulator, item).
    for element in list:
        initial = function(initial, element)
    return initial


def foldr(function, list, initial):
    for element in list[::-1]:
        initial = function(element, initial)
    return initial


def reverse(list):
    return list[::-1]
