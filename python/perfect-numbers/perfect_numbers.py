def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        # Initialize the sum of the divisors
        asum = 0
        # Loop through the divisors
        for i in range(1, number):
            if number % i == 0:
                # Add the divisor to the sum
                asum += i
        # Return the classification
        if asum == number:
            return "perfect"
        elif asum > number:
            return "abundant"
        else:
            return "deficient"