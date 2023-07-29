def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True

    # Check for divisibility by numbers from 2 up to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True