""" coding """


def contains_duplicate(nums: list[int]):
    """ duplicate check """
    return len(set(nums)) != len(nums)


def contains_duplicates(nums: list[int]):
    """" another """
    seen: set = set()
    for item in nums:
        if item in seen:
            return True
        seen.add(item)
    return False


if __name__ == "__main__":
    print(contains_duplicates([1, 2, 3, 4, 5, 1]))
    print(contains_duplicate([1, 2, 3, 4, 5, 1]))
    print("=====")
    print(contains_duplicates([1, 2, 3, 4, 5, 7]))
    print(contains_duplicate([1, 2, 3, 4, 5, 7]))
    
