"""
Contains Duplicate
Solved 
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""
def hasDuplicate(nums):
        return not len(nums)==len(set(nums))
nums1 = [1, 2, 3, 3]
nums2=[1, 2, 3, 4]
print(hasDuplicate(nums1))
print(hasDuplicate(nums2))
