
def _gcf(x: int, y: int) -> int:
    """
    calculates greatest common factor among 2 numbers
    """
    while y:
        x, y = y, x % y
    return x


def gcf(nums: list[int]) -> int:
    """
    calculates greatest common factor among a given list of numbers
    """
    result = nums[0]

    for n in nums[1:]:
        result = _gcf(result, n)

    return result


def _lcm(x: int, y: int) -> int:
    """
    calculates lowest common multiple among two numbers
    """
    return abs(x * y) // _gcf(x, y)


def lcm(nums: list[int]) -> int:
    """
    calculates lowest common multiple among a given list of numbers
    """
    result = nums[0]

    for n in nums[1:]:
        result = _lcm(result, n)

    return result
    
###

def check_prime(n: int) -> bool:
    """
    returns True if a number is prime else False
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # check from 5 to sqrt(n), skipping evens
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
    
def next_prime(n: int) -> int:
    """
    returns the nearest prime number to a given number
    """
    start = n + 1
    while True:
        if check_prime(start):
            return start
        start += 1
        
def prime_factors(n: int) -> dict:
    factors = {}
    divisor = 2

    while divisor * divisor <= n:
        while n % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            n //= divisor

        divisor += 1

    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    return factors