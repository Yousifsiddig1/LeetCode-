https://leetcode.com/problems/single-number-ii/description/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums : 
            if nums.count(i) == 1 : 
                return  i
# Faster Solution

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num_count = {}

        # Count occurrences of each number
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        # Find the number with count 1
        for num, count in num_count.items():
            if count == 1:
                return num

            
