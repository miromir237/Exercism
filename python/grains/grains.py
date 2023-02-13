def square(number):
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')
    else:
        return square(number - 1) * 2 if number > 1 else 1


def total():
    total = 0
    for i in range(1, 65):
        total += square(i)
        print('square {}: {} grains'.format(i, square(i)))
    return total

if __name__ == '__main__':
    print(total())

# Path: python/grains/grains_test.py
   #square 1:  1 grain 
   #square 2:  2 grains = 2 * square(1) 
   #square 3:  4 grains = 2 * square(2)
   #square 4:  8 grains = 2 * square(3)
   #square 5: 16 grains = 2 * square(4)
   #square 6: 32 grains = 2 * square(5)