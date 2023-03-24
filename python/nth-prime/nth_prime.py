# Function that determine what the nth prime is
def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")
    else:
        primes = [2]
        i = 3
        while len(primes) < number:
            for prime in primes:
                if i % prime == 0:
                    break
            else:
                primes.append(i)
            i += 2
        return primes[-1]
