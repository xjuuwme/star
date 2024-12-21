""" coding """


def contains_duplicate(nums: list[int]):
    """ duplicate check """
    return len(set(nums)) != len(nums)


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 4, 5, 1]))
    print(contains_duplicate([1, 2, 3, 4, 5, 7]))
    
