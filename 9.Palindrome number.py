#Input: x = 121
#Output: true
#Explanation: 121 reads as 121 from left to right and from right to left.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        length = len(x_str)

        for i in range(length // 2): 
            if x_str[i] != x_str[length - 1 - i]:
                return False

        return True
