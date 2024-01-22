https://leetcode.com/problems/valid-anagram/description/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listForS=list(s)
        listForT=list(t)
        #Now we sort the lists
        listForS.sort()
        listForT.sort()
        if listForS == listForT:
            return True
        else:
            return False



