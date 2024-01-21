https://leetcode.com/problems/length-of-last-word/description/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       s=s.split()
       s=len(s[-1])
       return s
