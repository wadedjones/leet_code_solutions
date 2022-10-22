# Given an integer array nums, return true if any value appears at least 
# twice in the array, and return false if every element is distinct.


def contains_duplicate(nums: List[int]): -> bool:
    return len(set(nums)) < len(nums)
