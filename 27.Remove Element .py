# Beats 83%
class Solution:
 
    def removeElement(self, nums: List[int], val: int) -> int:
        i =0
        while i < len(nums):
            if val in nums : 
                nums.remove(val)
            else:
                i +=1
       
