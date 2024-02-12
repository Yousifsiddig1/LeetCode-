https://leetcode.com/problems/move-zeroes/description/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0
        r = 0
        while r < len(nums):
            if nums[r] != 0:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
            r += 1
