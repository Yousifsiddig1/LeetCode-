https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
# bad solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        i=0
        while i < len(nums):
            for j in nums:
                if nums.count(j)>2:
                    nums.pop(nums.index(j))
                else:
                    k+=1
            i +=1
        return k
# Better solution ( 66ms memory time )

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        i = 0
        while i < len(nums):
            if nums.count(nums[i]) > 2:
                nums.pop(i)
            else:
                i += 1
                k += 1
        return k
        
