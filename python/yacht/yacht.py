# Score categories.
# Change the values as you see fit.
YACHT = [[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3],[4,4,4,4,4],[5,5,5,5,5],[6,6,6,6,6]]
ONES = [1]
TWOS = [2]
THREES = [3]
FOURS = [4]
FIVES = [5]
SIXES = [6]
FULL_HOUSE = [0, 0, 0, 0, 2, 3]
FOUR_OF_A_KIND = [4*[1],4*[2],4*[3],4*[4],4*[5],4*[6]]
LITTLE_STRAIGHT = [[1,2,3,4,5]]
BIG_STRAIGHT = [[2,3,4,5,6]]
CHOICE = "CHOICE"

def isYacht(roll):
    counts = [roll.count(die) for die in range(1,7)]
    print(counts)
    return 5 in counts

def isFullHouse(roll):
    counts = [roll.count(die) for die in range(1,7)]
    counts.sort()
    print(counts)
    return counts == [0, 0, 0, 0, 2, 3]

def isFourOfAKind(roll):
    counts = [roll.count(die) for die in range(1,7)]
    return 4 in counts

def score(dice, category):
    if category == ONES:
        return dice.count(1)
    if category == TWOS:
        return dice.count(2) * 2
    if category == THREES:
        return dice.count(3) * 3
    if category == FOURS:
        return dice.count(4) * 4
    if category == FIVES:
        return dice.count(5) * 5
    if category == SIXES:
        return dice.count(6) * 6
    if category == FOUR_OF_A_KIND and (isFourOfAKind(dice) or isYacht(dice)):
        for i in range(1, 7):
            if dice.count(i) >= 4:
                return i * 4
    if category == FULL_HOUSE and isFullHouse(dice):
        if isYacht(dice):
            return 0
        return sum(dice)
    if category == LITTLE_STRAIGHT and sorted(dice) in LITTLE_STRAIGHT:
        return 30
    if category == BIG_STRAIGHT and sorted(dice) in BIG_STRAIGHT:
        return 30
    if category == CHOICE:
        return sum(dice)        
    if category == YACHT and isYacht(dice):
        return 50
    else:
        return 0
