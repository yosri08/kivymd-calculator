

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