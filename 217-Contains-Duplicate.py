"""
Given an integer array nums, return true if any value appears at least
twice in the array, and return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums:list[int]) -> bool:
        return len(nums)>len(set(nums))


s=Solution()
print(s.containsDuplicate(nums=[1,2,3,4]))
print(s.containsDuplicate(nums=[1,2,2,3,4]))
    