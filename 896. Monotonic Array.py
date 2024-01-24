
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        increasing = decreasing = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increasing = False
            elif nums[i] < nums[i - 1]:
                decreasing = False

        return increasing or decreasing
